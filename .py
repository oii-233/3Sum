class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        adi=set()
        length=len(nums)
        left=0
        right=length-1
        add=left+1
        while left<length-2 and right>=0:
            result=nums[left]+nums[add]+nums[right]
            if result == 0:
                adi.add((nums[left],nums[add],nums[right]))
                add+=1
                right-=1
            elif result< 0:
                add+=1
            else:
                right-=1
            if add>=right:
                left+=1
                add=left+1
                right=length-1

        return [list(i) for i in adi]


