def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (right+left)//2
            need = 1
            curr = 0
            for each in weights:
                if curr + each > mid:
                    need += 1
                    curr = 0
                curr += each
            if need > days:
                left = mid + 1
            else:
                right = mid
        return left