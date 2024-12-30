class Solution(object):
    def reverseWords(self, s):
        ls = s.split()
        ls.reverse()

        return ' '.join(ls)