# Import Modules
import bookList as bookList
import cacheStudent as cacheStudent
import cacheBook as cacheBook
import libraryLog as libLog

welcome_msg = "1) Can a student borrow a book on a particular day for a certain number of days?\n 2) What are the most borrowed/popular books in the library?\n 3) Which books have the highest borrow ratio?\n 4) Sorted lists of most borrowed books / books with highest usage ratio.\n 5) What are the pending fines at the end of the log/at a specific day in the log?\n Press any other key to exit\n"

# Read book list from 'booklist.txt'
booklist = bookList.read()
# Update booklist by using 'librarylog.txt'
libLog.update(booklist)
# Get cache_book and cache_student database
Book = cacheBook.read()
Student = cacheStudent.read()

while True:
    mode_select = int(input(welcome_msg))
    # Book 이랑 Student 변수가 텍스트 파일에서 로그 읽어서 가져온 데이터니까 이걸 이용해서 각자 기능을 구현하시면 됩니다.
    if mode_select == 1:
        # Borrow Availability (replace 'pass' with corresponding functions)
        pass
    elif mode_select == 2:
        # Popular books (replace 'pass' with corresponding functions)
        pass
    elif mode_select == 3:
        # Borrow Ratio (replace 'pass' with corresponding functions)
        pass
    elif mode_select == 4:
        # Sorted List of books (replace 'pass' with corresponding functions)
        pass
    elif mode_select == 5:
        # Pending Fines (replace 'pass' with corresponding functions)
        pass
    else:
        break
