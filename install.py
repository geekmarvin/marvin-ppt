"""Install the two PPT skills from this repository into Codex."""

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import sys
from tempfile import TemporaryDirectory
from zipfile import BadZipFile, ZipFile


ROOT = Path(__file__).resolve().parent
ARCHIVE_NAME = "ppt-master-skill-v6.9.0.zip"
ARCHIVE_SHA256 = "5ac7bf511b1bbaf3809b9fb3d8465918f79ca39b5451203c9eb9e08763acd873"
OFFICIAL_PATH = "ppt-master/skills/ppt-master/"
SKILL_NAMES = ("ppt-master", "marvin-ppt")


def prepare_ppt_master(staging):
    archive = ROOT / "vendor" / ARCHIVE_NAME
    if not archive.is_file():
        parts = sorted((ROOT / "vendor").glob(f"{ARCHIVE_NAME}.part-*"))
        if not parts:
            raise ValueError("Missing official archive. Download the entire repository ZIP.")
        archive = staging / ARCHIVE_NAME
        with archive.open("wb") as output:
            for part in parts:
                with part.open("rb") as source:
                    shutil.copyfileobj(source, output)

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    if digest != ARCHIVE_SHA256:
        raise ValueError("The PPT Master archive failed its checksum. Download the repository again.")

    with ZipFile(archive) as bundle:
        members = [entry for entry in bundle.infolist() if entry.filename.startswith(OFFICIAL_PATH)]
        bundle.extractall(staging, members=members)

    skill = staging / OFFICIAL_PATH
    for required in ("SKILL.md", "LICENSE", "requirements.txt", "scripts/attribution_guard.py"):
        if not (skill / required).is_file():
            raise ValueError(f"Missing expected PPT Master file: {required}")
    return skill


def install(destination):
    destination.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(prefix='.marvin-ppt-', dir=destination) as directory:
        staging = Path(directory)
        pending = {}
        for name in SKILL_NAMES:
            target = destination / name
            if target.exists() or target.is_symlink():
                print(f"Kept existing skill: {target}")
            elif name == 'ppt-master':
                pending[name] = prepare_ppt_master(staging)
            else:
                source = ROOT / "skills" / name
                if not (source / "SKILL.md").is_file():
                    raise ValueError("Missing Marvin PPT skill. Download the entire repository ZIP.")
                pending[name] = staging / name
                shutil.copytree(source, pending[name])

        for name, source in pending.items():
            target = destination / name
            if target.exists() or target.is_symlink():
                print(f"Kept existing skill: {target}")
                continue
            source.rename(target)
            print(f"Installed {name}: {target}")

    requirements = destination / "ppt-master" / "requirements.txt"
    if requirements.is_file():
        print(f"PPT Master Python requirements: {requirements}")


def main():
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=codex_home / "skills", help="Codex skills directory")
    args = parser.parse_args()
    try:
        install(args.dest.expanduser().resolve())
    except (OSError, ValueError, BadZipFile) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
