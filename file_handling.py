
### shows that default mode
"""
### Modes of Opening a File

| Character | Meaning                                           |
|-----------|---------------------------------------------------|
| 'r'       | open for reading (default)                        |
| 'w'       | open for writing, truncating the file first       |
| 'x'       | create a new file and open it for writing         |
| 'a'       | open for writing, appending to the end of the file if it exists |
| 'b'       | binary mode                                       |
| 't'       | text mode (default)                               |
| '+'       | open a disk file for updating (reading and writing) |

"""


# ### opens in read mode, write not possible
# file = open("test.txt", "r")
# print("File content ", file.read())
# file.close()

# ### opens in read write mode, without flusing the files
# file = open("test.txt", "r+")
# print("File content ", file.read())
# file.close()

# ### open for writing, appending to the end of the file if it exists
# file = open("test1.txt", "x+")
# print("File content ", file.read())
# file.close()

# ### opens in read write mode, without flusing the files
# file = open("test.txt", "a+")
# print("File content ", file.read())
# file.close()

# ### opens in read write mode, flusing the files
# file = open("test.txt", "w+")
# print("File content ", file.read())
# file.close()

### opens in image or binary file
# file = open("sample_image.jpg", "rb+")
# print("File content ", file.read())
# file.close()



### file context manager
"""
with open("test.txt", "r") as file:
    print(file.read())

# open 2 files with context manager
with open("test.txt", "r") as file1:
    with open("test.txt", "r") as file2:
        print(file1.read())
        print(file2.read())   

## using format2
with open("test.txt", "r") as file1, open("test.txt", "r") as file2:
    print(file1.read())
    print(file2.read())
"""
    
### understand read, readline and readlines
# with open("test.txt", "r") as file:
#     print(file.read())
"""
## to read a large chunk of data
with open("test.txt", "r") as file:
    file.readline()
    file.readline()
    file.readline()

with open("test.txt", "r") as file:
    print(file.readlines())

## to read a large chunk of data
with open("test.txt", "r") as file:
    for line in file:
        print(line, end="")

"""
 
### understanding file seek() and tell()
"""
file = open("test.txt", "r+")
print("File pointer position ", file.tell())
print("File content ", file.read())
print("File pointer position ", file.tell())
## move to start of the file
file.seek(0)
print("File pointer position ", file.tell())
print("File content ", file.read())
## move to end of file
file.seek(0, 2)
print("File pointer position ", file.tell())
print("File content ", file.read())
file.close()
"""

## understand write, writelines

file = open("test_write.txt", "w+")
file.write("Hello wrold!!!")
file.seek(0)
print("File content ", file.read())

file.write("i am second line")
file.seek(0)
print("File content ", file.read())

lines = ["one", "two", "three"]
file.writelines(lines)
file.seek(0)
print("File content ", file.read())

file.close()


### copy file1 content into file2

with open("test.txt", "r") as file1:
    with open("test1.txt", "w+") as file2:
        file_content1 = file1.read()
        file2.write(file_content1)
        print(file2.read())
    

## using format2
with open("test.txt", "r") as file1, open("test1.txt", "w+") as file2:
        file_content1 = file1.read()
        file2.write(file_content1)
        print(file2.read())

with open("sample_image.jpg", "rb") as file1, open("sample_image_copy.jpg", "wb+") as file2:
        file_content1 = file1.read()
        file2.write(file_content1)
        print(file2.read())
