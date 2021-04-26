import errno

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
