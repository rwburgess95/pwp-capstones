class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return print("User's email has been updated to " + self.email)

    #User methods
    
    def __repr__(self):
        return "User: " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books)) 
    # Need to figure out how to return number of books read for this guy

    def __eq__(self, other_user):

        try:
            if (self.name == other_user.name) & (self.email == other_user.email):
                return print("The Users are the same")
            else:
                return print("The Users are not the same")
        except AttributeError:
            pass
    def read_book(self, book, rating=None):
        self.books[book] = rating
        
    def get_average_rating(self):
        Average = 0
        for book in self.books:
            if self.books.get(book) != None:
                Average += self.books.get(book)
                
        if len(self.books) == 0:
            return 0
        else:
            return (Average/len(self.books))
    
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return print("The isbn has been updated to " + str(self.isbn))
    
    #Book Methods
    
    def add_rating(self, new_rating):
        if new_rating == None:
            return print("Invalid Rating")
        if (new_rating >= 0 & new_rating <= 4):
            self.ratings.append(new_rating)
        else:
            return print("Invalid Rating")
    
    def __eq__(self, other_book):
        if (self.title == other_book.title) & (self.isbn == other_book.isbn):
            return print("The books are the same")
        else:
            return print("The books are not the same")
    
    def get_average_rating(self):
        Average = 0
        for rating in self.ratings:
            Average += rating
        return (Average/len(self.ratings))
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def __repr__(self):
        rString = "{title} {isbn}"
        return rString.format(title = self.title, isbn = self.isbn)
    
class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
        
    def __repr__(self):
        return f'{self.title} by {self.author}'
    
class NonFiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return str(self.title) + ", " + str(self.level) + " manual on " + str(self.subject)
    
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    def create_book(self, title, isbn):
        
        book = Book(title, isbn)
        return book     

    def create_novel(self, title, isbn, author):
        book = Fiction(title, isbn, author)
        return book
    
    def create_non_fiction(self, title, isbn, subject, level):
        book = NonFiction(title, isbn, subject, level)
        return book
    
    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        
    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if (user_books != None):
            for book in user_books:
                self.add_book_to_user(book, email, None)
                
    #TomeRater methods                        
    def print_catalog(self):
        for book in self.books:
            print(book)
            
    def print_users(self):
        for user in self.users:
            print(self.users.get(user))
    
    def most_read_book(self):
        most_read_book = None
        NumReads = 0
        for book in self.books:
            if (self.books.get(book) > NumReads):
                NumReads = self.books.get(book)
                most_read_book = book
        return most_read_book
    
    def highest_rated_book(self):
        highest_average_rating = 0
        highest_rated_book = None
        for book in self.books:
            if (book.get_average_rating() > highest_average_rating):
                highest_average_rating = book.get_average_rating()
                highest_rated_book = book
        return highest_rated_book
    
    def most_positive_user(self):
        highest_average_rating = 0
        most_positive_user = None
        for user in self.users.values():
            average_rating = user.get_average_rating()
            if (average_rating > highest_average_rating):
                highest_average_rating = average_rating
                most_positive_user = user
        return most_positive_user
            
    #dunder methods for TomeRater
    #repr prints how many users and the number of unique they've read
    def __repr__(self):
        return "There are " + str(len(self.users)) + " users who have read " + str(len(self.books)) + " unique books"
    
    def __eq__(self, other_tome_rater):
        if (self.users == other_tome_rater.users) & (self.books == other_tome_rater.books):
            print("These two have the same users and books!")
        else:
            print("These two do not have the same users and books!")
#Code I used to test my functions as I programmed
#User class test code
#BigBandito = User("BigBandito", "bb@gmail.com")
#BigBandito.change_email("BB@gmail.com")
#print(BigBandito)
#BBI = User("BigBandito", "bb@gmail.com")
#BigBandito == BBI
#BigBandito.read_book("hurf", 3)   
#BigBandito.read_book("Durf", 2)   
#print(BigBandito.get_average_rating())   

#Book class test code
#WinBigly = Book("WinBigly", 419)
#WinBigly.get_title()
#WinBigly.get_isbn()
#WinBigly.set_isbn(68)
#WinBigly.add_rating(3)
#WinBigly.add_rating(2)
#BigWinly = Book("WinBigly", 70)
#WinBigly == BigWinly
#print(WinBigly.get_average_rating())

#Fiction subclass test code
#MobyDick = Fiction("Moby Dick", 1, "WhatsHisFace")
#print(MobyDick)
#MobyDick.get_author()
        
#Nonfiction subclass test code
#TheArtOfTheDeal = NonFiction("The Art of the Deal", 42069, "Negotiation & Persuasion", "a very high level, believe me folks")
#TheArtOfTheDeal.get_level()
#print(TheArtOfTheDeal)
        
#TomeRating class test code
#Test = TomeRater()
#Test2 = TomeRater()
#print(Test)
#Test == Test2
#Test.create_book("Butts", 2)
#Test.create_novel("BigButts", 4, "Me")
#Test.create_non_fiction("Little brains", 3, "Baskets", "novice")
#Test.add_user("Ray", "me@g.com", ["Oh man what", "uhhh"])
#Test.add_user("Barry", "him@g.com", [])
