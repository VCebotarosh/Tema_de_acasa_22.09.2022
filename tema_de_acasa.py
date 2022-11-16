def putere_recursie(a,b):
    if b==0:
        return 1
    else:
        return a*putere_recursie(a,b-1)

def putere_iteratie(a,b):
    putere=1
    if b==0:
        return 1
    else:
        for i in range(1,b+1):
            putere*=a
        return putere

a=int(input("Dati numarul: "))
b=int(input("Dati puterea: "))
print(f"Valoare prin recursie: {putere_recursie(a,b)}")
print(f"Valoarea prin iteratie: {putere_iteratie(a,b)}")