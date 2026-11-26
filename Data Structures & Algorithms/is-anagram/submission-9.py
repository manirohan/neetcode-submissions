class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif set(s) != set(s).union(set(t)):
            return False

        
        def dict(s:str):
            s1 = {}
            for item in s:
                if item in s1.keys():
                    s1[item] = s1[item] + 1
                else:
                    s1[item] = 1
            return s1
        s1 = dict(s)
        t1 = dict(t)

        for item in set(s).union(set(t)):
            if item not in set(t):
                return False
            elif s1[item]!=t1[item]:
                return False
        return True
