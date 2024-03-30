def rot_pos(nums):
  pos = 0
  while pos < len(nums):
    if pos > 0 and nums[pos] < nums[pos-1]:
        return pos
    pos +=1
  return 0
num =  [3,5,7,8,10,18,20,23,25]
nums = [10,18,20,23,25,3,5,7,8] 
print(rot_pos(nums))