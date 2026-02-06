import json

class FileStorage:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {"users": [], "orders": []}

    def save(self, users, orders):
        data = {"users": [u.to_dict() for u in users],
                "orders": [o.to_dict() for o in orders]}
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
