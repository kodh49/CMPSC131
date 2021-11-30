def readAll():
    logcalls = open("librarylog.txt", 'r', encoding='utf-8')
    line = logcalls.readline()
    processCmd(line.split('#'))
    while line != "":
        line = logcalls.readline()
        if line != "":
            processCmd(line.split('#'))
    logcalls.close()


def processCmd(code):
    command = []
    for i in range(len(code)):
        command.append(code[i].strip())
    # Call proper commands
    identifier_code = command[0]
    # [Borrow Notation]
    if identifier_code == "B":
        # B  # <day>#<Student Name>#<Book name>#<days borrowed for>
        day = command[1]
        student_name = command[2]
        book_name = command[3]
        days_borrowed = command[4]
        borrowBooks(day, student_name, book_name, days_borrowed)

    # [Return Notation]
    elif identifier_code == "R":
        # R  # <day>#<Student Name>#<Book name>
        day = command[1]
        student_name = command[2]
        book_name = command[3]
        returnBooks(day, student_name, book_name)

    # [Book Addition]
    elif identifier_code == "A":
        # A  # <day>#<Book name>
        day = command[1]
        book_name = command[2]
        addBooks(day, book_name)

    # [Fine Pay Notation]
    elif identifier_code == "P":
        # P  # <day>#<student name>#<amount>
        day = command[1]
        student_name = command[2]
        amount = command[3]
        payFines(day, student_name, amount)
    else:
        # Identifier code does not exist
        NameError


def borrowBooks(day, student_name, book_name, days_borrowed):
    borrower_info = [student_name, day, day+days_borrowed, None, 0]
    # Check if library has unborrowed copy
    print("Borrow Books", day, student_name, book_name, days_borrowed)
    pass


def returnBooks(day, student_name, book_name):
    # Update books dataframe to address the remaining books
    dataframe = Books.read()
    index = Books.searchBy("book_name", book_name)
    dataframe[index][1] += 1
    Books.update(dataframe)
    print("Return Books", day, student_name, book_name)
    pass


# Add book to the booklist.txt file
def addBooks(day, book_name):
    dataframe = Books.read()
    index = Books.searchBy("book_name", book_name)
    # If the book already exists
    if index != -1:
        # Increase the number of copies to the dataframe
        dataframe[index][1] += 1
    else:
        # Add new book information to the dataframe
        dataframe.append([book_name, 1, False])
    print("[200] day:", day, " Add Book:", book_name)


def payFines(day, student_name, amount):
    print("Pay Fine", day, student_name, amount)
    pass


readAll()
