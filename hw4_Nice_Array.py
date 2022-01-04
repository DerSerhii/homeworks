def is_nice(arr):
    for n in arr:
        if (n - 1) not in arr and (n + 1) not in arr:
            return False
    return True if arr else False
