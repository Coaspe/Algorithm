class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Create a set of words for fast lookup
        word_set = set(wordDict)
        # Create a memoization dictionary to store previously calculated results
        memo = {}

        # Define a recursive function to find all possible sentences
        def dfs(s):
            # If the current string s has already been calculated, return the result
            if s in memo:
                return memo[s]

            # If the string s is empty, return an empty list
            if not s:
                return []

            # Initialize the result list
            res = []

            # Iterate over all possible splits of the string s
            for i in range(1, len(s) + 1):
                # If the left part of the split is a valid word
                if s[:i] in word_set:
                    # Recursively find all possible sentences for the right part of the split
                    right_sents = dfs(s[i:])
                    # If there are any possible sentences for the right part of the split
                    if right_sents:
                        # Append the current word and all possible sentences for the right part of the split
                        for right_sent in right_sents:
                            res.append(s[:i] + " " + right_sent)
                    # If there are no possible sentences for the right part of the split, but the right part is empty
                    elif not s[i:]:
                        # Append just the current word
                        res.append(s[:i])

            # Store the result for the current string s in the memoization dictionary and return it
            memo[s] = res
            return res

        # Call the recursive function to find all possible sentences for the input string s
        return dfs(s)
