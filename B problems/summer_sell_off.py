def summer_sell_off():
    i, f = map(int, input().split())
    products = []
    clients = []
    if i == 0:
        print(0)
        return
    if f == 0:
        total_sum = 0  
        for _ in range(i):
            k, l = map(int, input().split())  
            total_sum += min(k, l)
        print(total_sum)
        return  
    list_of_added_products = [0] * f
    
    total_sum = 0  
    for _ in range(i):
        k, l = map(int, input().split())
        products.append(k)
        clients.append(l)
    for k in range(f):
        if clients[k] <= products[k]:
            total_sum += clients[k]  
            continue 
        diff = clients[k] - products[k] * 2 
        if diff >= 0:  
            list_of_added_products.remove(0)
            list_of_added_products.append(products[k])
            total_sum += products[k]  
        else:  
            list_of_added_products.remove(0)
            list_of_added_products.append(clients[k] - products[k])
            total_sum += products[k]
    for j in range(f,i):
        if clients[j] <= products[j]:
            total_sum += clients[j]  
            continue 
        diff = clients[j] - products[j] * 2  
        if diff >= 0:  
            if min(list_of_added_products) < products[j]:
                min_value = min(list_of_added_products)
                list_of_added_products.remove(min_value)
                list_of_added_products.append(products[j])
            total_sum += products[j]  
        else:  
            if min(list_of_added_products) < (clients[j] - products[j]):
                min_value = min(list_of_added_products)
                list_of_added_products.remove(min_value)
                list_of_added_products.append(clients[j] - products[j])
            total_sum += products[j]  
    total_sum += sum(list_of_added_products)
    print(total_sum)  
    
        
    
summer_sell_off()
