currency = ["USD", "EUR", "UAH", "BYN", "RUB"]
rate = [1, 0.8813, 28.69, 2.61, 77.59]

while True:
   # currency_num = None
    header = input('CHOOSE YOUR CURRENCY (USD,EUR,CHF,UAH,BYN,RUB): ')
    for i in range(len(currency)):
        if currency[i] == header:
           currency_num = i

    #if currency_num == None:
      #  print('YOUR VALUE is NONE')
      #  continue
    currency_amount = input("AMOUNT $ : ")
    if currency_amount is None:
        empty_form = True
    else:
        empty_form = False
    try:
        currency_amount = int(currency_amount)
        int_form = True
    except ValueError:
        int_form = False
    if empty_form:
        print("Your value is an empty field")
    elif int_form:
        if currency_amount >= 0:
            print("Your value :", currency_amount, currency[0])
            currency_result = currency_amount * rate[currency_num]
            print("Converted summ in", currency[currency_num], "=", currency_result)
        else:
            print("Your value < 0 ")
    else:
        print("Your value is a string. Input an interger")
