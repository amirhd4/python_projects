import json
from pathlib import Path


class ContactManager:
    def __init__(self, path=None):
        self.contact_list = []

        if path is not None:
            print("Loading previous contacts...")
            with open(path, "r") as f:
                data = f.read()
                self.contact_list = json.loads(data)
            print(f"Loaded...")

    def add(self, name, number):
        self.contact_list.append({
            "name": name,
            "number": number
        })

    def search(self, name):
        result =[]
        for item in self.contact_list:
            if name.lower() in item["name"].lower():
                result.append(item)

        print(result)

    def backup(self):
        mode = "r+" if Path("contact_list.json").is_file() else "w"
        with open("./contact_list.json", mode) as f:
            if mode == "r+":
                js_file = json.load(f)
                for contact in self.contact_list:
                    js_file.append(contact)
                f.seek(0)
                f.flush()
                f.write(json.dumps(js_file, indent=2))
            else:
                f.write(json.dumps(self.contact_list, indent=2))

    def print(self):
        print(f"Your contacts are: {self.contact_list}")

my_contacts = ContactManager(path="./contact_list.json")
my_contacts.print()
my_contacts.search("Behnam")
# my_contacts.add("Amir", "09352342321")
# my_contacts.add("mir", "09533421294")
# my_contacts.add("Sina", "09533421295")
#
# my_contacts.backup()