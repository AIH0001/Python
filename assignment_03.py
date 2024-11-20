
def calculate_bmi(weight, height):
    bmi = weight /(height ** 2)
    return bmi
    
def classify_bmi(bmi):
    if bmi < 18.5:
        category = 'underweight'
    elif bmi >= 18.5 and bmi< 25:
        category = 'normal weight'
    elif bmi >=25 and bmi < 30:
        category = 'overweight'
    else:
        category = 'obesity'
    return category
    
weight = float(input('enter your weight in kilograms: '))
height = float(input('enter your height in meter: '))
bmi = round(calculate_bmi(weight, height), 2)
category = classify_bmi(bmi)

print(f'bmi: {bmi}')
print(f'category: {category}')

    
def convert_currency(amount_in_usd, exchange_rate):
    amount_in_eur = amount_in_usd * exchange_rate
    return amount_in_eur
    
amount_in_usd = float(input('enter the amount in usd: '))
exchange_rate = float(input('enter the amount in exchange rate: '))
amount_in_eur = round(convert_currency(amount_in_usd, exchange_rate), 2)

print(f'amount in eur: {amount_in_eur}')

    
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal = float(input('enter the principal amount: '))
rate = float(input('enter the interest rate: '))
time = float(input('enter the time period (in years): '))

interest = round(calculate_simple_interest(principal, rate, time), 2)
print(f'simple interest: {interest}')  
    
