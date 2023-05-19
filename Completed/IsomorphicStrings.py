'''
#205 Isomorphic Strings
Difficulty: Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Status: Completed
Notes: Took me some time for a goofy issue, dic.update was an issue for some reason

'''
def isIsomorphic(s: str, t: str) -> bool:
        dic,dic2 = {},{}
        for i,j in zip(s,t):
            if (i in dic and dic[i] != j) or (j in dic2 and dic2[j] != i):
                return False
            dic[i] = j
            dic2[j] = i
        return True
print(isIsomorphic("badc","baba"))