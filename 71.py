import unittest
class Solution:
    def simplifyPath(self, path: str) -> str:
        statck = []
        for dir in path.split("/"):
            if dir not in [".", "..",""]:
                statck.append(dir)
            elif dir == "..":
                if statck:
                    statck.pop()
        return '/'+'/'.join(statck)