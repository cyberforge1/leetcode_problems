def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # for i in range(0, len(nums) - 1):
        #     print('This is i', i)
        #     for j in range(1, len(nums)):
        #         print('This is j', j)
        #         print('This is nums[i]', nums[i])
        #         print('This is nums[j]', nums[j])
        #         if nums[i] + nums[j] == target and i != j:
        #             print('target found')
        #             return [i, j]

    
    
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = sorted_nums[left][0] + sorted_nums[right][0]

            if current_sum == target:
                return [sorted_nums[left][1], sorted_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []

print(twoSum([3, 2, 4], 6))
        
