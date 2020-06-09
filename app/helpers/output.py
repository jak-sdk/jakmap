from flask import current_app
import json

def jdump(array):
    indent = current_app.config["JSON_INDENT"]
    return json.dumps(array, indent=indent)
