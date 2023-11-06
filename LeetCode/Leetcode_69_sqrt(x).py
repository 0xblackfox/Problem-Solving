# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return int(x ** 0.5)



# LeetCode - 69  =>  Sqrt(x) 

def binary_Search_sqrt(x):
    
    if x == 0 or x == 1:
        return x
    
    first = 1
    last = x
    
    while first <= last:
        
        mid = (first + last )//2
        mid_sqr = mid * mid

        if mid_sqr == x:
            return mid
        
        if mid_sqr < x:
            first = mid +1
            ans = mid
        
        else:
            last = mid -1
    return ans

        
find_root = binary_Search_sqrt(int(input("enter any number: ")))
print(find_root)
        