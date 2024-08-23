class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(start, path):
            # If the combination is of the desired length
            if len(path) == k:
                result.append(path[:])  # Append a copy of path
                return
            # Explore further combinations
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # Remove the last element to backtrack
        
        result = []
        backtrack(1, [])
        return result

# Example usage
solution = Solution()
print(solution.combine(4, 2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(solution.combine(1, 1))  # Output: [[1]]
