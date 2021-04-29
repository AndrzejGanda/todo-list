import errno
import random
from todolog import AddLog

class Todo:
    def addNote(self):
        
        with open("todoList.txt", "a") as f:
            f.write(input("create a new note: ")+"\n")
        f.close()
        AddLog.addNoteLog(lognote=1)

    def hello(self):
        print("Welcome to the todo list\n"
        +"Show all notes: select 1\n"
        +"Add new note: select 2\n"
        +"Delete note with particural number: select 3\n"
        +"Draw a note: select 4\n")


    def doList(self):
    
        index = 1
        with open("todoList.txt", "r") as f:
            print("Your notes:")
            for line in f:
                line = line.strip()
                print(str(index) + ") " +line)
                index = index + 1 
        AddLog.addNoteLog(lognote=0)
        

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
        AddLog.addNoteLog(lognote=2)

    def drawNote(self):
        with open("todoList.txt", "r") as f:
            #allText = f.read()
            #words = list(map(str, allText.split()))
            #drawline = random.choice(words)
            allText = f.readlines()
            drawline = random.choice(allText)
            print("The drawn note is: " + drawline)
        AddLog.addNoteLog(lognote=3)
        
        input_answer = input("Delete the drawn note?(yes or no): ")
        if (str.upper(input_answer) == "YES"):
            
            with open("todoList.txt", "r") as f:
                lines = f.readlines()
            with open("todoList.txt", "w") as f:
                for line in lines:
                    
                    if line != drawline:
                        f.write(line)
            AddLog.addNoteLog(lognote=2)
        elif (str.upper(input_answer) == "NO"):
            pass
        else:
            print("wrong answer, next time enter 'yes' or 'no'")
try:
    
    obj = Todo()
    obj.hello()
    obj.addNote()  
    obj.doList()  
    #obj.deteleCreatedNote()  
    obj.drawNote()
    
except IndexError:
    print("There is no note with such number")
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
