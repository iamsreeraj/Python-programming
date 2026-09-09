def febinacci(n):
    if n<=1:
        return n
    else:
        return febinacci(n-1)+febinacci(n-2)
        
for i in range(8):            
 print(febinacci(i))    
