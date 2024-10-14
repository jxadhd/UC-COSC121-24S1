def threshold_filter(readings, threshold):
    """Updates list to Q10 spec"""
    for num in range(len(readings)):
        if readings[num] < 0:
            readings[num] = 0
        elif readings[num] >= 0 and readings[num] <= threshold:
            readings[num] = threshold

#Test
alist = [0, -3, 0, 3, 5, 7, 9, 8, 2, 0, -2, 8, 5]
ret = threshold_filter(alist, 2)
print(alist)
print(ret)