#
//  generate_schema_index.py
//  
//
//  Created by Patrick Kunze on 14.05.25.
//


import os
import json

def create_schema_index(schemas_dir="schemas", base_url="https://raw.githubusercontent.com/politpatrick/betreuer-gpt/main/schemas"):
    """
    Scans the specified schemas directory for .json files (including subdirectories),
    constructs a list of schemas with their name (filename without extension) and
    corresponding raw GitHub URL, and writes the result to schemaIndex.json.

    :param schemas_dir: Local path to the 'schemas' directory.
    :param base_url: Base URL for raw GitHub access to the 'schemas' directory.
    """
    entries = []
    for root, _, files in os.walk(schemas_dir):
        for file in files:
            if file.endswith(".json"):
                # Generate relative path and URL
                rel_path = os.path.relpath(os.path.join(root, file), schemas_dir)
                url = f"{base_url}/{rel_path.replace(os.sep, '/')}"
                name = os.path.splitext(file)[0]
                entries.append({"name": name, "url": url})

    index = {"schemas": entries}

    # Write the index file
    output_path = os.path.join(schemas_dir, "schemaIndex.json")
    os.makedirs(schemas_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"Created schemaIndex.json at {output_path}")

# Example usage
# create_schema_index()