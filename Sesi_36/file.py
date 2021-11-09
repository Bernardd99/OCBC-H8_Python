# # untuk membuka file
# file = open('Hack8_Sample_Text.txt')

# #menutup file
# file.close()

# # cara lebih aman unmtuk membuka file
# try:
#    f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
#    print('Opening the file')
#    # perform file operations
# finally:
#    f.close()
#    print('Closing the file')


# # tipe" file
# open('abc.txt') # open

# open('abc.txt', 'r') # read 

# open('abc.txt', 'w') # write

# # buffered binary
# open('abc.txt', 'rb')

# open('abc.txt', 'wb')

# #raw file
# open('abc.txt', 'rb', buffering=0)

# # membuat file dan mengisikan data pada file
# with open("sample.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")


f = open("sample.txt",'r',encoding = 'utf-8')

# test = f.read(4) # read the first 4 data

# test1 = f.read(4)    # read the next 4 data

# test2 = f.read()     # read in the rest till end of file

# test3 = f.read()  # further reading returns empty sting

# test4 = f.tell()

# test5 = f.seek(0)

# print(test)
# print(test1)
# print(test2)
# print(test3)
# print(test4)
# print(test5)

#read file with iteration
f.seek(0)   # bring file cursor to initial position
for line in f:
  print(line, end = '')

f.seek(0)
#read file till end of line
print(f.readline())

# how to open and read the entire file using .read():
with open('sample.txt', 'r') as reader:
     # Read & print the entire file
     print(reader.read())