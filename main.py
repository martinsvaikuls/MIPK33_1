import random

# Spēles sākumā spēles programmatūra gadījuma ceļā saģenerē 5 skaitļus diapazonā no 10000 līdz 20000, 
# bet tādus, kas sākotnēji dalās gan ar 3, gan ar 2.  

start = []
for i in range(5):
    start.append(6*random.randint(1667, 3333))

for i in range(len(start)):
    print(f"Sakuma skaitlis {i+1} = {start[i]}")

a = start[int(input())-1] # Cilvēks-spēlētājs izvēlas, ar kuru no saģenerētajiem skaitļiem viņš vēlas sākt spēli.
print(a)