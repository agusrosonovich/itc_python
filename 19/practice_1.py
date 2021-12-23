equipment = ["hammer", "ruler", "torch",  "scissors", "screwdriver", "scissors",  "torch", "hammer", "hammer", "ruler"]
most_common_item = ""
highest_count = 0

for item in equipment:
    count_of_item = equipment.count(item)
    if count_of_item > highest_count:
        highest_count=count_of_item
        most_common_item = item

print("The item that appears the most in the  list is " + most_common_item)

salaries = [1200, 2500, 1800, 1600, 1800, 700, 3200, 1500, 1300, 1300,  850, 1900]
avg=0
sum=0
salaries_above_average=[]
avg_salaries_above_average=0
sum_of_salaries_above_average=0

for salary in salaries:
    sum += salary
avg=sum/len(salaries)

for salary in salaries:
    if salary>avg:
        salaries_above_average.append(salary)

for salary in salaries_above_average:
    sum_of_salaries_above_average+=salary
avg_salaries_above_average=sum_of_salaries_above_average/len(salaries_above_average)

print(avg_salaries_above_average)

a = 3
c = 0
b = a
c = a + b
b = 2
a = b
b = c
c = a
a = b + (c + a)
# a=10, b=6, c=2
print(a, b, c)






