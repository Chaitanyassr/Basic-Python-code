'''print("hello world")
num1 = 10
num2 = 20
print("num1+num2=",num1+num2)
'''
'''x=True
y=False
print(x and y)
print(x or y)
print(not x)
'''
'''
num4 = 3 #110
num5 = 12 #010
print(num4 & num5)
print(num4 | num5)
print(num4 ^ num5)
print(num4 >> 2)
print(num5 << 2)'''

'''name = "chinu"
print(name)
print("i love \' python")
print("""i love ,,,,python""")
print("""hello"""[1])'''
'''print("""hello"""[0:3])'''
'''print("hello")
print("line1\nline\n2line\n3")
'''
'''variable and data type'''
'''greetings = "hello world"'''

#data type
'''myStr,myInt,myFloat'''
'''myStr = "chini"
print(type(myStr), myStr)
print(myStr)
#condition
x = 4
if x < 6: print("this is true")
else: print("this is false")'''
#loops
'''people = ["sera", "jhon", "humpty"]
print(people)
print(people[0])
for person in people:
    print("current person",person)

    for i in range(len(people)):
        print(people[2])

        for i in range(0,10):
            print("hello")'''

            #while loop
'''
count = 0
while count < 10:
    print(count)
    count = count + 1
'''
'''
count = 0
while count < 10:
    print(count)
    if count == 5:
        break
        count = count + 1
        '''

#function
'''
def sayhello(name):
    print("hello", name)
    
    sayhello("jhon")
    sayhello("carl")
'''

#return function
'''
 def getsum(num1, num2):
     total = num1 + num2
     return total

 numsum = getsum(3,4)
 print(numsum)'''

'''we = "nhjshkf cd"
print(we.capitalize())

#swap case

print(we.swapcase())

#get length

print(len(we))

#replace

print(we.replace("cd", "er"))

sub = "c"
print(we.count(sub))

#start with

print(we.startswith("n"))

#ends with

print(we.endswith("n"))

#split to list
print(we.split())

#find func

print(we.find("n"))

#index
#same as find , but gives an error when it doesnt find any thing
print(we.index("x"))

#is all alphanumeric

print(we.isalnum())

#is all alphabetic

print(we.isalpha())

#is all numeric

print(we.isnumeric())

'''

#modules

#how to insert A PY INTO A PY
'''WE USE import filename'''

#opening another file and write in it by using previous file
'''
fo = open("tstdjf.txt", "w")
fo.write("")
fo.close()

forvcreating

fo = open("trt.txt, "wt)
fo.write("this is my new file")
fo.close()
'''
#class
'''
class person:
    __name = ""
    __email = ""

def __init__(self, name, email):
    self.__name = name
    self.__email = email
    
    
    def set_name(self, name):
      self.__name = name

   def get_name(self):
    return self.__name


def set_email(self, email):
    self.__email = email


def get_email(self):
    return self.__email

def tostring(self):
    return "{} can be contact at {}".format(self.__name, self.__email)

brad = person(
"brad trabsvery", "sdfdfsdf.com")

print(brad.tostring())
print(brad.get_name())
print(brad.get_email())


'''
c = np.array([[1, 23, 4],[3, 4, 5]])
print(c)









































