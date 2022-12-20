myfile=open('countries.txt', 'r') 
#r means read this file
#w means write in this file
#a means append in this file
#r+ means both reading and writing

print(myfile.readable())  #Do we have access to read this file? It will return true/false

# print(myfile.readline())
# print(myfile.readline())  This will print 2 lines

for item in myfile.readlines():
    print(item, end='')

myfile.close()