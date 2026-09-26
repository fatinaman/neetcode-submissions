class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] +=1
        for char in t:
            if char not in dict:
                return False
            else:
                if dict[char]>0:
                    dict[char] -=1
                else:
                    return False
        checkSum = 0
        for value in dict.values():
            checkSum += value

        if checkSum == 0: return True
        else: return False