"""
- Write a function that will work out the amount of VAT
(https://en.wikipedia.org/wiki/Valueadded_tax) that is associated with a
sale of a product. The function should take a gross price of
the product as an input, and then return the net price (without VAT)
and the amount of VAT to pay.
UK VAT is 20%. 
"""

def vat(gross,tax):
    tax_percentage = tax/100
    net_price = gross/(1+tax_percentage)
    VAT_to_pay = net_price*tax_percentage
    return net_price, VAT_to_pay

price = float(input("Enter the gross price: £"))
vat_value = float(input("Enter tha VAT value: "))
final = vat(price,vat_value)
print(f"The net price is: £{final[0]}")
print(f"The amount of VAT to pay is: £{final[1]}")