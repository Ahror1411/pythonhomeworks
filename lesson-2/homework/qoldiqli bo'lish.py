nom1=int(input("Bo'linuvchini kiriting: "))
nom2=int(input("Bo'luvchini kiriting: "))
if nom2==0:
    print("Nolga bolish mumkin emas!!!") 
else:
        bolinma =nom1//nom2
        qoldiq=nom1%nom2
        print("Bo'linma = ", bolinma)
        print("Qoldiq = ",qoldiq)
# or        
a,b=divmod(nom1,nom2)
print("Bo'linma = ", a)
print("Qoldiq = ",b)
        