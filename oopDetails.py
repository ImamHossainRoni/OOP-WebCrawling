class Person:
    def index():
        person = "{name}'s age is {age}"
        person=person.format(name ='Roni',age =23)
        print(person)
obj =Person
obj.index()