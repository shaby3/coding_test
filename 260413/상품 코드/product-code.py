product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product:
    def __init__(self, name = "codetree", code = 50):
        self.name = name
        self.code = code


P1 = Product()
P2 = Product(product_name, product_code)

print(f"product {P1.code} is {P1.name}")
print(f"product {P2.code} is {P2.name}")

