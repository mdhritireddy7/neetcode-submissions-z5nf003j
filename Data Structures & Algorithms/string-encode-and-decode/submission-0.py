class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for ls in strs:
            res += ls
            res += ";"

        return res

    def decode(self, s: str) -> List[str]:
        rsult = []
        st = ""
        for c in s:
            if c != ';':
                st += c
            else:
                rsult.append(st)
                st = ""

        return rsult

