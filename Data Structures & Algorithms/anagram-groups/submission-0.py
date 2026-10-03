class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_list = []
        dictionary_of_anagrams  = {}
        for string in strs:
            count_list = [0]*26 # list containing the count for 26 alphabets
            string = string.lower()
            for char in string:
                count_list[ord(char)-97] +=1
            count_list = "-".join(str(x) for x in count_list)
            if count_list in dictionary_of_anagrams.keys():
                dictionary_of_anagrams[count_list].append(string)
            else:
                dictionary_of_anagrams[count_list] = [string]
        for v in dictionary_of_anagrams.values():
            return_list.append(v)
        return return_list