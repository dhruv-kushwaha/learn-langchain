from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

# Only ide type checking will catch this error
# No runtime error will be raised (No validation)
new_person : Person = { "name": "Alice", "age": "30" }

print(new_person)