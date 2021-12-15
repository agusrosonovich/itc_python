from random import randint


def random_number():
    return randint(0, 100)


print("Useless processes should be removed")
idle_process_ids = [17, 18, 32, 6, 41, 8, 23,
                    88, 91]
while len(idle_process_ids) >= 6:
    test = random_number()
    if test in idle_process_ids:
        index = idle_process_ids.index(test)
        idle_process_ids.pop(index)
print(idle_process_ids)

turtle_status = ["sick", "healthy", "healthy", "healthy,"
                 "sick", "sick", "healthy", "sick", "healthy", "healthy ,"
                 "healthy", "healthy", "healthy", "sick "]
sick_counter = 0
healthy_counter = 0
for i in range(len(turtle_status)):
    if turtle_status[i] == "sick":
        sick_counter += 1
    else:
        healthy_counter += 1
if sick_counter > healthy_counter:
    print("We have a shell of a problem")
else:
    print("Let's shell-ebrate")