import random
def buble_sort(arr):
    flag = True
    per = 0
    compare = 0
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr)-1 - i):
            compare += 1
            if arr[j + 1] < arr[j]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                per += 1
                flag = False
        if flag:
            print('Array is sorted!!!')
            break
    print('number of swipe :', per)
    print('number of comparisons :', compare)
    return arr
n = 20
#array = [random.randint(1,n) for i in range(n)]
array = random.sample(range(1, n+1), n)
print('Початковий масив :', array)
sorted_array = buble_sort(array)
print('Відсортований  масив :', sorted_array)

