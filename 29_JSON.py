import json

# Sample JSON data (as a Python dictionary)
data = {
    "name": "Arjun Verma",
    "age": 22,
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "is_student": True,
    "education": {
        "degree": "B.Tech",
        "college": "XYZ University",
        "year": 2025
    }
}

# Convert Python dictionary to JSON string
json_data = json.dumps(data, indent=4)
print("✅ JSON Output:\n")
print(json_data)

