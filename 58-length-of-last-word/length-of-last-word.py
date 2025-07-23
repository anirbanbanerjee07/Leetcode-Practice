class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
          i -= 1
        lastIndex = i
        while i >= 0 and s[i] != ' ':
          i -= 1

        return lastIndex - i