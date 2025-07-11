products = {}

def add_product(name, price):
    products[name] = price

def update_price(name, new_price):
    if name in products:
        products[name] = new_price

def find_in_range(min_price, max_price):
    return {name: price for name, price in products.items() if min_price <= price <= max_price}


add_product("Pen", 20)
add_product("Notebook", 50)
update_price("Pen", 25)
print(find_in_range(20, 50))
