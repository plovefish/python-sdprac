def multiple(limit):
    flag = 1
    summary = 0
    while flag < limit:
        if flag % 3 == 0 or flag % 5 == 0:
            summary += flag
        flag += 1
    return summary

print(multiple(10))