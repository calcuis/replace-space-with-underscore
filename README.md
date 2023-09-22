## replace-whitespace(' ')-with-underscore('-')

Replace 'file.txt' with the actual file (path) you want to modify.

**Main purpose**

This code reads the file, replaces whitespace with underscores, and saves the modified content back to the same file.

## code review
The given Python code defines a function named `replace_whitespace_with_underscore` that takes a filename as an argument. The goal of this function is to replace all occurrences of whitespace characters (spaces) in the content of the specified file with underscores (_) and save the modified content back to the same file.

Here's a step-by-step explanation of the code:

Function Definition:
```
def replace_whitespace_with_underscore(filename):
```
This line defines a function named `replace_whitespace_with_underscore` that takes a single parameter, filename, which is expected to be a string representing the name of the file to be processed.

Try-Except Block:
```
try:
```
This line initiates a try-except block. Code inside this block is attempted, and if an exception is raised, it is caught and handled.

Opening the File in Read Mode:
```
with open(filename, 'r') as file:
    contents = file.read()
```
Within the try block, the function attempts to open the specified file (filename) in read mode ('r') using a context manager (with statement) and assigns the content of the file to the variable contents.

Replacing Whitespace with Underscore:
```
modified_contents = contents.replace(' ', '_')
```
The function replaces all spaces (' ') in the content (stored in contents) with underscores ('_') and stores the modified content in the variable modified_contents.

Opening the File in Write Mode and Saving Modified Content:
```
with open(filename, 'w') as file:
    file.write(modified_contents)
```
The function then opens the same file (filename) in write mode ('w') using a context manager and writes the modified content (modified_contents) to the file, effectively replacing the original content.

Print a Success Message:
```
print('Whitespace replaced with underscore and saved to', filename)
```
Finally, the function prints a success message indicating that the whitespace has been replaced with underscores and the modified content has been saved to the specified file.

Exception Handling:
```
except FileNotFoundError:
    print('File not found:', filename)
except Exception as e:
    print('An error occurred:', str(e))
```
If a `FileNotFoundError` is raised (indicating that the specified file does not exist), it is caught and an error message is printed. Additionally, if any other exception is raised during the try block, it is caught and a general error message along with the specific error is printed.

Function Call:
```
filename = 'file.txt'
replace_whitespace_with_underscore(filename)
```
Finally, the code sets the variable filename to 'file.txt' and calls the `replace_whitespace_with_underscore` function with this filename as an argument, initiating the processing of the file.

## exercise
You can modify the whitespace and underscore into anything, i.e., replace 'Apple' with 'Orange', etc.
