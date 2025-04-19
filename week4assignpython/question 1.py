# Function to read a file, modify its content, and write to a new file
def modify_file(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as infile:
            content = infile.readlines()
        
        # Modify the content (example: add line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content has been written to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file name
    output_file = "output.txt"  # Replace with your output file name
    modify_file(input_file, output_file)