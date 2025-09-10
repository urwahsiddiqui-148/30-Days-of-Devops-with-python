##file = open("day3.txt",'r')
file1 = open("day3.txt",'w')
file1.write("THIS IS REWRITTEN FILE CONTENT")
file1 = open("day3.txt",'r')
content = file1.read()

##content = file.read()
##readoneline = file.readline()
##readoneline = file.readlines()

##file.close()
print(content)

file1.close()