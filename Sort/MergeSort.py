# Author   : Orange
# Coding   : Utf-8
# @Time    : 2021/11/3 9:20 下午
# @File    : MergeSort.py
import copy


def merge(nums, begin, pivot, end):
	tempA = copy.deepcopy(nums[begin: pivot + 1])
	tempB = copy.deepcopy(nums[pivot + 1: end + 1])

	tempB = tempB + [float('inf')]
	tempA = tempA + [float('inf')]
	i = j = 0
	for index in range(begin, end + 1):
		if tempB[i] > tempA[j]:
			nums[index] = tempA[j]
			j += 1
		else:
			nums[index] = tempB[i]
			i += 1


def mergesort(nums, begin, end):
	if begin < end:
		pivot = (begin + end) // 2
		mergesort(nums, begin, pivot)
		mergesort(nums, pivot + 1, end)

		merge(nums, begin, pivot, end)


if __name__ == '__main__':
	nums = [5, 4, 3, 6, 8, 1, 2]
	# merge(nums, 0, 7 // 2, 6)
	# print(nums)

	mergesort(nums, 0, len(nums) - 1)
	print(nums)


