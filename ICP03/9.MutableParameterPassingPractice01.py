def swapFL(alist):
    last = len(alist) - 1
    alist[0], alist[last] = alist[last], alist[0]
    print(alist)


ingredients = ['flour', 'sugar', 'butter', 'apples']
swapFL(ingredients)
