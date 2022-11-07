if 'cde' in 'abcdefg':
    print('hello')
else:
    print('nope')

print(type('cde' in 'abcdefg'))

def fun(a=2,b=4,c=2,d=4):
    return a+b+c+d

print(fun())
print(fun(a=1,d=2))

print('abcdefg'.replace('cde', 'zzz'))