# Author   : Orange
# Coding   : Utf-8
# @Time    : 2021/11/3 2:28 下午
# @File    : QuickSort.py

# 快排应该是 面试时候最长考察的排序算法了吧
# 快排 的代码 算法导论给出的最为简洁
#

def QuickSort(nums, begin, end):
	if begin < end:
		pivot = Partition(nums, begin, end)
		QuickSort(nums, begin, pivot - 1)
		QuickSort(nums, pivot + 1, end)


def Partition(nums, begin, end):
	tmp = nums[end]
	i = begin - 1
	for j in range(begin, end):
		if nums[j] <= tmp:
			i = i + 1
			nums[i], nums[j] = nums[j], nums[i]
	nums[i + 1], nums[end] = nums[end], nums[i + 1]
	return i + 1


if __name__ == '__main__':
	nums = [3, 2, 4, 5, 6, 1]
	QuickSort(nums, 0, len(nums) - 1)
	print(nums)
