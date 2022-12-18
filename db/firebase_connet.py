import json
import pyrebase


class Firebase:
    def __init__(self, path):
        with open(path) as f:
            config = json.load(f)
        self.firebase = pyrebase.initialize_app(config)
