def suma_numerelor(a,b):
    return a+b

def produsul_numerelor(a,b):
    return a*b

def media_aritmetica(a,b):
    return (a+b)/2

def cmmdc(a,b):
    while b!=0:
        a,b=abs(b),abs(a%b)
    return a

def cmmc(a,b):
    return abs(a*b)/cmmdc(a,b) 

def minim(a,b):
    if a>b:
        return b
    else:
        return a
def maxim(a,b):
    if a>b:
        return a
    else:
        return b

def suma2():
    print(f"{a}+{b}={suma_numerelor(a,b)}")

def produs2():
    print(f"{a}*{b}={produsul_numerelor(a,b)}")

def all_divisors_between_two_numbers():
    divizori=[]
    for i in range(1,abs(maxim(a,b))+1):
        if a%i==0 and b%i==0:
            divizori.append(i)
    return divizori

def number_of_divisors_one_number(x:int):
    divizori=0
    for i in range(1,x+1):
        if x%i==0:
            divizori+=1
    return divizori


def five_multiples():
    multipli=[]
    for i in range(1,6):
        multipli.append(abs(cmmc(a,b))*i)
    return multipli

def cifre_comune():
    return list(set(str((abs(a)))).intersection(set(str((abs(b))))))

def cifre_specifice():
    return f"Cifrele specifice numarului {a} sunt: {list(set(str(a)).difference(set(str(b))))}\nCifrele specifice numarului {b} sunt: {list(set(str(b)).difference(set(str(a))))}"

def afisare_prietene():
    divizor1=number_of_divisors_one_number(a)
    divizor2=number_of_divisors_one_number(b)
    if divizor1==divizor2:
        print(f"PRIETENE")
    else:
        print(f"NU SUNT PRIETENE")
a=int(input())
b=int(input())
print(suma_numerelor(a,b))
print(produsul_numerelor(a,b))
print(media_aritmetica(a,b))
print(cmmdc(a,b))
print(cmmc(a,b))
print(minim(a,b))
print(maxim(a,b))
suma2()
produs2()
print(all_divisors_between_two_numbers())
print(five_multiples())
print(cifre_comune())
print(cifre_specifice())
afisare_prietene()
