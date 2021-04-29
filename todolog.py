import time

class Log:
    def __init__(self, path):
        self.path = path
    def addNoteLog(self, lognote):
        timestamp = time.time()
        info = " [INFO] "
        if lognote == 0:
            note="All notes shown"
        elif lognote == 1:
            note = "New task added to list"
        elif lognote == 2:
            note = "Note deleted from the list"
        elif lognote == 3:
            note = "Note drawn"
        elif lognote == 4:
            note = "Aplication starts"
        else: 
            info = " [ERROR] "
            note = "Adding new task to list has failed. No storage file was found."
            with open(path, "a") as f:
                f.write(str(timestamp) + info + note +"\n")
                return
        with open(self.path, "a") as f:
            f.write(time.strftime("%Y-%B-%d %H:%M:%S") + info + note +"\n")
        f.close()
        

