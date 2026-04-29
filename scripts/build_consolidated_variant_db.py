#!/usr/bin/env python3
"""Build a branch-scoped MiSTer Downloader database for a mapping variant.

This is intended for a consolidated MiSTercade repository where each
install option lives on its own source branch, and each source branch publishes
to a matching database branch:

    maps-v2-osd -> db-maps-v2-osd

The stock DB-Template_MiSTer build script supports DB_ID, but it always publishes
to a branch named "db" and hardcodes the database URL to that branch. This wrapper
keeps DB_ID, DB_URL, BASE_FILES_URL, and the publish branch aligned per variant.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Iterable


DEFAULT_REPO_NAME = "MiSTercade"
DEFAULT_REPO_SLUG = "misteraddons/MiSTercade"
DEFAULT_DB_OPERATOR_URL = (
    "https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/"
    "main/.github/db_operator.py"
)
DEFAULT_FINDER_IGNORE = (
    "README.md",
    "LICENSE",
    "CLAUDE.md",
    "AGENTS.md",
    ".DS_Store",
    "scripts",
    "db.json",
    "db.json.zip",
)


def main() -> int:
    args = parse_args()
    source_dir = Path(args.source_dir).resolve()
    if not source_dir.exists():
        raise SystemExit(f"source directory does not exist: {source_dir}")

    variant_key = normalize_variant_key(args.variant_key or current_branch(source_dir))
    repo_slug = (args.repo_slug or DEFAULT_REPO_SLUG).strip().strip("/")
    db_branch = args.db_branch or f"db-{variant_key}"
    db_id = args.db_id or f"{repo_slug}/{variant_key}"
    db_url = f"https://raw.githubusercontent.com/{repo_slug}/{db_branch}/db.json.zip"
    base_files_url = f"https://raw.githubusercontent.com/{repo_slug}/%s/"

    db_operator = resolve_db_operator(args.db_operator)

    print(f"{DEFAULT_REPO_NAME} consolidated database build")
    print(f"  source_dir:     {source_dir}")
    print(f"  variant_key:    {variant_key}")
    print(f"  repo_slug:      {repo_slug}")
    print(f"  db_id:          {db_id}")
    print(f"  db_branch:      {db_branch}")
    print(f"  db_url:         {db_url}")
    print(f"  base_files_url: {base_files_url}")
    print(f"  publish:        {args.publish}")
    print()
    sys.stdout.flush()

    build_database(
        source_dir=source_dir,
        db_operator=db_operator,
        db_id=db_id,
        db_url=db_url,
        base_files_url=base_files_url,
    )

    db_json = source_dir / "db.json"
    if not db_json.exists():
        raise SystemExit("db_operator did not create db.json")

    db_zip = source_dir / "db.json.zip"
    zip_database(db_json, db_zip)
    drop_ins = create_drop_in_database_files(source_dir, db_id, db_url)

    print()
    print("Generated:")
    print(f"  {db_json}")
    print(f"  {db_zip}")
    for path in drop_ins:
        print(f"  {path}")

    if args.publish:
        publish_database(source_dir, db_branch, [db_zip, *drop_ins])
    else:
        print()
        print("Build-only run complete. Re-run with --publish to force-push the DB branch.")

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a variant-specific MiSTer Downloader database."
    )
    parser.add_argument(
        "--variant-key",
        default=os.getenv("MISTERCADE_VARIANT_KEY"),
        help="Variant/source branch key, for example maps-v2-osd.",
    )
    parser.add_argument(
        "--repo-slug",
        default=os.getenv("GITHUB_REPOSITORY", DEFAULT_REPO_SLUG),
        help="GitHub repository slug used in generated URLs.",
    )
    parser.add_argument(
        "--db-branch",
        help="Database branch to publish. Defaults to db-{variant-key}.",
    )
    parser.add_argument(
        "--db-id",
        help="Downloader DB_ID. Defaults to {repo-slug}/{variant-key}.",
    )
    parser.add_argument(
        "--db-operator",
        default=os.getenv("DB_OPERATOR_PATH"),
        help="Path to db_operator.py. Downloads the upstream copy when omitted.",
    )
    parser.add_argument(
        "--source-dir",
        default=".",
        help="Directory containing the installable files for this variant.",
    )
    parser.add_argument(
        "--publish",
        action="store_true",
        help="Create an orphan DB branch and force-push it to origin.",
    )
    return parser.parse_args()


def normalize_variant_key(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^refs/heads/", "", value)
    value = re.sub(r"^origin/", "", value)
    value = value.lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = value.strip("._-")
    if not value:
        raise SystemExit("Unable to derive a variant key. Pass --variant-key.")
    return value


def current_branch(cwd: Path) -> str:
    ref = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=cwd, capture=True)
    branch = ref.stdout.strip()
    if branch == "HEAD":
        sha = run(["git", "rev-parse", "--short", "HEAD"], cwd=cwd, capture=True).stdout.strip()
        return f"detached-{sha}"
    return branch


def resolve_db_operator(configured_path: str | None) -> Path:
    if configured_path:
        path = Path(configured_path).expanduser().resolve()
        if not path.exists():
            raise SystemExit(f"db_operator.py not found: {path}")
        return path

    temp_dir = Path(tempfile.mkdtemp(prefix="mistercade-db-"))
    target = temp_dir / "db_operator.py"
    print(f"Downloading db_operator.py to {target}")
    urllib.request.urlretrieve(DEFAULT_DB_OPERATOR_URL, target)
    return target


def build_database(source_dir: Path, db_operator: Path, db_id: str, db_url: str, base_files_url: str) -> None:
    external_files = existing_external_file_args(source_dir)
    generated_ignores = existing_generated_ignore_args(source_dir)
    finder_ignore = " ".join(
        [
            os.getenv("FINDER_IGNORE", "").strip(),
            " ".join(DEFAULT_FINDER_IGNORE),
            " ".join(external_files),
            " ".join(generated_ignores),
        ]
    ).strip()

    env = os.environ.copy()
    env.update(
        {
            "DB_ID": db_id,
            "DB_URL": db_url,
            # Always emit a fresh db.json. The upstream helper can decide
            # "no changes" and skip writing the artifact, but our source branch
            # SHA may still have changed after a force-push.
            "TEST_DB_URL": os.getenv("TEST_DB_URL", f"{db_url}.force-rebuild"),
            "DB_JSON_NAME": "db.json",
            "BASE_FILES_URL": base_files_url,
            "FINDER_IGNORE": finder_ignore,
            "BROKEN_MRAS_IGNORE": os.getenv("BROKEN_MRAS_IGNORE", "true"),
        }
    )
    if external_files:
        env["EXTERNAL_FILES"] = " ".join(external_files)
    else:
        env.pop("EXTERNAL_FILES", None)

    run([sys.executable, str(db_operator), "build", "."], cwd=source_dir, env=env)


def existing_external_file_args(source_dir: Path) -> list[str]:
    return [
        filename
        for filename in ("external_files.csv", "external_repos_files.csv")
        if (source_dir / filename).exists()
    ]


def existing_generated_ignore_args(source_dir: Path) -> list[str]:
    ignored = [str(path.relative_to(source_dir)) for path in source_dir.rglob(".DS_Store")]
    ignored.extend(path.name for path in source_dir.glob("downloader_*.ini"))
    ignored.extend(path.name for path in source_dir.glob("downloader_*.zip"))
    return sorted(set(ignored))


def zip_database(db_json: Path, db_zip: Path) -> None:
    if db_zip.exists():
        db_zip.unlink()
    with zipfile.ZipFile(db_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.write(db_json, "db.json")


def create_drop_in_database_files(source_dir: Path, db_id: str, db_url: str) -> list[Path]:
    sanitized_db_id = sanitize_db_id_for_filename(db_id)
    ini_path = source_dir / f"downloader_{sanitized_db_id}.ini"
    zip_path = source_dir / f"downloader_{sanitized_db_id}.zip"
    contents = f"[{db_id}]\ndb_url = {db_url}\n"

    ini_path.write_text(contents, encoding="utf-8", newline="\n")
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr(ini_path.name, contents)

    return [ini_path, zip_path]


def sanitize_db_id_for_filename(db_id: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9._-]+", "_", db_id).strip("._-")
    if not sanitized:
        raise ValueError(f'Unable to derive a drop-in filename from DB_ID "{db_id}"')
    return sanitized


def publish_database(source_dir: Path, db_branch: str, publish_files: Iterable[Path]) -> None:
    run(["git", "config", "user.email", os.getenv("GIT_AUTHOR_EMAIL", "actions@github.com")], cwd=source_dir)
    run(["git", "config", "user.name", os.getenv("GIT_AUTHOR_NAME", "MiSTercade DB Builder")], cwd=source_dir)
    run(["git", "checkout", "--orphan", db_branch], cwd=source_dir)
    run(["git", "reset"], cwd=source_dir)
    run(["git", "add", *[str(path.relative_to(source_dir)) for path in publish_files]], cwd=source_dir)
    run(["git", "commit", "-m", f"Build {db_branch} database"], cwd=source_dir)
    run(["git", "push", "--force", "origin", db_branch], cwd=source_dir)


def run(
    cmd: list[str],
    *,
    cwd: Path,
    env: dict[str, str] | None = None,
    capture: bool = False,
) -> subprocess.CompletedProcess[str]:
    printable = " ".join(cmd)
    print(f"+ {printable}", flush=True)
    return subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


if __name__ == "__main__":
    raise SystemExit(main())
