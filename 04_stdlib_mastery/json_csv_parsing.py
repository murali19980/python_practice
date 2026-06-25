"""
Practice: JSON & CSV parsing
"""
import json
import os

def write_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, indent=2)

def read_json(file):
    with open(file, 'r') as f:
        return json.load(f)

def parse_csv_string(csv_str):
    lines = csv_str.strip().split('\n')
    headers = lines[0].split(',')
    result = []
    for line in lines[1:]:
        values = line.split(',')
        result.append(dict(zip(headers, values)))
    return result

if __name__ == "__main__":
    data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
    filename = "test.json"
    write_json(data, filename)
    print("Read JSON:", read_json(filename))
    
    # Cleanup json file
    if os.path.exists(filename):
        os.remove(filename)

    csv_str = "name,age\nAlice,30\nBob,25"
    print("Parsed CSV:", parse_csv_string(csv_str))
