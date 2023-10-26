import random
def random_picker(lists, num):
    for i in range(num):
        print(random.choice(lists))

num_lists = [3, 2, 1, 34, 5]
random_picker(num_lists, 3)