from random import randint

vetor_1 = [randint(0, 101) for _ in range(10)]
vetor_2 = [randint(0, 101) for _ in range(10)]
vetor_3 = []

for x in range(0,9):
    vetor_3.append(vetor_1[x])
    vetor_3.append(vetor_2[x])

print(vetor_1)
print(vetor_2)
print(vetor_3)
    