def modify_file_content(content):
    """
    Modify the content as needed — here we'll reverse each line.
    You can customize this function!
    """
    modified_lines = [line.strip()[::-1] for line in content.splitlines()]
    return "\n".join(modified_lines)

def read_and_write_file():
    # Ask the user for the input file name
    input_file = input("📂 Enter the name of the file to read (e.g., input.txt): ")

    try:
        # Try to open and read the file
        with open(input_file, "r") as file:
            original_content = file.read()

        # Modify the content
        modified_content = modify_file_content(original_content)

        # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ Success! Modified content written to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Error: The file could not be read. Make sure it’s accessible.")

# Run the program
read_and_write_file()
