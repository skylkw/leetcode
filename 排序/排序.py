# 选择排序
def select_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]


# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 插入排序
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break


# 归并排序
def merge_sort(arr):
    # 左闭右开
    def merge(arr, left, mid, right):
        temp = [0] * (right - left)
        i, j, k = left, mid, 0
        while i < mid and j < right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        if i < mid:
            temp[k:] = arr[i:mid]
        if j < right:
            temp[k:] = arr[j:right]
        arr[left:right] = temp

    def merge_sort(arr, left, right):
        if right - left <= 1:
            return
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)

    merge_sort(arr, 0, len(arr))


# 快速排序
def quick_sort(arr):
    # 左闭右闭
    def partition(arr, left, right):
        pivot = arr[left]
        l = left
        r = right
        i = left
        while i <= r:
            if arr[i] < pivot:
                arr[l], arr[i] = arr[i], arr[l]
                i += 1
                l += 1
            elif arr[i] > pivot:
                arr[r], arr[i] = arr[i], arr[r]
                r -= 1
            else:
                i += 1
        return l, r
    
    def quick_sort(arr, left, right):
        if left >= right:
            return
        l, r = partition(arr, left, right)
        quick_sort(arr, left, l - 1)
        quick_sort(arr, r + 1, right)
    
    quick_sort(arr, 0, len(arr) - 1)




if __name__ == "__main__":
    arr = [1, 3, 2, 5, 4, 4, 10]
    # select_sort(arr)
    # bubble_sort(arr)
    # insert_sort(arr)
    # merge_sort(arr)
    quick_sort(arr)
    print(arr)
