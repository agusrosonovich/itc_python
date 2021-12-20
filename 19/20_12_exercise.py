class LimitedList:
    def __init__(self, limit):
        self.limited_list = []
        self.limit = limit

    def __getitem__(self, key):
        return self.limited_list[key]

    def __setitem__(self, key, value):
        self.limited_list[key] = value

    def __str__(self):
        return str(self.limited_list)

    def __len__(self):
        return len(self.limited_list)

    def append(self, number):
        self.limited_list.append(number)
        if len(self.limited_list) > self.limit:
            self.limited_list.pop(0)


element=int(input("insert amount of numbers: "))
my_list = LimitedList(element)
print(my_list)

for i in range(my_list.limit):
    number = (input("Insert the " + str(i+1) + " number: "))
    my_list.append(number)
print(my_list)

my_list.append(4)
print(my_list)











