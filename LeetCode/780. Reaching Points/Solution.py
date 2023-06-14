class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:

        while tx >= sx and ty >= sy:
            if ty > tx:
                if tx > sx:
                    ty %= tx
                elif tx == sx:
                    return (ty - sy) % tx == 0
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                elif ty == sy:
                    return (tx - sx) % ty == 0
            else:
                break

        return (ty == sy and tx == sx)
