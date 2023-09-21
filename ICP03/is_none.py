thing = None
if thing:
    print("It's something")
else:
    print("It's nothing")
# Q1. Something? Nothing?

if thing is None:
    print("It's nothing")
else:
    print("It's something")
# Q2. Nothing? Something?

def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")


is_none(None)  # Q3.
is_none(True)  # Q4.
is_none(False)  # Q5.
is_none(0)  # Q6.
is_none(0.0)  # Q6.
is_none(())  # Q7.
is_none([])  # Q8.
is_none({})  # Q9.
is_none(set())  # Q10.
