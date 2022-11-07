#days_of_week = [m,t,w,h,f,sa,su]


def testtt():
    return 1, 2, 4

x, y, z = testtt()

this_turns_into_tuple = testtt()

print(z,y,x)

# can use for loop to analyze one character at a time

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#for ch in alphabet:
    #print(ch)
    # prints one character one at a time

print(alphabet[3])
alphabet[-8]

print(alphabet[3:8])

#LISTS AND STRINGS ARE VERY SIMILAR USES LEN, INDEX FUNCTION

name = 'bob'

name += alphabet

print(name)


#strings are immutable, like a tuple

#python can't change string, but can overwrite

age = '5'
print(age.isdigit())

# if you compare strings, python is case sensitive

name2 = '       fffff        '
print(name2.rstrip())
print(name2.lstrip())
### STRIP REMOVES SPACES, TABS, NEWLINES
print(name2.strip())

text = ' this is exciting    %%%%%%     '

print(text.strip(' '))
print(text.strip(' %'))
print(text.strip(' %g'))
print(text.strip(' %ing'))
print(text.strip(' %inG'))

print('this is uper'.upper())

print(text.find('%'))
print(text.find('%', 55)) #returns -1 since no % past index 55

print(text.replace('%', 'l'))
print(text.replace('th', 'aaaa'))

print(text.split())
