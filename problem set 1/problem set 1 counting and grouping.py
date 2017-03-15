def item_order(order):

    s = order.count('salad')
    h = order.count('hamburger')
    w = order.count('water')
    
    print 'salad:' + str(s) + ' hamburger:' + str(h) + ' water:' + str(w)

item_order("salad water hamburger salad hamburger")