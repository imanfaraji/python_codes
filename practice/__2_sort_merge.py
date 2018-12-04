# merge sort

# 1. getmid and placemid
# 2. mergesort left
# 3. mergesort right

DEBUG = True
def log(s):
    if DEBUG:
        print(s)

def merge(l_lst, r_lst):
    l = 0
    r = 0
    ret_lst = []
    while l < len(l_lst) and r < len(r_lst):
        if l_lst[l] < r_lst[r]:
            ret_lst.append(l_lst[l])
            l += 1
        else:
            ret_lst.append(r_lst[r])
            r += 1

    if l < len(l_lst):
        ret_lst = ret_lst + l_lst[l:]
    if r < len(r_lst):
        ret_lst = ret_lst + r_lst[r:]
    return ret_lst

def mergesort(mylst):
# termination condition
    lst_size = len(mylst)
    if lst_size <=1:
        return mylst
# recursive part
    else:
        m = int(lst_size/2)
        left = mergesort(mylst[0:m])
        right = mergesort(mylst[m:])
        retlst = merge(left, right)
    return retlst

print()
lst = [3,5,6,2,11,9,1,3,7,10,4]
print(lst)
print("sorted array:")
lst_sorted = mergesort(lst)
print(lst_sorted)
