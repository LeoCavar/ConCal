#!/usr/bin/python3

import sys
import decimal

def perform_operation(num1, operator, num2):
    try:
        num1 = decimal.Decimal(num1)
        num2 = decimal.Decimal(num2)
    except decimal.InvalidOperation:
        print("Druga i treća vrijednost moraju biti broj.")
        sys.exit(1)

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Nije moguće dijeliti s nulom.")
            sys.exit(1)
        result = num1 / num2
    else:
        print("Error: Invalidni operator. Molimo koristite +, -, *, or /.")
        sys.exit(1)

    print(f"Rezultat: {result:.4f}")

if len(sys.argv) != 4:
    print("Koristite ovaj skript s tri argumenta u formatu: broj operator broj")
    sys.exit(1)

number_one = sys.argv[1]
operator = sys.argv[2]
number_two = sys.argv[3]

perform_operation(number_one, operator, number_two)
