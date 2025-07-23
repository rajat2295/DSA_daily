class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out_dict = defaultdict(list)
        out_list =[]
        for word in strs:
            one_hot = [0]*26
            for letter in word:
                one_hot[ord(letter)-ord('a')] +=1
            key = tuple(one_hot)
            out_dict[key].append(word)
        for key in out_dict:
            out_list.append(out_dict[key])
        return (out_list)
            


        
