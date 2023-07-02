# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!
myList1 = [4,6,2,1,9,63,-134,566] 
myList2 = [-52, 56, 30, 29, -54, 0, -110]
myList3 = [42, 54, 65, 87, 0]
myList4 = [5]

def maximum(a):
	max_n = a[0]
	for n in a:
		if n > max_n:
			max_n = n
	return max_n

def minimum(a):
	min_n = a[0]
	for n in a:
		if n < min_n:
			min_n = n
	return min_n

print('max = ', maximum(myList1),', min = ', minimum(myList1))
print('max = ', maximum(myList2),', min = ', minimum(myList2))
print('max = ', maximum(myList3),', min = ', minimum(myList3))
print('max = ', maximum(myList4),', min = ', minimum(myList4))
