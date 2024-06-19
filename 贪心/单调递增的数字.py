class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num = list(str(n))
        for i in range(len(num) - 2, 0, -1):
            if num[i] > num[i + 1]:
                num[i] = str(int(num[i]) - 1)
                num[i + 1] = "9"
        return int(("".join(num)).lstrip("0"))
