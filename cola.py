def cola():
    welcome = input("Cola Calculator... by dwellkerwave")

    amount = int(input('Amount of Cold Drinks-'))
    type = str(input('Brand of Cold Drink-'))
    if type == 'Pepsi' or 'pepsi':
        print('The price of',amount,'Pepsi bottle(s) are INR',amount*34)
    if type == 'Coke' or 'Cola' or 'coke' or 'cola':
        print('The price of',amount,'Coca-Cola bottle(s) is INR',amount*40)
    if type == 'Fanta' or 'fanta':
        print('The price of',amount,'Fanta bottle(s) is INR',amount*38)
    if type == 'Mirinda' or 'mirinda':
        print('The price of',amount,'Mirinda bottle(s) is INR',amount*82)
    if type == 'Red Bull' or 'red bull':
        print('The price of',amount,'Red Bull can(s) is INR',amount*125)
    else:
        print('This is not a valid drink.')