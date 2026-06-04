def interview(lst, tot):
    max = [5, 5, 10, 10, 15, 15, 20, 20]
    if len(lst) != 8:
        return "disqualified"
    for i in range(8):
        if lst[i] > max[i]:
            return "disqualified"
    if tot > 120:
        return "disqualified"
    return "qualified"
