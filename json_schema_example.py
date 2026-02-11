from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name"]
}

data = {
    # "name": "Anna",
    "age": 30
}

print(validate(instance=data, schema=schema))