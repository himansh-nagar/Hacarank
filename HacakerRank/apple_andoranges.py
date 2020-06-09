############################     apples and oranges

def countApplesAndOranges(s, t, a, b, apples, oranges):
    fruits_in_sam_house=[]
    total_apple_in_sam_house,total_orange_in_sam_house=0,0
    d1,d2=[],[]
    for apple in apples:
        D=0
        D=a+apple
        d1.append(D)
    for orange in oranges:
        D2=0
        D2=b+orange
        d2.append(D2)
    for i in d1:
        if i>=s and i<=t:
            total_apple_in_sam_house+=1
    for j in d2:
        if j>=s and j<=t:
            total_orange_in_sam_house+=1
    # fruits_in_sam_house.append(total_apple_in_sam_house)
    # fruits_in_sam_house.append(total_orange_in_sam_house)
    print(total_apple_in_sam_house)
    print(total_orange_in_sam_house)


countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])