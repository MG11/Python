def minSwaps(nums):
    # Code here
    my_dict = {}
    for i in range(len(nums)):
        my_dict[i] = i

    numsi = nums[:]
    nums.sort()
    print(numsi)
    print(nums)

    count = 0
    for i in range(len(nums)):
        if nums[i] == numsi[i]:
            continue
        else:
            index = my_dict[nums[i]]
            my_dict[numsi[i]] = index
            my_dict[numsi[index]] = i
            c = numsi[i]
            numsi[i] = numsi[index]
            numsi[index] = c
            count += 1
    return count


if __name__ == "__main__":
    print(minSwaps([7, 16, 14, 17, 6, 9, 5, 3, 18]))
