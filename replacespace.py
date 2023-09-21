def replace_whitespace_with_underscore(filename):
    try:
        # Read the contents of the file
        with open(filename, 'r') as file:
            contents = file.read()

        # Replace whitespace with underscore
        modified_contents = contents.replace(' ', '_')

        # Write the modified contents back to the file
        with open(filename, 'w') as file:
            file.write(modified_contents)

        print('Whitespace replaced with underscore and saved to', filename)
    except FileNotFoundError:
        print('File not found:', filename)
    except Exception as e:
        print('An error occurred:', str(e))

# Replace with your file path
filename = 'file.txt'
replace_whitespace_with_underscore(filename)
