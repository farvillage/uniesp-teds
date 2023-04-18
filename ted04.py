##TED04:
##R1:

VN = str(input("Insira um valor númerico (positivo ou negativo): "))
print(VN)

##R2:

N = float(input("Quantas maçã(s) você deseja? "))
if N < 12:
    print("A(s) maçã(s) custa(m) R$1,30 cada")
elif N >= 12:
    print("As maçãs custam R$1,00 cada")
