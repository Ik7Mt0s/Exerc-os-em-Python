def insertion_sort(A):
    for j in range(1, len(A)):
        chave = A[j]
        i = j-1
        while i >= 0 and A[i]> chave:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = chave

lista = []
entrada = input()
numeros = entrada.split()  

for num in numeros:
    lista.append(int(num))

print(f"Lista original: {lista}")
insertion_sort(lista)
print(f"Lista ordenada: {lista}")

'''
Terminal
1 2 4 3 5 7 6
Lista origial: [1, 2, 4, 3, 5, 7, 6]
Lista ordenada: [1, 2, 3, 4, 5, 6, 7]
'''
#Complexidade O(n²)