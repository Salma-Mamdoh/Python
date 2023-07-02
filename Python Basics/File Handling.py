# file handling in python
# "a"  Append open file for appending values , create file if not exists
# "r" Read [Default value] open file for read and give error if file not exists
# "w" open file for writing , create file if not exists
# "x" create file , Give Error ir File exists

# import os
# print(os.getcwd()) # main current working directory
# print(os.path.dirname(os.path.abspath(__file__))) # directory for the oppend file
# os.chdir(os.path.dirname(os.path.abspath(__file__))) # change current working directory
file = open("file.txt","r")
print(file) # <_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>
# print(file.read()) # default value read all content of the file , but can specify num of chars you want to read
# output hallo
# keep going
# love you
# print(file.read(5)) # hallo

# print(file.readline()) # default read first line
# print(file.readline(2)) # read first 2 chars in the second line as he read the first line in the privious line of code


# print(file.readlines()) # ['hallo \n', 'keep going \n', 'love you \n']

# for line in file:
    # print(line,end="")

# output hallo
# keep going
# love you

# file.close()

# file.write("this new line write it ") # remove the old content of file and write this new content
# to avoid this open fila with status "a" for append not "w" for write
# file.write("this second new line by append method \n")
# file.write("this third new line by append method \n")


# Truncate
# file.truncate(10) # this deleted all content except first 10 chars  # this new l this become the content of file

# print(file.tell()) # 77 this the postion of writing indicator in the file consider new line with 2 postions
# file.seek(5) move the writing indicator to the position that you want to start read from it
# print(file.read())

# import os
# os.remove("path of file or folder you want to remove")