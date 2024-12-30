class Solution(object):
    def reverseVowels(self, s):
        wanted_letters = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        s_list = list(s)  
        vowels = [char for char in s_list if char in wanted_letters]  
        vowels.reverse()  
        index = 0
        
        for i in range(len(s_list)):
            if s_list[i] in wanted_letters:  
                s_list[i] = vowels[index]  
                index += 1
        
        return ''.join(s_list) 