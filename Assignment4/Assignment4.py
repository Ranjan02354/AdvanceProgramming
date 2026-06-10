def add_products():
    products = []
    n = int(input("Enter number of products: "))


    for i in range(n):
        print("\nProduct", i+1)
        name = input("Enter product name: ")
        stock = int(input("Enter stock quantity: "))

        product = {
            "name": name,
            "stock": stock
        }

        products.append(product)

    return products


def display_low_stock(products):
    print("\nProducts with stock less than 10:")
    found = False

    for product in products:
        if product["stock"] < 10:
            print("Name:", product["name"], "| Stock:", product["stock"])
            found = True

    if not found:
        print("No products with stock less than 10")


def display_all_products(products):
    print("\nAll Products:")
    for product in products:
        print("Name:", product["name"], "| Stock:", product["stock"])


products_list = add_products()
display_all_products(products_list)
display_low_stock(products_list)
