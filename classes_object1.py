class car:
    def __init__(self, speed , color):
        print(speed)
        print(color)

ford = car(300 , 'red')
honda = car(400 ,'black')
suzuki = car(300 , 'blue')

#an other method to seter and geter
class name:
    def __init__(self, name , color):
        self.name = name
        self.color = color
    def set_name(self, value):
        self.name = value
    def get_name(self):
        return self.name
iqra = name('iqra' , 'white')
Qurat = name('qurat', 'white')
print(iqra.name)
print(Qurat.color)
#Write a Python program to get the class name of an instance in Python.
import itertools
x = itertools.cycle('ABCD')
print(type(x).__name__)
#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
class Circle():
    def __init__(self, r):
        self.radius = r
    def area_of_circle(self):
        return self.radius**2*3.14
    def perimete_of_circle(self):
        return 2*self.radius*3.14
Newcircle = Circle(8)
print(Newcircle.area_of_circle())
print(Newcircle.perimete_of_circle())
#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangular():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def area_of_rectangular(self):
        return self.length * self.width
new_rectngular = Rectangular(10 ,20)
print(new_rectngular.area_of_rectangular())
#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.s
class IOS():
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter any string")
    def print_string(self):
        print(self.str1.upper())
str1 = IOS()
str1.get_string()
str1.print_string()
#count letter in dic
def count_letter(text):
    result = {}
    for letter in text:
        if letter  not in result:
            result[letter] = 0
        result[letter] += 1
    return result
count_letter("aaaaaaa")
#Write a Python program to reverse a string word by word.
class py_sol():
    def reverse_word(self s):
    return ''.join(reversed(s.split()))
print(py_solution().reverse_words('hello .py'))
