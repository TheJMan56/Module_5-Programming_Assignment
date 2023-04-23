def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

def difference(arg):
    total = arg[0]
    del arg[0]
    for val in arg:
        total -= val
    return total
