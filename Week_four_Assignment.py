"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""
input_file = input("Enter the filename: ")
output_filename = "modified_" + input_file

try:
        # Read the input file
        with open(input_file, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content (convert to uppercase as an example)
        modified_content = content.upper()
        
        # Write to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Successfully read '{input_file}' and wrote modified content to '{output_filename}'.")

except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
except PermissionError:
        print(f"Error: Permission denied when accessing '{input_file}' or writing to '{output_filename}'.")
except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
