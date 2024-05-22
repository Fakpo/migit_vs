import time
c = 0
start = time.time()
array = [4,6,32,123,44,45]

def swap(a: int, b: int):         #funcion que intercambia valores
    return b,a   

#print (array)

for i in range(0, len(array)-1):
    for j in range(i + 1, len(array)):
        c += 1
        if array[i] > array[j] :
            array[i],array[j] = swap(array[i],array[j])


end = time.time()
#print (array)
print (start)
print (end)
print (f"{(end - start) * 1000}ms")
print (f"{c} veces")

