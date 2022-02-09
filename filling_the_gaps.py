def writerfunc(string_list):
    index_list = []
    val = 0
    if string_list[0] == "_":
        string_list[0] = 0
    for i, j in enumerate(string_list):
        if j != "_":
            index_list.append(i)
    for n in range(0, len(index_list)-1):
        if index_list[n+1] - index_list[n] > 1:
                value = (int(string_list[index_list[n+1]])+int(string_list[index_list[n]]))/((index_list[n+1]-index_list[n])+1)
                for k in range(index_list[n], (index_list[n+1])+1):
                    string_list[k] = value
        else:
            continue
    if len(string_list) != index_list[-1]:
        value1 = int(string_list[index_list[-1]])/(len(string_list)-index_list[-1])
        for k in range(index_list[-1], len(string_list)):
            string_list[k] = value1
    return string_list

if __name__ == "__main__":
    string = input("Space Separated Input: ")
    input_list = string.split(" ")
    output = writerfunc(input_list)
    print()
    for out in output:
        print(out, end=" ")
    print()
