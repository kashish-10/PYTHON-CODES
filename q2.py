def credit_card(credit_card_number):
    n = len(credit_card_number)
    required_slice = credit_card_number[(n-4):n]
    return ("*" *(n-4) + required_slice)

demo_number = input()
result = credit_card(demo_number)
print("The required Credit Card Number : " + result)