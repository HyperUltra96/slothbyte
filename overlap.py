def overlap(str1, str2):
    start = 0
    for c in str1:
        if c == str2[start]:
            start += 1
        else:
            start = 0
    return str1+str2[start:]
