#Shipping Cost Calculator

##Input package weight and Shipping rate
weight=float(input("Enter the package weight in kilograms:"))
rate=float(input("Enter the shipping rate per kilogram:"))

##Calculate Shipping Cost
Shipping_cost=weight*rate

##Display the result
print(f"Shipping cost: {Shipping_cost} USD")
