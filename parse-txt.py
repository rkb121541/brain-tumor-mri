import os

def main():
    read_file = open(r"C:\Users\rkbid\Documents\braintumormri\requirements.txt")
    list_of_lines = []
    for line in read_file:
        list_of_lines += [line]
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list_of_lines[i].rsplit('=')[0]
        list_of_lines[i] += '\n'
    print(list_of_lines)
    read_file.close()

    with open("installations.txt", "w") as write_file:
        write_file.writelines(list_of_lines)
        write_file.close()



if __name__ == "__main__":
    main()