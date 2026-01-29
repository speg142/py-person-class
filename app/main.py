class Person:
    people = {}

    def __init__(self, name: str, age: int) -> str:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])
    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]  # Находим объект
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_obj.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person_obj.husband = Person.people[person_dict["husband"]]
    return [Person.people[person_dict["name"]] for person_dict in people]
