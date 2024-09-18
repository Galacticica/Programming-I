import statistics
nums = []
average = None

while True:
    num = input()
    if num == "":
        break
    nums.append(int(num))

if len(nums) == 0:
    pass
else:
    print(statistics.mean(nums))