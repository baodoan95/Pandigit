# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product, we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and(1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n >1?

# Check if number is 1 to 9 pandigital
def isPan(x):
    l1 = []
    for i in str(x):
        if i == "0":
            return False
        else:
            l1.append(i)
    return True if len(set(l1)) == 9 and len(l1) == 9 else False


# Generate pandigital number from an int x and a provided array
def getPan(x, l1):
    ans = ""
    for i in l1:
        ans += str(x * i)
    return int(ans)


# largest pandigital number with provided integer and n
def largestPan(x, n):
    l1 = []
    panList = []
    for i in range(1, n + 1):
        l1.append(i)
        z = getPan(x, l1)
        if isPan(z):
            panList.append(z)
    return "No 1-9 pan digit found for this set of x and list of range n" if len(panList) == 0 else max(panList)


if __name__ == "__main__":
    print(largestPan(192, 3))  # test case 9 is int and x is range for list
