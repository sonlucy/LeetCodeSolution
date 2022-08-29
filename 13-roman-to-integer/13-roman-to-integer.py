class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
#         문자열에서 각 문자를 추출하여 덧셈(뺄셈) 하기.

       # for i in range(len(s))
    
        
#         a=[0 for i in range(len(s))]
#         res=0
        
        
#         for i in range (0,len(s)):
#             if s[i]==I:
#                 a[i]=1
#             elif s[i]==V:
#                 a[i]=5
#             elif s[i]==X:
#                 a[i]=10
#             elif s[i]==L:
#                 a[i]=50
#             elif s[i]==C:
#                 a[i]=100
#             elif s[i]==D:
#                 a[i]=500
#             else:
#                 a[i]=1000
                
#         for i in range(len(a)):
#             if a[i]<a[i+1]: 
#                 res+= a[i+1]-a[i]
#             else: 
#                 res+=a[i]

# 4, 9  -> IV(1,5),  IX(1,10) 
# 40,90  -> XL(10,50), XC(10,100)
# 400, 900 -> CD(100,500), CM(100,1000)

        roman2value={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
            
        value=0
        temp=''
        cursor=0
        while cursor<len(s):
            if (cursor+1)!=len(s) and s[cursor]+s[cursor+1] in roman2value:  # Check current character and next character
                value+=roman2value[s[cursor]+s[cursor+1]]
                cursor+=2
            else:  #마지막 로마숫자?
                value+=roman2value[s[cursor]]
                cursor+=1
                
            
        
        return value
