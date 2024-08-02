def isSubset( a1, a2, n, m):
    n = len(a1)
    m = len(a2)
    y = 'Yes'
    no = 'No'
    if m > n:
        return no
    a1_counts = {}
    for element in a1:
        a1_counts[element] = a1_counts.get(element,0) + 1
    for element in a2:
        if element not in a1_counts or a1_counts[element] == 0:
            return no
        a1_counts[element] -= 1
    return y
