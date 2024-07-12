# func_calculate_median.py
def func_calculate_median(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    if length % 2 == 0:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[length // 2]

print(func_calculate_median([1, 2, 3, 4, 5]))
