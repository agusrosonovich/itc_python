import re
print(dir(re))

result = re.findall(r"AV", "AV bla bla bla available.")
print(result)


sentence = 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections ' \
           '1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact ' \
           'original form, accompanied by English versions from the 1914 translation by H. Rackham. '

result2 = re.findall(r'f', sentence)

print(result2)
print(len(result2))

extra=input("What do you want to look for?: ")

result3 = re.findall(extra, sentence,re.I)
print(result3)

my_string='Send an email from this@email.com to test@user.com 34 times.'

result4 = re.findall(r'\S+@\S+', my_string)
print(result4)

my_string2 = "Waba luba dub dub"
result5 = re.search(r'dub', my_string2)
print(result5)

pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
user_input = input("Give me your email adress")
if re.search(pattern, user_input):
    print("valid")
else:
    print("invalid")

split_list=re.split(r"\s",my_string2)
print(split_list)
# replace all ocurrenes of 5 with five
ip = "They ate 5 apples and 5 oranges"
ip = re.sub(r'5','five',ip)
print(ip)


# replace all ocurrences of note irrespective of case with X
ip2 = "This note should not be NoTeD"
ip2=re.sub(r'note','X',ip2,2,re.I)
print(ip2)

# filter all elements that dont contain e:
items = ["goal","new", "user", 'sit',"eat","dinner"]
list = []
for i in items:
    if not re.search(r'e', i):
        list.append(i)
print(list)




