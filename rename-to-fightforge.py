#!/usr/bin/env python3
"""
FightForge Rename Script
Replaces all Paperclip → FightForge branding in the UI source files.
Run from the root of your fightforge repo AFTER cloning.

Usage: python3 rename-to-fightforge.py

Safe to run multiple times — skips binary files and
files already containing FightForge branding.
"""

import os
import sys

# ── Replacements (order matters — most specific first) ────────────────────────
REPLACEMENTS = [
    # Product name variants
    ("Paperclip AI",           "FightForge AI"),
    ("paperclipai",            "fightforgeai"),
    ("paperclip-ai",           "fightforge-ai"),
    ("Paperclip",              "FightForge"),
    ("paperclip",              "fightforge"),

    # Taglines
    ("Open-source orchestration for zero-human companies",
     "Open-source AI operating system for combat sports businesses"),
    ("Manage a team of AI agents to run your business",
     "Run your martial arts academy with a 10-agent AI workforce"),

    # CLI branding
    ("npx paperclipai",        "npx fightforgeai"),
    ("pnpm paperclipai",       "pnpm fightforgeai"),
    ("paperclipai",            "fightforgeai"),
    ("PAPERCLIP_HOME",         "FIGHTFORGE_HOME"),
    ("PAPERCLIP_INSTANCE_ID",  "FIGHTFORGE_INSTANCE_ID"),
    ("PAPERCLIP_IN_WORKTREE",  "FIGHTFORGE_IN_WORKTREE"),
    ("PAPERCLIP_WORKTREE",     "FIGHTFORGE_WORKTREE"),

    # GitHub org (keep upstream attribution, update fork refs)
    ("KoshoDJ/paperclip",      "KoshoDJ/fightforge"),
]

# ── Files and directories to skip ─────────────────────────────────────────────
SKIP_DIRS = {
    "node_modules", ".git", "dist", ".turbo", ".next",
    "__pycache__", ".cache", "coverage",
    # Don't touch these — they're intentional upstream references
    "CHANGELOG.md",
}

SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
    ".woff", ".woff2", ".ttf", ".eot",
    ".zip", ".tar", ".gz",
    ".db", ".sqlite",
    ".lock",  # pnpm-lock.yaml managed by CI
}

# ── Target directories (only process these) ───────────────────────────────────
TARGET_DIRS = [
    "apps",
    "packages",
    "cli",
    "doc",
    "agents",
    "claude_skills",
    "company-templates",
    "integrations",
]

TARGET_ROOT_FILES = [
    "README.md",
    "package.json",
    ".env.example",
    "docker-compose.yml",
    "docker-compose.quickstart.yml",
]

# ── Main ──────────────────────────────────────────────────────────────────────
def should_skip(path):
    for skip in SKIP_DIRS:
        if skip in path.split(os.sep):
            return True
    _, ext = os.path.splitext(path)
    return ext.lower() in SKIP_EXTENSIONS

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return False

    original = content
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)

    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    root = os.getcwd()
    changed = []
    skipped = []

    # Process root-level target files
    for filename in TARGET_ROOT_FILES:
        filepath = os.path.join(root, filename)
        if os.path.isfile(filepath):
            if process_file(filepath):
                changed.append(filepath)

    # Process target directories recursively
    for target_dir in TARGET_DIRS:
        dirpath = os.path.join(root, target_dir)
        if not os.path.isdir(dirpath):
            continue
        for dirroot, dirs, files in os.walk(dirpath):
            # Remove skip dirs from traversal
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for filename in files:
                filepath = os.path.join(dirroot, filename)
                if should_skip(filepath):
                    skipped.append(filepath)
                    continue
                if process_file(filepath):
                    changed.append(filepath)

    # Report
    print(f"\n✅ FightForge rename complete")
    print(f"   Files updated:  {len(changed)}")
    print(f"   Files skipped:  {len(skipped)}")

    if changed:
        print(f"\nUpdated files:")
        for f in changed:
            print(f"  ✓ {os.path.relpath(f, root)}")

    print(f"""
Next steps:
  1. Review changes with: git diff
  2. Test the build:      pnpm install && pnpm dev
  3. Commit:             git add . && git commit -m "rebrand: Paperclip → FightForge"
  4. Push:               git push origin master
""")

if __name__ == "__main__":
    main()
