import os
import json

settings = {}


def load_settings(file_name, is_local=False):

    directory = os.path.dirname(os.path.abspath(__file__)).replace('util', '')
    with open("%s%s" % (directory, file_name), "r") as f:
        _settings = json.load(f)

    if is_local:
        return _settings

    global settings
    if not settings.has_key(file_name):
            settings[file_name] = _settings
    return settings[file_name]
