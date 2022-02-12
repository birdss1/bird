n=10
arr=[1,2,3,4,5,6,7,8,9,10]
k=8
print(arr)

low=0
high=n-1
res=-1
print(low,high)
while(low<=high):
    mid=low+(high-low//2)
    if arr[mid]==k:
        res=mid
    elif arr[mid]<k:
        low=mid+1
    elif arr[mid]>k:
        high=mid-1

print(res)