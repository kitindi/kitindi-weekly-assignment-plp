"""
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
Activity 2: Polymorphism Challenge! 🎭

"""

# Activity 1

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def loan(self):
        print(f"The book title: {self.title}")
        return ""
    

fiction_book = Book("Now next year", "Kitindi")
print(fiction_book.loan())


# Activity 2: Polymorphism Challenge! 🎭
"""
Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""

class School:
    def name(self):
        pass

class Teacher(School):
    def name(self):
        return "I work here"
    
        