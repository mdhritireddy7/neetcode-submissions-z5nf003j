class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(string)

        l = 0

        for r in range(len(string)-1, -1, -1):
            if string[l] != string[r]:
                return False
            l += 1

        return True
        