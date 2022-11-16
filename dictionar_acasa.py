dictionar={2:56, 1:2, 4:12, 5:24, 6:18, 3:323}
solution1=dict(sorted(dictionar.items(), key=lambda x:x[1]))
solution2=dict(sorted(dictionar.items(), key=lambda x:x[0]))
print(f"Cheile in ordine crescatoare: ")
for key, value in solution2.items():
    print(key, end=" ")
print("\n")
print(f"Valorile dupa cheile sortate crescator: ")
for key, value in solution2.items():
    print(value, end=" ")
print("\n")
print(f"Valorile sortate crescator sunt: ")
for key, value in solution1.items():
    print(value, end=" ")
print("\n")
print(f"Valorile ordonate crescator dupa cheie si valoare sunt: ")
print(list(solution1.items()))