class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    temp = {}
    result = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        temp[name] = person
        result.append(person)

    for person_data, person in zip(people, result):
        wife_name = person_data.get("wife")
        if wife_name:
            spouse = temp.get(wife_name)
            if spouse is None:
                raise KeyError(f"Unknown wife name: {wife_name}")
            person.wife = spouse
        husband_name = person_data.get("husband")
        if husband_name:
            spouse = temp.get(husband_name)
            if spouse is None:
                raise KeyError(f"Unknown husband name: {husband_name}")
            person.husband = spouse

    return result
