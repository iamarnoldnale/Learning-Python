def calculate_discount(price, discount_percentage):

    if discount_percentage >= 20:
        discount = price * (discount_percentage/100)
        return discount
    else:
        return price

original_price = float(input("Item price: "))
discount_percent = float(input("Discount Percentage: "))
final_price = calculate_discount(original_price, discount_percent)

if original_price == final_price:
    print("No discount was applied."
          "Final price: ", final_price)
else:
    print("Final price: ", final_price)
