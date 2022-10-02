crypt = list("51c49a1a00647b037f5f3d5c878eb656")

#crypt = list("3ea7")

nums = [9]

for c in crypt:
    nums = nums + [int(c, 16)]
print(nums)

flag = ""
for i, n in enumerate(nums[1:], 1):
    flag += hex(((n+16) - nums[i-1]) & 0x0f)[2:]

print(flag)

# lic ccb85179606e3453486a4a87cf16dbf1
# flag flag{clock_math_too_hard}
