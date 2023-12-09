class A:
    def sum(a,b):
        return a+b
    def sum(a,b,c=1):
        return a+b+c
obj=A
print(obj.sum(1,2,5))
# 	Same class = class A
# 	Same function name = sum 
# 	Diff parameters = a,b and a,b,c 
# 	Obj create chesi print chesthe last function ey thiskoni error vasthundi 
# 	E error ni overcome cheyali ante default ga parameter pass cheyali 
# 	Apudu error pothundi 
# 	Oka vela print chese time lo value pedithe default ga pettindi care cheyadu
