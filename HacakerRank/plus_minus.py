### plus minus 
 def plusMinus(arr):
     pos=0
     neg=0
     neu=0
     for i in range(len(arr)):
         if(arr[i]>0):
             pos+=1
         elif(arr[i]==0):
             neu+=1
         else:
             neg+=1
     print(pos/len(arr))
     print(neg/len(arr))
     print(neu/len(arr))


 plusMinus([-4, 3 ,-9 ,0 ,4 ,1])
