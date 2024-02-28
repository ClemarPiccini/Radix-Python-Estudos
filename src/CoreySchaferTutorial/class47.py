# JSON Data
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data["name"])


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_to_dict(person):
    return person.__dict__

person = Person("Alice", 25)
json_string = json.dumps(person, default=person_to_dict)
print(json_string)

def dict_to_person(d):
    return Person(d["name"], d["age"])

json_string = '{"name": "Bob", "age": 30}'
person = json.loads(json_string, object_hook=dict_to_person)
print(person.name, person.age)


data = {
    "name": "Jane",
    "age": 35,
    "city": "Los Angeles"
}

json_string = json.dumps(data, indent=4)
print(json_string)
