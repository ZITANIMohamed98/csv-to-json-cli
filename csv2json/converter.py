"""Core CSV to JSON conversion logic."""

import csv
import json
from typing import List, Dict, Any


def csv_to_json(csv_file_path: str, output_format: str = "array") -> List[Dict[str, Any]]:
    """
    Convert a CSV file to JSON format.
    
    Args:
        csv_file_path: Path to the CSV file
        output_format: Format of output ('array' or 'lines')
    
    Returns:
        List of dictionaries representing the CSV rows
    """
    data = []
    
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        # Use Sniffer to detect the CSV dialect
        sample = csv_file.read(1024)
        csv_file.seek(0)
        
        try:
            dialect = csv.Sniffer().sniff(sample)
            has_header = csv.Sniffer().has_header(sample)
        except csv.Error:
            # Fall back to default dialect
            dialect = csv.excel
            has_header = True
        
        csv_file.seek(0)
        reader = csv.DictReader(csv_file, dialect=dialect) if has_header else csv.reader(csv_file, dialect=dialect)
        
        if has_header:
            for row in reader:
                data.append(row)
        else:
            # If no header, use column indices as keys
            for row in reader:
                data.append({f"column_{i}": value for i, value in enumerate(row)})
    
    return data


def write_json(data: List[Dict[str, Any]], output_path: str = None, pretty: bool = False, lines: bool = False):
    """
    Write JSON data to a file or stdout.
    
    Args:
        data: List of dictionaries to write
        output_path: Path to output file (None for stdout)
        pretty: Whether to pretty-print the JSON
        lines: Whether to output as JSON lines format
    """
    indent = 2 if pretty else None
    
    if lines:
        # JSON lines format - one JSON object per line
        output = '\n'.join(json.dumps(row, indent=None) for row in data)
    else:
        # Standard JSON array format
        output = json.dumps(data, indent=indent)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
            if lines or not pretty:
                f.write('\n')
    else:
        print(output)
