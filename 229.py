from typing import List
from collections import Counter
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        threshold = math.ceil(len(nums)/3)

        return [k  for k, v in counter.items() if v>=threshold]

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1,1,1,3,3,2,2,2]))