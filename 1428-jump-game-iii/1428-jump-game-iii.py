from collections import deque
from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True

            # Mark as visited by setting arr[curr] to -1
            if arr[curr] < 0:
                continue
            
            # If we can move to curr + arr[curr] within bounds
            if (curr + arr[curr]) < len(arr):
                q.append(curr + arr[curr])

            # If we can move to curr - arr[curr] within bounds
            if (curr - arr[curr]) >= 0:
                q.append(curr - arr[curr])
            
            # Mark this index as visited by negating the value
            arr[curr] = -arr[curr]
            
        return False

        