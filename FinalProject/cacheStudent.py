# Create cache_student.txt from dataframe
def create(dataframe):
    outputStr = ""
    for line in dataframe:
        linestr = ""
        for i in range(len(line)):
            # Student Name
            if i == 0:
                linestr += line[i]+"#"
            # Book Name
            elif i == 1:
                linestr += line[i]+"#"
            # Borrow Start ...
            else:
                linestr += str(line[i])+"#"
        linestr += '\n'
        outputStr += linestr
    cache_book = open("cache_student.txt", 'w', encoding='utf-8')
    cache_book.write(outputStr)
    cache_book.close()


# Read from cache_student.txt and construct a dataframe
def read():
    # [Student Name, Book Name, Borrow Start Date, Borrow End Date, Return Date, Fine, Fine Date]
    dataframe = []
    cache_student = open("cache_student.txt", 'r', encoding='utf-8')
    line = cache_student.readline()
    getInfo(line, dataframe)
    while line != "":
        line = cache_student.readline()
        if line != "":
            getInfo(line, dataframe)
    cache_student.close()
    return dataframe


def getInfo(string, dest):
    pcs = []
    line = string.split('#')
    for i in range(len(line)):
        item = line[i].strip()
        # Student Name, Book Name
        if i >= 0 and i <= 1:
            pcs.append(item)
        # Borrow Start, End Date
        elif i == 2 or i == 3:
            pcs.append(int(item))
        # Return Date, Fine Date
        elif i == 4 or i == 6:
            if item == "None":
                pcs.append(None)
            else:
                pcs.append(int(item))
        # Fine
        elif i == 5:
            pcs.append(int(item))
    dest.append(pcs)
    return dest
