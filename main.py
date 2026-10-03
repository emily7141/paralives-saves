"""Paralives Saves — A local helper for Paralives household folders, lot files, and custom content lists."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='paralives_saves',
        description='A local helper for Paralives household folders, lot files, and custom content lists.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Paralives Saves')
    print('Keep families on disk before an Early Access update.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
