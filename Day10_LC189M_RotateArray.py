def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k%n
    new = nums[n-k:n] + nums[0:n-k]
    for i in range(n):
        nums[i] = new[i]

nums = [1,2]
k = 7
rotate(nums, k)
print(nums)