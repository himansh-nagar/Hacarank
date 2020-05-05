######      Birthday Cake Candles
def birthdayCakeCandles(ar):
    blown_candle=0
    maxi=max(ar)
    for i in ar:
        if i==maxi:
            blown_candle+=1
    print(blown_candle)
birthdayCakeCandles([3,2,1,3])