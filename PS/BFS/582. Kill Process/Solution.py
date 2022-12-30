class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        answer = []
        # {parent: List[children]}
        counter = collections.defaultdict(list)

        # Init counter
        for idx, p in enumerate(ppid):
            counter[p].append(idx)
        stack = [*counter[kill]]

        # Iterate
        while stack:
            x = stack.pop()
            answer.append(pid[x])
            stack.extend(counter[pid[x]])

        return answer + [kill]
