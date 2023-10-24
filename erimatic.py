patient_list=[]

def add_person_to_px_list(people_list):
    name = input("Enter a name (or 'quit' to exit): ")
    if name == 'quit':
        return
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    person = {"name": name, "age": age, "city": city}
    people_list.append(person)
