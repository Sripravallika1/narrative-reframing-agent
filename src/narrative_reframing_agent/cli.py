"""CLI for narrative-reframing-agent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import reframe_narrative


def build_parser() -> argparse.ArgumentParser:
    """Build parser for CLI arguments."""
    parser = argparse.ArgumentParser(description="Generate structured narrative reframing output.")
    parser.add_argument("--input", type=Path, required=True, help="Path to narrative text file.")
    parser.add_argument("--output", type=Path, help="Optional output JSON path.")
    return parser


def main() -> None:
    """Run command line app."""
    args = build_parser().parse_args()
    text = args.input.read_text(encoding="utf-8")
    result = reframe_narrative(text).to_dict()
    content = json.dumps(result, indent=2)

    if args.output:
        args.output.write_text(content + "\n", encoding="utf-8")
    else:
        print(content)


if __name__ == "__main__":
    main()
