'''В данном модуле храянятся функции с разными видами сортировки'''


def bubble_sort(lst):
	'''Функция сортировки пузырьком
    :param lst: list
    :return list
    '''
	last_elem_index = len(lst) - 1
	for passNo in range(last_elem_index, 0, -1):
		for idx in range(passNo):
			if lst[idx] > lst[idx + 1]:
				lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
	return lst


def counting_sort(lst, largest):
	'''Функция сортировки подсчетом.
    :param lst: list
    :param largest: float
    :return list
    '''
	c = [0]*(largest + 1)
	for i in range(len(lst)):
		c[lst[i]] = c[lst[i]] + 1
	c[0] = c[0] - 1
	for i in range(1, largest + 1):
		c[i] = c[i] + c[i - 1]
		result = [None]*len(lst)
	for x in reversed(lst):
		result[c[x]] = x
		c[x] = c[x] - 1

	return result


def heapify(lst, n, i):
	'''Функция преоброзовывания в двоичную кучу, где lst список, i корневой индекс, n размер кучи
	:param lst: arrow
	:param i: int
	:param n: int
	'''
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2

	if left < n and lst[i] < lst[left]: #проверка существования левого элемента который больше корня
		largest = left
	if right < n and lst[largest] < lst[right]: #аналогичная проверка для правого элемента
		largest = right
	if largest != i:
		lst[i], lst[largest] = lst[largest], lst[i] #меняем корень если того требуется
		heapify(lst, n, largest) #применяем функцию к корневому элементу


def heap_sort(lst):
	'''Сама функция Пирамидальная сортировка(Heap Sort).
	:param lst: list
	:return list
	'''
	n = len(lst)
	for i in range(n, -1, -1):
		heapify(lst, n, i)
	for i in range(n - 1, 0, -1):
		lst[i], lst[0] = lst[0], lst[i] #меняем элементы местами
		heapify(lst, i, 0)


def marge_sort(lst):
	'''Сортировка слиянием
	:param lst: list
	:return list
	'''
	if len(lst) > 1:
		mid = len(lst) // 2 #делим список пополам
		left = lst[:mid]
		right = lst[mid:]
		marge_sort(left)# применяем функцию к левой и правой частям
		marge_sort(right)

		a = 0
		b = 0
		c = 0
		while a < len(left) and b < len(right):
			if left[a] < right[b]:
				lst[c] = left[a]
				a = a + 1
			else:
				lst[c] = right[b]
				b = b + 1
			c = c + 1
		while a < len(left):
			lst[c] = left[a]
			a = a + 1
			c = c + 1
		while b < len(right):
			lst[c] = right[b]
			b = b + 1
			c = c + 1
		return lst


def quicksort(lst):
	'''Функция быстрой сортировки
	:param lst: list
	:return list
	'''
	#Если длина списка менее двух, то он является отсортированным
	if len(lst) < 2:
		return lst
	else:
		#Опорный элемент
		pivot = lst[0]
		less = [i for i in lst[1:] if i < pivot] #подсписок элементов меньше опорного
		greater = [i for i in lst[1:] if i > pivot] #подсписок элементов больше опроного
		return quicksort(less) + [pivot] + quicksort(greater)


def radix_sort(lst):
	'''Функция поразрядной сортировка(Radix Sort)
	:param lst: list
	:return list
	'''
	# Находим длину самого длинного числа
	max_digit = max([len(str(num)) for num in lst])
	# Система счисления
	radix = 10
	# Создаём промежуточные списки
	lists = [[] for i in range(radix)]
	# Перебираем все разряды, начиная с нулевого
	for i in range(0, max_digit):
		# перебираем все элементы в списке
		for elem in lst:
			# получаем цифру текущего разряда, для каждого числа
			digit = (elem // radix ** i) % radix
			# добавляем число в промежуточный массив
			lists[digit].append(elem)
		# собираем в исходный список нулевые значения
		lst = [x for queue in lists for x in queue]
		# очищаем промежуточный списко
		lists = [[] for i in range(radix)]
	return lst