class Persona:
    name = " "
    age = 0
    height = 0
    weight = 0
    bmi = 0

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self. height = height
        self. weight = weight

    def calculate_bmi(self):
        bmi = int(self.weight)/int(pow(int(self.height), 2))
        return bmi


def main():
    p1 = Persona(input("name "), input("age "), input("height "), input("weight "))
    print(p1.name, p1.age, + p1.calculate_bmi())

    p2 = Persona(input("name "), input("age "), input("height "), input("weight "))
    print(p2.name, p2.age, + p2.calculate_bmi())





    #people = [Persona for i in range(2)]
    # for per in people:
    # Persona(name=input("name"), age= input("age"), height= input("height"), weight= input("weight"))
    # print(people)











if __name__ == '__main__':
        main()

