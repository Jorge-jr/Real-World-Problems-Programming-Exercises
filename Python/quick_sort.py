from random import randint

unsorted_list = [randint(-100, 100) for _ in range(10)]


def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


def quick_sort(list):
    if len(list) == 0:
        return list
    pivot = list[0]
    first = quick_sort([smaller for smaller in list[1:] if smaller <= pivot])
    last = quick_sort([greater for greater in list[1:] if greater > pivot])
    return first + [pivot] + last


print(bubble_sort(unsorted_list))
