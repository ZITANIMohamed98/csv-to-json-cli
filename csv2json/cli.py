"""Command-line interface for CSV to JSON converter."""

import argparse
import sys
from pathlib import Path
from .converter import csv_to_json, write_json


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Convert CSV files to JSON format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  csv2json input.csv output.json
  csv2json input.csv output.json --pretty
  csv2json input.csv --lines
  csv2json input.csv
        """
    )
    
    parser.add_argument(
        "input",
        help="Path to the input CSV file"
    )
    
    parser.add_argument(
        "output",
        nargs="?",
        default=None,
        help="Path to the output JSON file (optional, defaults to stdout)"
    )
    
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the JSON output with indentation"
    )
    
    parser.add_argument(
        "--lines",
        action="store_true",
        help="Output as JSON lines (one JSON object per line)"
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file '{args.input}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not input_path.is_file():
        print(f"Error: '{args.input}' is not a file", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Convert CSV to JSON
        data = csv_to_json(args.input)
        
        # Write output
        write_json(data, args.output, pretty=args.pretty, lines=args.lines)
        
    except FileNotFoundError:
        print(f"Error: Could not read file '{args.input}'", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied reading '{args.input}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
