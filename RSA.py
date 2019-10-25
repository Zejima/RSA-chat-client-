
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
#for more info look here: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
#will also be explained in class
def get_d(e, z):
    ###################################your code goes here#####################################
    #This Snippet is just an implemented algorithm of the Extended Euclidian Algorithm
    b=int(z)
    a=int(e)
    x=0
    y=1
    result = 0
    while result == 0:
        if a == 1:
            result = y
            break
        if a == 0:
            result = b
            break
        q=int(b/a)
        b=int(b-a*q)
        x=int(x+q*y)
        if b == 1:
            result= z-x
            break
        if b==0:
            result = a
            break
        q=int(a/b)
        a=int(a-b*q) 
        y=int(y+q*x)
    return result
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    e=593465 #e value specific to our 2 numbers
    n=p*q           #calculate n
    z=(p-1)*(q-1)   #calculate z
    d=get_d(e,z)    #run get d to find d
    return ((e, n), (d, n))#return the keypair(private,public)

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    cipher=pow(ord(plaintext),pk[0],pk[1]) #cipher = plaintext^e mod n
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    plain= chr(pow(ciphertext,pk[0], pk[1])) #plaintext= cipher^d mod n
    return ''.join(plain)
