# 0 1 1 2 3....
fn = 0
sn = 1
number = int(input("Enter your number:"))
if number>=1:
    print(fn)
if number>1:
    print(sn)
for x in range(0,number-2):
    sum = fn + sn
    fn = sn
    sn = sum 
    print(sum)

   
