num = int(input("Enter the Number:"))

def my_fact(num):
    if(num==1):
        return 1
    else:
        return num*my_fact(num-1)

print("%d! = %d" % (num, my_fact(num)))