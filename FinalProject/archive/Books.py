# Construct a dataframe by reading through the booklist
def read():
    # [Book Name, Total Copies, Restriction, Borrow Time]
    dataframe = []
    booklist = open("booklist.txt", 'r', encoding='utf-8')
    line = booklist.readline()
    addBookInfo(line, dataframe)
    while line != "":
        line = booklist.readline()
        if line != "":
            addBookInfo(line, dataframe)
    booklist.close()
    return dataframe


# Process each line of the list
def addBookInfo(str, dest):
    pcs = []
    str = str.split('#')
    for i in range(len(str)):
        item = str[i]
        pcs = []
        # Book Name
        if i == 0:
            pcs.append(item)
        # Total Number of Copies
        elif i == 1:
            pcs.append(int(item))
        # Book Restriction
        elif i == 2:
            item = item.strip()
            if item == "FALSE":
                pcs.insert(2, False)
            elif item == "TRUE":
                pcs.insert(2, True)
            else:
                ValueError
        else:
            pcs.append([])
    dest.append(pcs)
    return dest


# Search element by certain label name
def searchBy(col_name, value):
    dataframe = read()
    search_col = None
    index = -1
    for i in range(len(dataframe[0])):
        if col_name == dataframe[0][i]:
            search_col = i
    # Conduct searching by selected settings
    for j in range(len(dataframe)):
        if dataframe[j][search_col] == value:
            index = j
    return index


print(read())
