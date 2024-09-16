times = eval(input())
for i in range(times):
   num = input().rstrip().split(' ')
   

   if(num[0] == num[1] == num[2] ):
      print("Yes")

   else:
      print("No")
