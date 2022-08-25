class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        """자릿수 구하기"""
        """ 
        int digit=0
        while x:
            x //=10
            digit++
            
        int reverse_x =0
        while
        reverse_x += (x%10) * 10^(digit-1)"""
    

    
        if x<0:
            return False
        else:
            return x == int( str(x)[::-1] )  #문자열 슬라이싱 사용하기 위해 문자열 형태로 바꾼다음 문자열 역순으로 해주고 int형인 x와 비교하기위해 다시 int형으로 변경해서 x와 같으면 true 다르면 false
  


#          if x<0 or x%10==0 and x!=0:
#             return False

#         if x==0:
#             return True
    
    
#         digit=0
#         while x!=0:
#             x //=10  #123 ->12  ->1  ->0
#             digit+=1  #3
            
#         reverse_x=0
#         while x!=0:
#             reverse_x += x%10 * (10**(digit-1)) #300 ->320 ->321
#             digit -= 1  #2  ->1 ->0 
#             x //=10 #123 -> #12->1-> 0


        
#         if x==reverse_x:
#             return True 
#         else:
#             return False