import statistics
nums = []

while True:
    num = input()
    if num == "":
        break
    nums.append(int(num))

print(statistics.mean(nums))