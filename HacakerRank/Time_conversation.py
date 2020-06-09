###################  Time conversation

 def timeConversion(s):
     S=int(s[:2])
     if "AM" in s and S==12:
         print("00"+s[2:8])
     elif S==12 and "PM" in s:
         print(s[:8])
     elif "AM" in s and S!=12:
        print(s[:8])

     else:
         S=str(S+12)
         print(S+s[2:8])

 timeConversion("03:05:45AM")
