####    digonal sum
digonal=[[1,2,3,5],
         [4,5,6,4],
         [7,8,9,3]
        ]
def digonaldiffernce(arr):
    SUM1=0
    SUM2=0
    j=0
    for i in arr:
        SUM1+=i[j]
        SUM2+=i[(len(i)-1)-j]
        j+=1
    return abs(SUM1-SUM2)
            

print(digonaldiffernce(digonal))
