def bubble_sorting(lst):
	length_of_lst = len(lst) - 1
	ready = False
	while not ready:
		ready = True
		for i in range(length_of_lst):
			if lst[i] > lst[i + 1]:
				ready = False
				lst[i], lst[i + 1] = lst[i + 1], lst[i]
	return lst
