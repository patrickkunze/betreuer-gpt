#!/usr/bin/env python3
"""
generate_schema_index.py

Durchsucht das 'schemas/' Verzeichnis nach allen JSON-Dateien und erstellt
eine schemaIndex.json mit Name und roher GitHub-URL für jedes Schema.

Verwendung:
    python3 generate_schema_index.py \
        --schemas-dir schemas \
        --base-url https://raw.githubusercontent.com/politpatrick/betreuer-gpt/main/schemas
"""

import os
import json
import argparse

def create_schema_index(schemas_dir, base_url):
    """
    Scans the specified schemas directory for .json files (including subdirectories),
    constructs a list of schemas with their name (filename without extension) and
    corresponding raw GitHub URL, and writes the result to schemaIndex.json.
    """
    entries = []
    for root, _, files in os.walk(schemas_dir):
        for file in files:
            if file.endswith(".json"):
                # Skip existing schemaIndex.json to avoid recursion
                if file == "schemaIndex.json":
                    continue
                # Generate relative path and URL
                rel_path = os.path.relpath(os.path.join(root, file), schemas_dir)
                url = f"{base_url}/{rel_path.replace(os.sep, '/')}"
                name = os.path.splitext(file)[0]
                entries.append({"name": name, "url": url})

    index = {"schemas": entries}

    # Write the index file
    output_path = os.path.join(schemas_dir, "schemaIndex.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"Created schemaIndex.json at '{output_path}'")

def main():
    parser = argparse.ArgumentParser(
        description="Generate a schemaIndex.json for all JSON schemas in a directory."
    )
    parser.add_argument(
        "--schemas-dir",
        default="schemas",
        help="Pfad zum Verzeichnis mit den JSON-Schemas (Standard: schemas)"
    )
    parser.add_argument(
        "--base-url",
        default="https://raw.githubusercontent.com/politpatrick/betreuer-gpt/main/schemas",
        help="Basis-URL für die rohen GitHub-Dateien"
    )

    args = parser.parse_args()
    create_schema_index(args.schemas_dir, args.base_url)

if __name__ == "__main__":
    main()
