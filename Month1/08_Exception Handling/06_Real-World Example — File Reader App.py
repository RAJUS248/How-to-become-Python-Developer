def file_reader(file):

    try:
        with open(file,"r") as f:
            data = f.read()

            print(data)

    except FileNotFoundError:
        print("Error: File not found!")

    except PermissionError:
        print("Error: Permission denied!")

    except Exception as e:
        print("Unknown error:", e)

    finally:
        print("File operation completed.")

file_reader("my_demo.txt")

