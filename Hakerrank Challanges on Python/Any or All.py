def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)

    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

    
si=int(input())
lis=list(map(int,input().split()))
flg=False
if all ( i>0 for i in lis):
    if any(is_palindrome(j) for j in lis):
        flg=True
        
if flg:
    print("True")
else:
    print("False")

        
