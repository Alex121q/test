print('hello world')
list01 = [9, 5, 8, 3, 99, 1, 23, 66]
for i in range(len(list01)-1):
    for j in range(len(list01)-i-1):
        if list01[j] > list01[j+1]:
            list01[j], list01[j+1] = list01[j+1], list01[j]
print(list01)
