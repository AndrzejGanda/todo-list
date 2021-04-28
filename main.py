import errno
import random

class Todo:
    def addNote(self):
        
        with open("todoList.txt", "a") as f:
            f.write(input("create a new note: ")+"\n")
        f.close()
        
class Welcome():
    def hello(self):
        print("Welcome to the todo list\n"
        +"Show all notes: select 1\n"
        +"Add new note: select 2\n"
        +"Delete note with particural number: select 3\n"
        +"Draw a note: select 4\n")

class ShowAllNotes():
    def doList(self):
    
        index = 1
        with open("todoList.txt", "r") as f:
            print("Your notes:")
            for line in f:
                line = line.strip()
                print(str(index) + ") " +line)
                index = index + 1 
        
class DeleteNote():
    def deteleCreatedNote(self):
        input_del = int(input("Provide numer of the note to be deleted: "))
        with open("todoList.txt", "r") as f:
            lines = f.readlines()
            f.close()
            del lines[input_del-1]
        with open("todoList.txt", "w+") as f:
            for line in lines:
                f.write(line)
            f.close()

class TakeRandomNote():
    def drawNote(self):
        with open("todoList.txt", "r") as f:
            allText = f.read()
            words = list(map(str, allText.split()))
            print("The drawn note is: " + random.choice(words))
            f.close()
try:
    obj = Welcome()
    obj.hello()
    #obj2 = Todo()
    #obj2.addNote()
    obj3 = ShowAllNotes()
    obj3.doList()
    #obj4 = DeleteNote()
    #obj4.deteleCreatedNote()
    obj5 = TakeRandomNote()
    obj5.drawNote()
except IndexError:
    print("There is no note with such number")
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
