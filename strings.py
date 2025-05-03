#here are all the examples for the python strings and its methods

a = "hello wORld!!!!!" #single line string
b = '''
hello
world,
I 
an
good''' #this is a multiline string
c = "abc"

#indexing
print(a.index('R'))

#slicing 
for i in a:  #slicing using for loop
    print(i)
print('from 0 to 3',a[:4]) #from 0 to 3
print('from 1 to 4',a[1:5]) #from 1 to 4
print('from 2 to end',a[2:]) #from 2 to end
print('last 3 char',a[-3:-1]) #last 3 char

#string methods
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.replace("h","m"))
print(a.rstrip("!"))
print(a.capitalize())
print(a.capitalize())
print(a.split(" "))