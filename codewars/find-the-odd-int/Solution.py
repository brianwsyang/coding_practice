def find_it(seq):
    # store values in hashset for O(1) search
    num_set = set()
    
    for n in seq:
        if n in num_set:
            num_set.remove(n)
        else:
            num_set.add(n)
    
    return list(num_set)[0]
