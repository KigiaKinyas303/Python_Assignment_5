# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line with text and numbers\n")
except Exception as e:
    print("Error creating file:", e)
else:
    print("File 'my_file.txt' created successfully.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nContent of 'my_file.txt':\n", content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Error reading file:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("\nAdditional line 1\n")
        file.write("Appending another line\n")
        file.write("Last line for appending\n")
except Exception as e:
    print("Error appending to file:", e)
else:
    print("\nContent appended to 'my_file.txt'.")

# Error Handling
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print("\nContent of 'nonexistent_file.txt':\n", content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("Error reading file:", e)
finally:
    print("This block always executes, regardless of errors.")
