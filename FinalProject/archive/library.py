"""
The rules of the library are:

Restricted books can be borrowed for at most 7 days. Non restricted books can be borrowed for 28 days.

Books returned late are fined 5 a day for each day late for restricted books, 1 per day late for non restricted books.

Any library user can have at most 3 books borrowed at a time.

A library user can only borrow if they have no pending fines.

New books to the library can be added as per the log, these are in addition to the original list of books in booklist. (The added book can already exist in which case its an additional copy or can be a new book)

A book can only be borrowed if there is an unborrowed copy in the library.

===============================================


"""
# Import libraries from the same folder
import Books as Books
import Logs as Logs

fileloc = "cache.txt"

welcome_msg = "1) Can a student borrow a book on a particular day for a certain number of days?\n 2) What are the most borrowed/popular books in the library?\n 3) Which books have the highest borrow ratio?\n 4) Sorted lists of most borrowed books / books with highest usage ratio.\n 5) What are the pending fines at the end of the log/at a specific day in the log?\n Press any other key to exit\n"


def constructor():
    dataframe = Books.read()
    msg = ""
    for line in dataframe:
        linestr = ""
        for i in range(len(line)-1):
            linestr += (str(line[i])+"|/|")
        for j in range(len(line[-1])):
            linestr += str(line[-1][j])+"|"
        msg += linestr[:-1]+"\n"
    output = open(fileloc, 'w', encoding='utf-8')
    output.write(msg)
    output.close()


def readCache():
    cache = open(fileloc, 'r', encoding='utf-8')
    dataframe = [['book_name', 'number_of_copies', 'restrictions',
                  'borrowed_times', 'total_rent_time', 'borrower_infos']]
    line = cache.readline()


def processCacheLine(str, dest):
    str = str.split('|/|')
    pcs = []
    for i in range(len(str)):
        item = str[i]
        if i == 1:
            # Number of copies = int
            pcs.append(int(item))
        elif i == 2:
            # Restriction
            item = item.strip()
            if item == "FALSE":
                pcs.append(False)
            elif item == "TRUE":
                pcs.append(True)
            else:
                ValueError
        elif i >= 3 and i <= 4:
            # Borrowed times & Total rent time
            pcs.append(int(item))
        elif i == 5:
            # Borrower infomations in lists
            pass


while True:
    print("=== PRESS CORRESPONDING NUMBER KEY ===")
    menu_selection = int(input(welcome_msg))
    constructor()
    if menu_selection == 1:
        print("1")
    elif menu_selection == 2:
        print("2")
    elif menu_selection == 3:
        print("3")
    elif menu_selection == 4:
        print("4")
    elif menu_selection == 5:
        print("5")
    else:
        break


def checkBorrowAvailability(day, student_name, book_name, days_borrowing):
    #
    pass


def mostBorrowedBooks():
    pass


def findHighestBorrowRatio():
    pass


def sortBookLists():
    pass


def pendingFines(access_date):
    # End of the Log
    if access_date == -1:
        # Do something
        pass
    else:
        # Do something with the access date
        pass
