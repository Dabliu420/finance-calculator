z = input("Hello! What would you like to do?\n\nA) Calculate the price of a bond\nB) Calculate the duration of a financial portfolio\nC) Calculate the monthly mortgage payment\n\n")


# Bond Price

def price_with_coupons():
    t = int(input("In how many years does the bond mature? "))
    ytm = float(input("Enter the Yield to Maturity (YTM) in %: "))
    coupon_rate = float(input("Enter the annual coupon rate in %: "))
    face_value = float(input("Enter the face value: "))
    payments_per_year = int(input("Enter the number of coupon payments per year: "))

    price = 0.0
    coupon = ((coupon_rate / 100) * face_value) / payments_per_year

    for i in range(0, t):          
        for y in range(1, payments_per_year + 1):  
            period = i + y / payments_per_year
            price += coupon / ((1 + ytm/100) ** period)

    price += face_value / ((1 + ytm/100) ** t)

    return price


def price_without_coupons():
    t = int(input("In how many years does the bond mature? "))
    face_value = float(input("Enter the face value: "))
    rate = float(input("Enter the yield in %: "))

    price = face_value / ((1 + rate/100) ** t)

    return price


if z in ["A", "a"]:
    x = input("Does the bond pay coupons? (yes/no): ").lower()

    if x in ["yes", "y"]:
        price = price_with_coupons()   
        print("\nBond price:", round(price, 2))

    elif x in ["no", "n"]:
        price = price_without_coupons() 
        print("\nBond price:", round(price, 2))

    else:
        print("Invalid answer.")



# Duration of a financial portfolio

def duration():
    y = input("Does the bond pay coupons? (yes/no): ").lower()
    
    if y in ["yes", "y"]:
        t = int(input("In how many years does the bond mature? "))
        ytm = float(input("Enter the Yield to Maturity (YTM) in %: "))
        coupon_rate = float(input("Enter the annual coupon rate in %: "))
        face_value = float(input("Enter the face value: "))
        payments_per_year = int(input("Number of coupon payments per year: "))

        price = 0.0
        coupon = ((coupon_rate / 100) * face_value) / payments_per_year

        for i in range(0, t):
            for s in range(1, payments_per_year + 1):
                period = i + s / payments_per_year
                price += coupon / ((1 + ytm/100) ** period)

        price += face_value / ((1 + ytm/100) ** t)

        numerator = 0.0
        for i in range(t):
            for s in range(1, payments_per_year + 1):
                period = i + s / payments_per_year
                discounted_cf = coupon / ((1 + ytm/100) ** period)
                numerator += period * discounted_cf

        discounted_face = face_value / ((1 + ytm/100) ** t)
        numerator += t * discounted_face

        dur = numerator / price
    
        return price, dur
    
    elif y in ['no', 'n']:
        t = int(input("In how many years does the bond mature? "))
        face_value = float(input("Enter the face value: "))
        rate = float(input("Enter the yield in %: "))

        price = face_value / ((1 + rate/100) ** t)
        dur = t  

        return price, dur

    else:
        print("Invalid answer.")
        return None, None

        

if z in ['B', 'b']:
    x = int(input('How many securities does your portfolio contain? '))

    if x == 1:
        price, dur = duration()

    elif x > 1:
        i = 0
        prices = []
        durations = []
        while i < x:
            price, dur = duration()
            
            prices.append(price)
            durations.append(dur)

            i = i + 1

        total_duration = 0.0

        for v in range(x):
            total_duration = total_duration + (prices[v] / sum(prices)) * durations[v]

        print('\nThe duration of your portfolio is', total_duration, 'years')



# Mortgage payment

if z in ['C','c']:
    principal = float(input('Enter the loan amount: '))
    rate = float(input('Enter the periodic interest rate (monthly) in %: '))
    n = int(input('Enter the total number of months: '))

    rate = rate / 100   

    payment = principal * (rate * (1 + rate)**n) / ((1 + rate)**n - 1)

    print('Your monthly payment is', str(round(payment, 2)) + '€')

    x = input('Do you want to calculate the total interest paid? ').lower()

    if x in ["yes", "y"]:
        total_interest = payment * n - principal
        print('Total interest paid:', str(round(total_interest, 2)) + '€')
    else:
        pass
