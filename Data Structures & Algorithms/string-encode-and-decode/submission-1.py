class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""  # enmpty string
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []  # empty list to store strings
        i = 0  # pointer for position
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length  # starts from where the next string will begin
        return res
