class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans = []

        for p in path:
            if not p or p == ".":
                continue
            elif p == "..":
                if ans:
                    ans.pop()
                continue

            ans.append(p)

        return "/" + "/".join(ans)
