# Author   : Orange
# Coding   : Utf-8
# @Time    : 2021/11/3 3:19 下午
# @File    : HeapSort.py

# 调整为最大堆 MAX-HEAPIFY
def modify(currIndex, MaxLength, nums):
    while currIndex < MaxLength:
        if 2 * currIndex + 1 < MaxLength and nums[2 * currIndex + 1] > nums[currIndex]:
            largest = 2 * currIndex + 1
        else:
            largest = currIndex

        if 2 * currIndex + 2 < MaxLength and nums[2 * currIndex + 2] > nums[largest]:
            largest = 2 * currIndex + 2

        if largest == currIndex:
            break
        else:
            nums[largest], nums[currIndex] = nums[currIndex], nums[largest]
            currIndex = largest


def buildMaxHEAPIFY(nums):
    i = len(nums) // 2 - 1
    while i >= 0:
        modify(i, len(nums), nums)
        i -= 1


if __name__ == '__main__':
    A = [1,2,3,4,5]
    buildMaxHEAPIFY(A)
    print(A)