def has_33(nums):
    for i,num in enumerate(nums):
        if nums[i]==3 and nums[i+1]==3:
                   return True
    return False