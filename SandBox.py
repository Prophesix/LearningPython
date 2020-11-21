#Quick Refresher:
#Comments
name = input('Whats your name?: ')#Prompts for name
print('Hello ' + name)#Prints Hello *inputname*

#Calculate the area of a circle
radius = input("Enter the radius of your circle in Meters: ")
area = 3.142 * int(radius)**2#Type casting from a STRING to a INT
print("The Area of your circle is: ", area)

#String Formatting
num1 = 3.1425467389
num2 = 10.2903948
#Previous method:
print('num 1 is', num1, 'and num 2 is', num2)
#FORMAT METHOD
print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))
#Formatting examples:
#{0:.3} = Index property 0 : show 3 numbers(IE: 3.14)
#{0:.3f} = Index property 0 : show 3 floating points (IE: 3.142)
#USING F-Strings
print(f'num 1 is {num1:.3f} and num 2 is {num2:.3}')
#Formatting for F-Strings is the same as Format method

#IF statement Example
age = int(input('Enter your age:'))
if age < 10:
    print('You are under 10')
elif age == 10:
    print('You are 10')
else:
    print('You are over 10')
#FOR Loop example
ninjas = ['Ryu','Yoshi','Jeki','Ken']
for ninja in ninjas:#Can be sliced IE: For ninja in ninjas[1:3]
    if ninjas == 'Yoshi':
        print(f'{ninja} -Black belt')
        break
    else
        print (ninja)
#WHILE Loop example
age = 25
num = 0
while num < age:
    #if num == 0:
    #
    #if num % 2 == 0: #Print out even numbers ONLY
    print(num)
    num += 1#Incrementer to eventually fall out of the Loop
#Ranges
for n in range(5):
    print(n)
    #Counts 0-5
    #prints 0 1 2 3 4
#More Range Examples
for n in range(3,10):
    print(n)
    #Counts 3-10
    #prints 3 4 5 6 7 8 9
for n in range(0,20,4)
    print(n)
    #0-20 count by 4
    #prints 0 4 8 12 16

#FUNCTIONS:
#function defined:
def greet(name, time):
    print(f'Hello {name} it is {time}')
#Function called
greet(bob, afternoon)

#Playground Follows:
print ('Sandbox 0.1')
print ('')
print (' ,_ o')
print ('/ //\,')
print (' \>> |')
print ('  \\,')
print ('Created by: Alex Biglen')
print ('Date: 08/03/2019')
