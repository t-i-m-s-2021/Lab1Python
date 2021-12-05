sum=0

def adder(*nums):
    if (len(nums)>0):
        sum=nums[0]
        for n in range(1,len(nums)):
            try:
                sum + nums[n]
            except TypeError as e:
                raise e
            else:
                sum += nums[n]
        print("Сумма =", sum)
    return 0

adder(1,23,-1,2,9.6)    







    



        




