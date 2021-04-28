import errno
class Todo:
    def addNote(self):
        try:
            with open("todoList.txt", "a") as f:
                f.write(input("Add to list: ")+"\n")
            f.close()
        except Exception as exc:
            if exc.errno == errno.ENOENT:
                print("The file doesn't exist.")
            elif exc.errno == errno.EMFILE:
                print("You've opened too many files.")
            else:
                print("The error number is:", exc.errno)
class Welcome():
    def hello(self):
        print("Welcome to the todo list\n"
        +"Show all notes: select 1\n"
        +"Add new note: select 2\n"
        +"Delete note with particural number: select 3\n"
        +"Draw a note: select 4\n")
    
obj = Welcome()
obj.hello()
obj2 = Todo()
obj2.addNote()