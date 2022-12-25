class Solution(object):
    def parseTernary(self, expression):
        st = []
        for c in expression[::-1]:
            st.append(c)
            if len(st) >= 2 and st[-2] == '?':
                boolean, _, t, _, f = st.pop(), st.pop(), st.pop(), st.pop(), st.pop()
                st.append(t if boolean == 'T' else f)
        return st[0]
