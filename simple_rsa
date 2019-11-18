try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass 

p = int (input('Enter the prim p: ' ))
q = int (input('Enter the prime q: ' ))
print ("\nYou have taken p : {0} , q : {1} \n".format(p,q))
n = p * q
print ("Calculating Totient.... \n")
toi = (p - 1) * (q-1)
print ("The Totient for {0} is {1} \n".format(n,toi))


def gcd(a,b):
    while b != 0 :
        c = a % b
        a = b
        b = c
    return a
def modulur_multiple_invr(a,m):
    for x in range(1,m):
        if (a * x ) % m == 1:
            return x
    return None
def avlPrime(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modulur_multiple_invr(x,toi) != None:
            l.append(x)
    for x in l:
        if x == modulur_multiple_invr(x,toi):
            l.remove(x)
    return l

print(avlPrime(toi))
print("Pick a PrimeNumber(e) :")
e = int(input())
d = modulur_multiple_invr(e,toi)
print("\nPublicKey pair: ({0},{1}) \n".format(e,n))
print("PrivateKey pair: ({0},{1}) \n".format(d,n))


def enc_char(m):
    c = modulur_multiple_invr(m ** e , n)
    if c == None:
        print("Inverse is not in the range")
    return c

def dyc_char(dr):
    dy = modulur_multiple_invr(dr ** d , n)
    if dy == None:
        print("Inverse is not in the range")
    return dy

def enc_str(s):
    result = ""
    for x in list(s):
        t = chr(enc_char(ord(x)))
        result += t
    return result

def dyc_str(enc):
    result = ""
    for x in list(enc):
        t = chr(dyc_char(ord(x)))
        result += t
    return result

s = input("Enter the String : ")
print("\nThe Plain string: {0} \n".format(s))
enc = enc_str(s)
print("The Encrypted string: {0} \n".format(enc))
dyc = dyc_str(enc)
print("the Decrypted string: {0} \n".format(dyc))

