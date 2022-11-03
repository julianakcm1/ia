factBase = {
    "A": True,
    "C": True,
    "D": True,
    "E": True,
    "G": True,
    "H": True,
    "K": True
}

target = {
    "Q": True
}

def verify(rules):
    for i in rules:
        if (not(i in factBase)):
            return False # if it left the for, it is part of the factBase
    
    for i in rules:
        if(not(factBase[i])):
            return False # if it leaves this for, it is true

    return True
    

def rules():
    if verify(["K", "L", "M"]): #R1
        factBase["I"] = True
        return
    if (verify(["I", "L", "J"])): #R2
        factBase["Q"] =  True
        return
    if (verify(["C", "D", "E"])): #R3
        factBase["B"] = True
        return
    if(verify(["A", "B"])): #R4
        factBase["Q"] = True
        return
    if(verify(["L", "N", "O", "P"])): #R5
        factBase["Q"] = True
        return
    if(verify(["C", "H"])): #R6
        factBase["R"] = True
        return
    if(verify(["R","J","M"])): #R7
        factBase["S"] = True
        return
    if(verify(["F","H"])): #R8
        factBase["B"] = True
        return
    if(verify(["G"])): #R9
        factBase["F"] = True
        return
