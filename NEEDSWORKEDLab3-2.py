#David Garrett
#EET-107-100 Chapter 3 Lab 2
#2021-02-10

BASE_RATE = 50

print('Car Insurance Rate Estimator\n') #Changed /n to \n to properly create the new line character
age = int(input('Enter your current age: '))
sex = input('Enter your sex: ')
stateOfResidence = input('Enter your state of residence: ') #Changed state to stateOfResidence because stateOfResidence variable, not state, is used later on in the code

cost = BASE_RATE
if sex == 'M': #Changed = to == so that it's a comparison between the two values rather than an assignment statement
	cost = cost + (BASE_RATE * .25)
if state == 'MI' or state == 'FL':
	cost = cost + (BASE_RATE * .10)
if age < 21 or age > 70:
	cost = cost + (BASE_RATE * .05) #Changed .25 to .05 since it's suppose to be 5% premium rather than a 25% premium

print('\nYou are a', age, 'year old ' + sex, 'and you live in ' + stateOfResidence)
print('Your insurance will cost $', format(cost, '.2f'), sep='')