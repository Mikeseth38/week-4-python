def read_file():
    try:
        # Ask the user for a filename
        filename = input("Enter the filename to read: ")
        
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_file()