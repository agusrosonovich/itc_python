def remove_whitespace(string):
    cont_init = 0
    cont_fin = 0
    for i in string:
        cont_init += 1
        if i != " ":
            break
        if i == " ":
            cont_fin += 1
    return print(string[cont_init-1:(len(string)-cont_fin+1)])

# print("Contador de espacios " + str(cont_init-1))
# print("Contador de espacios al final " + str(cont_fin-1))


def remove_whitespace_revised(string):
    return print(string.strip(" "))


def main():
    remove_whitespace("     HOLA    ")
    remove_whitespace_revised("     HOLA    ")


if __name__ == '__main__':
    main()


