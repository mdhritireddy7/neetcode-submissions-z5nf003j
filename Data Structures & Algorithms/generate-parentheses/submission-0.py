class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        options = ["(", ")"]

        def valid(valid_paren, opens_so_far, closes_so_far):
            if len(valid_paren) == 2*n:
                result.append(valid_paren)
                return

            if opens_so_far < n:
                valid(valid_paren + options[0], opens_so_far + 1, closes_so_far)
            
            if opens_so_far > closes_so_far:
                valid(valid_paren + options[1], opens_so_far, closes_so_far + 1)

        valid("", 0, 0)

        return result
        