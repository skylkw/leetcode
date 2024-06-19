from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = defaultdict(int)
        for bill in bills:
            money[bill] += 1
            if bill == 10:
                if money[5] > 0:
                    money[5] -= 1
                else:
                    return False
            elif bill == 20:
                if money[10] > 0 and money[5] > 0:
                    money[10] -= 1
                    money[5] -= 1
                else:
                    if money[5] > 2:
                        money[5] -= 3
                    else:
                        return False
        return True
