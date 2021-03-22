class Person:

    def __init__(self,name,age,gender,height):
        self.name=name
        self.Age= age
        self.gender=gender
        self.height=height

    def eat(self):
        print("person is eating")

    def walk(self):
         print("person is walkinng")

    def getName(self):
        return self.name

    def getAge(self):
        return self.Age

person =Person("Akhil",22,"Male",168)

person.eat()
person.walk()
person.getAge()

person2 = Person("Pavithra",19,"Female",160)

print(person2.name)
print(person2.Age)

