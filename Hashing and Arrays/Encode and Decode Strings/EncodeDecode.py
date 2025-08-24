# Problem Link : https://neetcode.io/problems/string-encode-and-decode?list=neetcode250
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        return res    

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res


if __name__ == "__main__":
    sol = Solution()

    # Example input
    strs = ["leet", "code", "hello", "world"]

    # Encode
    encoded = sol.encode(strs)
    print("Encoded:", encoded)

    # Decode
    decoded = sol.decode(encoded)
    print("Decoded:", decoded)
