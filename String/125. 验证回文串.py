class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            # 两个循环找到左侧和右侧为字母或者数字的位置
            while left < len(s) - 1 and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1
            if left >= right:  # 判断移动过后的left right是否满足left在左，right在右的相对位置
                break
            else:
                if s[left] != s[right]:  # 如果左右指针所指不同，则肯定不构成回文
                    return False
                else:  # 左右指针各前进一步
                    left += 1
                    right -= 1
        return True

a = isPalindrome("a")
print(a)