def reverse(arr,i,n):
    if i >= n/2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    reverse(arr,i+1,n)

arr=[1,2,3,4]
reverse(arr,0,len(arr))
# print(arr)

def palindrome(s,i,n) -> bool:
    if i >= n/2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return palindrome(s,i+1,n)

string = "asdmadsdamdsa"
result = palindrome(string, 0, len(string))
print(result)