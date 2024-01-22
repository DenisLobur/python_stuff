class Solution:
    # Brute force O(n**n)
    def twoSumBrute(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    print([i, j])
                    return [i, j]

    # Hash Table O(1) to O(n)
    def twoSumHashTable(self, nums: list[int], target: int) -> list[int]:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
            print(hash_table)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table and hash_table[complement] != i:
                return [i, hash_table[complement]]


if __name__ == '__main__':
    solution = Solution()
    print("Brute Force: \n")
    solution.twoSumBrute([2, 7, 11, 15], 18)
    print("Hash Table: \n")
    solution.twoSumHashTable([2, 7, 11, 15], 18)
