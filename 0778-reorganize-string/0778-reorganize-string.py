class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        count_s = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count_s.items()]
        heapq.heapify(maxHeap)
        prev = None

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            cnt, char = heapq.heappop(maxHeap)

            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev=None

            if cnt != 0:
                prev = [cnt, char]

        return res



        