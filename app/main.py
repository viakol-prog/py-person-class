class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    temp = {}
    result = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        temp[person_data["name"]] = person
        result.append(person)

    for person_data, person in zip(people, result):
        if person_data.get("wife") is not None:
            person.wife = temp[person_data["wife"]]
        if person_data.get("husband") is not None:
            person.husband = temp[person_data["husband"]]
    return result
