class Library:
    def __init__(self, list_of_books, name):
        self.booksList=list_of_books
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print("we have the following books in our library:{self.name}")
        for book in self.booksList:
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.booksList:
            print("sorry, we dont have that book")
        elif book in self.lendDict:
            print("the book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book]=user
            print(
                "lender-book database has been updated, you can take the book now"
            )
    def addBook(self, book):
        self.booksList.append(book)
        print("{book} has been added to the book list")
    
    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned")
        else:
            print("that book wasn't borrowd from us.")

        if __name__=='__main__':
            books = Library([
            'harry potter','king of greed','the chronicles of astronautica','the hunger games','dork diaries'
         ],"Lets Upskill")
        user_name=input("Welcome to our library, please enter your name:")

        while True:
            print(
                f"\nHello {user_name}, welcome to the {books.name} library. please choose an option:"
            )
            print(
                "1. display books\n2. Lend a book\n3.Add a book\n4.return a book\n5.quit"
            )
            user_choice=input("enter your choice to continue:")
            
            if user_choice not in ['1', '2', '3', '4', '5']:
                print("please enter a valid option")
                continue
            if user_choice =='1':
                books.displayBooks()
            elif user_choice == '2':
                book = input("Enter the name of the book you want to lend:")
                books.lendBook(user_name, book)
            elif user_choice == '3':
                book = input("Enter the name of the book you want to add:")
                books.addBook(book)
            elif user_choice == '4':
                book = input("Enter the name of the book you want to return:")
            elif user_choice == '5':
                print("thankyou for using the library, {user_name}. Goodbye!")
                break