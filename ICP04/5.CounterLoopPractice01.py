def arithmetic(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return True

    num = lst[1] - lst[0]

    for i in range(2, len(lst)-1):
        if lst[i] - lst[i-1] != num:
            return False
    return True

print(arithmetic([3, 6, 9, 12, 15]))
print(arithmetic([3, 6, 9, 11, 14]))
print(arithmetic([3]))
print(arithmetic([]))