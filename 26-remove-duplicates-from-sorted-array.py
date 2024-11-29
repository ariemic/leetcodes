def removeDuplicates(nums) -> int:
        k = 0 #number of unique elements
        n = len(nums)
        # we need to transform nums list such that unique element occupy k first places in nums list in same at input order
        left = nums[0]
        right = nums[n-1]
        insert_pointer = 0

        while left < right:
            left_unique, right_unique = False, False
            if left < n and nums[left] != nums[left+1]:
                # left is unique
                insert_pointer += 1
                left += 1
                left_unique = True
                k += 1
            else:
                left +=1 
                

            if right > 0 and nums[right] != nums[right - 1]:
                # right is unique
                right_unique = True
                k += 1
            
            if right_unique and left_unique:
                while ()




nums = [1, 1, 1, 2, 3]