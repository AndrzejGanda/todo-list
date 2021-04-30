import errno
import random
from todolog import Log

class Todo(BaseException):
    objLog = Log("todoListLog.txt")
    def addNote(self):
        
        with open("todoList.txt", "a") as f:
            f.write(input("create a new note: ")+"\n")
        f.close()
        self.objLog.addNoteLog(lognote=1)

    def hello(self):
        self.objLog.addNoteLog(lognote=4)
        loop = True
        while loop == True:
            print("\nWelcome to the todo list\n"
            +"1) Show all notes: select 1\n"
            +"2) Add new note: select 2\n"
            +"3) Delete note with particural number: select 3\n"
            +"4) Draw a note: select 4\n"
            +"5) EXIT\n")
            input_menu = int(input("Select the option by typing the number: "))
            if input_menu == 1:
                obj.doList()
            elif input_menu == 2:
                obj.addNote()
            elif input_menu == 3:
                obj.deteleCreatedNote()
            elif input_menu == 4:
                obj.drawNote()
            elif input_menu == 5:
                raise Todo
            else:
                print("Wrong number, try again")

    def doList(self):
    
        index = 1
        with open("todoList.txt", "r") as f:
            print("Your notes:")
            for line in f:
                line = line.strip()
                print(str(index) + ") " +line)
                index = index + 1 
        self.objLog.addNoteLog(lognote=0)
        

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
        self.objLog.addNoteLog(lognote=2)

    def drawNote(self):
        with open("todoList.txt", "r") as f:
            #allText = f.read()
            #words = list(map(str, allText.split()))
            #drawline = random.choice(words)
            allText = f.readlines()
            drawline = random.choice(allText)
            print("The drawn note is: " + drawline)
        self.objLog.addNoteLog(lognote=3)
        
        input_answer = input("Delete the drawn note?(yes or no): ")
        if (str.upper(input_answer) == "YES"):
            
            with open("todoList.txt", "r") as f:
                lines = f.readlines()
            with open("todoList.txt", "w") as f:
                for line in lines:
                    
                    if line != drawline:
                        f.write(line)
            self.objLog.addNoteLog(lognote=2)
        elif (str.upper(input_answer) == "NO"):
            pass
        else:
            print("wrong answer, next time enter 'yes' or 'no'")

    def say_goodbye(self):
        print("Thank you for using our program. Be safe and have a nice day!")
        self.objLog.addNoteLog(lognote=5)



try:
    
    obj = Todo()
    obj.hello()
except Todo:
    obj.say_goodbye()
except ValueError:
    print("Only digites allowed")
except IndexError:
    print("There is no note with such number")
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
