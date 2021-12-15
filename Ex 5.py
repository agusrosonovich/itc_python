cont=1
for i in range(10):

    if i < 6:
        print("*" * i)
    else:
        print("*"*(i - (2*cont)))
        cont += 1





