def read_file(file_name):
    try:
        file = open(file_name, "r")
    except OSError:
        print("__CONTENT_START__")
        print("__NO_SUCH_FILE__")
    else:
        print("__CONTENT_START__")
        print(file.read())
        file.close()
    finally:
        print("__CONTENT_END__")

read_file(r"D:\Projects\Python\words.txt")

