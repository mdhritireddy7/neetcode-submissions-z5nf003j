class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for ls in strs:
            res += str(len(ls)) + ';' + ls

        return res

    def decode(self, s: str) -> List[str]:
        rsult, i = [], 0

        while i < len(s):
            j = i
            while s[j] != ";":
                j+= 1
            length = int(s[i:j])
            rsult.append(s[j+1:j+1+length])
            i = j + 1 + length

        return rsult

