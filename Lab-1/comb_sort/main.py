import random
def comb_sort(arr):
    com = 0
    per = 0
    step = int(len(arr) / 1.247)
    flag = True
    while step >= 1:
        for i in range(len(arr) - step):
            com += 1
            if arr[i + step] < arr[i]:
                tmp = arr[i + step]
                arr[i + step] = arr[i]
                arr[i] = tmp
                per += 1
                flag = False
        if flag:
            break
        step = int(step / 1.247)
    print('number of swipe :', per)
    print('number of comparisons :', com)
    return arr
n = 20
array = [random.randint(1,n) for i in range(n)]
print('Початковий масив :', array)
sorted_array = comb_sort(array)
print('Відсортований  масив :', sorted_array)
#array = random.sample(range(1, n + 1), n)
