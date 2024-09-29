def summer_sell_off():
    i, f= input().split()
    products = []
    clients = []
    
    # Read the product and client information for each of the n days
    for _ in range(n):
        k, l = map(int, input().split())  # Read k and l for each day
        products.append(k)  # Add k (number of products) to the products list
        clients.append(l)   