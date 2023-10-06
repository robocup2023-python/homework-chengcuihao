"""
原因是list可变，导致每次pop后列表元素的索引发生变化，最终导致
删除了非预期元素并且索引超出列表范围，修改如下:
"""
if __name__ == "__main__":
    lst = list(range(1000))
    idx = 0
    while idx < len(lst):
        if lst[idx] % 2 == 1:
            lst.pop(idx)
            idx -= 1
        idx += 1
    print(lst)
