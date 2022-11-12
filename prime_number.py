def is_prime(n):
    #any number below 2 is not a prime number
    if n<2:
        return False
    #we check that their in no number that can devide our number
    for i in range (2,n):
        if n%i==0:
            return False
    return True

num=5 #number of prime numbers we want
N=1   #to generate numbers
i=1   #to check if we have the right amount of prime numbers
#we increment N until we find the right amount of numbers
while i<num+1:
   if is_prime(N):
        print(N)
        print(i)
        i+=1 #we inrement i only when we find a prime number
   N+=1 