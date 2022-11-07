from guizero import App, CheckBox, ButtonGroup, PushButton, Text

##Fuctions ----

def service_total():
    discounts = {'No Discount':0.0,  '5% Discount':0.05, '10% Discount':0.1, 'Employee Discount':0.15}
    total = 0.0
    if oil_checkbox.value == True: #YOU DON'T NEED THE '== TRUE' PART
        total += 30.00
    if lube_checkbox.value:
        total += 20.00
    if radiator_checkbox.value:
        total += 40.00
    if transmission_checkbox:
        total += 100.00

    key = discount_radbt.value
    discount_value = float(discounts[key])
    total = total - total*discount_value
    total_output.value = 'The total service charge is $' + format(total, '.2f')


## Globals -----


##App----------
app = App(title='Joes Automative', layout='grid')
services_label = Text(app, text='List of available services:', grid=[0,0,])
oil_checkbox = CheckBox(app, text='Oil change--$30.00', grid=[0,1], align='left')
lube_checkbox = CheckBox(app, text='Lube change--$20.00', grid=[0,2], align='left')
radiator_checkbox = CheckBox(app, text='radiator flush--$40.00', grid=[0,3], align='left')
transmission_checkbox = CheckBox(app, text='transmission flush--$100.00', grid=[0,4], align='left')

total_output = Text(app, text='', grid=[1,1])
total_button = PushButton(app, text='Calculate Total', grid =[0,7], command=service_total)

discount_label = Text(app, text='Available discounts:', grid=[0,5])
discount_radbt = ButtonGroup(app, options=['No Discount', '5% Discount', '10% Discount', 'Employee Discount'],
                                            grid=[0,6], selected="No Discount")

app.display()