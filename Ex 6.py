
def build_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        a = []
        for j in range(cols):
            a.append(i*j)
        matrix.append(a)

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=" ")
        print()


def main():
    matrix = []
    rows = int(input("insert a number for rows: "))
    cols = int(input("insert a number for cols: "))
    build_matrix(rows, cols)


if __name__ == '__main__':
  main()







