import json
import os


def read_json(file_path):
    absolute_path = os.path.abspath(file_path)

    try:
        with open(absolute_path, "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {absolute_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {absolute_path}")