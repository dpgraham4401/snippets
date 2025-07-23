"""
Given 2 strings, return a boolean indicating whether they are anagrams of each other.
an anagram is a string that contains the exact same characters as another string, but 
the orders can be different.
"""

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_map: dict = {}
    t_map: dict = {}
    for i in range(len(s)):
        s_map[s[i]] = s_map.get(s[i], 0) + 1
        t_map[t[i]] = t_map.get(t[i], 0) + 1
    return s_map == t_map


# Example usage
s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))  # True

s1 = "hello"
s2 = "world"
print(is_anagram(s1, s2))  # False