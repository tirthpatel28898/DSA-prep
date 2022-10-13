class Solution:
       
    def encode(self, strs):
        """method to encode a list of strings to a single string

        Args:
            strs (list): a list of strings

        Returns:
            str: encodes a list of strings to a single string.
        """        
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, str):
        """method to decode a string to list of strings

        Args:
            str (_type_): a string

        Returns:
            list: decodes a single string to list of strings
        """        
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j+1 : j+1+length])
            i = j + 1 + length
        return res