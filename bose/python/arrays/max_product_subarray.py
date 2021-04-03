def maxProduct(nums):
    # maxProduct = nums[0]
    # prod_pos = 1
    # prod_neg = 1

    # for i in range(0,len(nums)):
    #     prod_pos*=nums[i]
    #     prod_neg*= nums[i]
    #     if prod_pos > prod_neg:
    #         if prod_pos>maxProduct:
    #             maxProduct = prod_pos
    #     else:
    #         if prod_neg > maxProduct:
    #             maxProduct = prod_neg
    #     if prod_pos < 1:
    #         prod_pos = 1
        
    # return maxProduct


    maxProduct = -99999

    left_arr=[0]*len(nums)
    right_arr=[0]*len(nums)


    prod = 1
    for i in range(0,len(nums)):
        prod*=nums[i]
        left_arr[i] = prod
        if prod==0:
            prod=1

    prod=1

    for i in range(len(nums)-1,-1,-1):
        prod*=nums[i]
        right_arr[i] = prod
        if prod==0:
            prod=1

    for i in range(0,len(nums)):
        maxProduct = max(maxProduct,left_arr[i],right_arr[i])

    print("Left array :: {}".format(left_arr))
    print("Right array :: {}".format(right_arr))

    return maxProduct
if __name__ == '__main__':
    nums = [-3,-1,-1]
    print(maxProduct(nums))
