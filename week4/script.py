# Step 1: Create and write to input.txt (optional: only if it doesn't exist)
with open("input.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("Here is another line of text.\n")
    file.write("Python makes file handling easy.\n")
    file.write("This is the fourth line.\n")
    file.write("And here comes the final line.\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 3: Process the content
word_count = len(content.split())
upper_content = content.upper()

# Step 4: Write processed content and word count to output.txt
with open("output.txt", "w") as file:
    file.write("PROCESSED TEXT:\n")
    file.write(upper_content + "\n")
    file.write(f"WORD COUNT: {word_count}\n")

# Step 5: Print success message
print("✅ Success! Processed content written to output.txt")
