# CSV to JSON Converter CLI

A simple command-line tool to convert CSV files to JSON format.

## Installation

```bash
pip install -e .
```

## Usage

```bash
csv2json input.csv output.json
```

Or output to stdout:

```bash
csv2json input.csv
```

### Options

- `--pretty`: Pretty-print the JSON output with indentation
- `--array`: Output as a JSON array (default)
- `--lines`: Output as JSON lines (one JSON object per line)

### Examples

```bash
# Convert CSV to pretty-printed JSON file
csv2json data.csv output.json --pretty

# Output to stdout
csv2json data.csv

# Convert to JSON lines format
csv2json data.csv output.jsonl --lines
```

## Features

- Supports standard CSV files
- Automatically detects CSV delimiters
- Handles headers
- Multiple output formats (array or JSON lines)
- Pretty-printing support
