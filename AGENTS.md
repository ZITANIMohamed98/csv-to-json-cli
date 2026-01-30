# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

A Python CLI tool that converts CSV files to JSON format. The tool supports automatic CSV dialect detection, multiple output formats (JSON array or JSON lines), and flexible output options (file or stdout).

## Development Setup

Install the package in editable mode for development:
```bash
pip install -e .
```

## Running the CLI

```bash
# Basic usage
csv2json input.csv output.json

# Pretty-print output
csv2json data.csv output.json --pretty

# JSON lines format (one JSON object per line)
csv2json data.csv output.jsonl --lines

# Output to stdout
csv2json data.csv
```

## Testing the Tool

To manually test the tool during development:
```bash
# Create a test CSV file
echo -e "name,age,city\nAlice,30,NYC\nBob,25,LA" > test.csv

# Run the converter
csv2json test.csv test.json --pretty
cat test.json
```

## Architecture

The codebase follows a simple modular structure:

- **`csv2json/cli.py`**: Entry point for the CLI. Handles argument parsing with `argparse`, validates input files, and orchestrates the conversion flow. Error handling and exit codes are managed here.

- **`csv2json/converter.py`**: Core conversion logic separated into two functions:
  - `csv_to_json()`: Reads CSV files using Python's `csv` module with automatic dialect detection via `csv.Sniffer`. Falls back to `csv.excel` dialect if detection fails. Handles both header and headerless CSVs (generating `column_N` keys for the latter).
  - `write_json()`: Handles output serialization in either JSON array or JSON lines format, with optional pretty-printing.

- **`setup.py`**: Defines the package metadata and console script entry point (`csv2json` command).

## Key Implementation Details

- **CSV Dialect Detection**: Uses `csv.Sniffer` to automatically detect delimiters and CSV dialect from the first 1024 bytes of the file.
- **Header Detection**: Automatically detects if the CSV has headers. If not, generates keys as `column_0`, `column_1`, etc.
- **Output Formats**: Supports both standard JSON array format and JSON lines (JSONL) format where each row is a separate JSON object on its own line.
- **No external dependencies**: Uses only Python standard library (`csv`, `json`, `argparse`, `pathlib`).

## Making Changes

When modifying the converter logic:
- The conversion and output logic are separated for easier testing and maintenance
- Input validation happens in `cli.py`, conversion logic in `converter.py`
- All file operations use `utf-8` encoding explicitly
- Type hints are used throughout for clarity

When adding new CLI options:
- Add the argument to the parser in `cli.py`
- Pass it through to the appropriate function in `converter.py`
- Update the README.md usage section
