### miniMaxSum

def miniMaxSum(arr):
    num_list=[]
    for i in arr:
        new_arr=arr.copy()
        new_arr.remove(i)
        SUM=sum(new_arr)
        num_list.append(SUM)
    print(min(num_list),max(num_list))
    
miniMaxSum([1,1,1])