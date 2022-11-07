myTuple = ("John", "Peter", "Vicky")

x = "aaa".join(chara for chara in 'asfs')

print(x)

sale_dict = {'sunday': 50.3, 'monday': 63.20}

#sunday, monday are keys, 50.3 and 63.20 are values associated
#with keys

#the key has to be unique

print(sale_dict['sunday'])

sale_dict['tuesday'] = 66.66
print(sale_dict)

#sale_dict[0] don't have indexes, has keys
print(sale_dict['monday'])
print('Monday' in sale_dict) #false
print('monday' in sale_dict) #true

sales = {'sunday':0, 'monday':0, 'tuesday':0, 'wednesday':0,
         'thursday':0, 'friday':0,'saturday':0}


import pickle

def totalSales(temp_dict):
    total = 0
    for key in temp_dict.keys():
        total = total + temp_dict[key]
    return total

def main():
    print('enter the sales for the week....')
    for key in sales.keys():
        print("Enter the sales for ", key,": ", sep='', end='')
        sales[key] = float(input())

    print(sales)
    weekly_sales = totalSales(sales)
    print('Total sales is $' + str(weekly_sales), sep='')
    avg_sales = weekly_sales/len(sales)
    print('average is $:', str(avg_sales), sep='')
    print('Max sales was on ', maxSales(sales), ' for $',
            sales[maxSales(sales)], sep='')
    saveSales('sales2.dat', sales)
    readSales('sales2.dat')


def maxSales(temp_dict):
    max_value = 0
    max_key = ''
    for key in temp_dict.keys():
        if temp_dict[key] > max_value:
            max_key = key
            max_value = temp_dict[key]
    return max_key

def saveSales(filename,sales_dict): #saves dictionary by pickle
    out_file = open(filename, 'wb') #write,binary
    pickle.dump(sales_dict, out_file)
    out_file.close()

def readSales(filename):
    input_file = open(filename, 'rb') # read binary
    end_of_file = False
    while not end_of_file:
        try:
            element = pickle.load(input_file)
            print(element)
        except EOFError:
            end_of_file = True

    input_file.close()

main()


print(sales.items()) #creates a bunch tuples of the dictionary
del sales['thursday']
print(sales)
sales['thursday'] = 500
print(sales) #thursday in the end now

temp = set('This is a sentence')
print(temp)
len(temp)
temp = 'This is a sentence'
aaa = set(temp.split())
print(aaa)
text2 = 'with repeats with repeat withs repeats with repeat'
print(text2.split())
print(set(text2.split()))

