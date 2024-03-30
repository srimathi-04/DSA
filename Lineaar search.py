def binary_search(lo,hi,con):
    while lo <= hi:
        mid = (lo+hi)//2
        res = con(mid)
        if res == ' found':
            return mid
        elif res== 'left':
            hi = mid-1
        else:
            lo = mid+1
    return -1
def first_position(nums,target):
    def con(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return ' found'
        elif nums[mid] <target:
            return 'right'
        else:
            return ' left'
    return binary_search(0,len(nums)-1,con)
def last_position(nums,target):
    def con(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return ' found'
        elif nums[mid] < target:
            return 'right'
        else:
            return ' left'
    return binary_search(0,len(nums)-1,con)
def fir_last_pos(nums,target):
    return first_position(nums,target),last_position(nums,target)