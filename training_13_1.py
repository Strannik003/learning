orders = []
id_count = 0
def create_order(customer_name):
    global id_count
    id_count += 1
    order = {
        "id": id_count,
        "customer":customer_name,
        "products": [],
        "closed": False
    }
    orders.append(order)
    return orders

def add_product(order_id, product_name):
    for order in orders:

        if order["id"] == order_id:
            if order["closed"] == True:
                return  ["You can not edit it, cause it's already closed"]
            order["products"].append(product_name)
            return orders
        
    return ["there is no order with such id"]

def close_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            if order["closed"] == True:
                return ["You can not edit it, cause it's already closed"]
            order["closed"] = True
            return orders  
    return ["there is no order with such id"]
        
def get_order(order_id):
    for order in orders:
        if order["id"] == order_id:
            return order

if __name__ == "__main__":
        
    create_order("Anton")
    create_order("Anton1")
    close_order(2)
    print(add_product(2, "affdf"))
    print(orders)
    

# {
#     "id": 1,
#     "customer": "Andrei",
#     "products": [],
#     "closed": False
# }

# add_product(order_id, product_name)
# get_order_total(order_id)
# close_order(order_id)