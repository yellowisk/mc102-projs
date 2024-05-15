def getCost(products, purchases):
    cost = 0
    for item, quantity in purchases:
        cost += products[item] * quantity
    return cost

def catalogProds(numProducts):
    products = dict()
    for i in range(numProducts):
        item, price = input().split()
        products[item] = float(price)
    return products

def catalogItems(numItems):
    purchases = []
    for k in range(numItems):
        item, quantity = input().split()
        purchases.append((item, int(quantity)))
    return purchases

trips = int(input())

for i in range(trips):
    numProducts = int(input())
    products = catalogProds(numProducts)
    
    numItems = int(input())
    purchases = catalogItems(numItems)
    
    totalCost = getCost(products, purchases)
    
    print("R$ {:.2f}".format(totalCost))