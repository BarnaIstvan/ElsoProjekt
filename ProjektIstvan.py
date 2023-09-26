with open('ki.txt', 'r') as file: 
    adat=file.read().split(";")[:-1]

def szamok(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def betuk(b): 
    return b.isalpha() 
    
def valosadat(adat): 
    for item in adat:   
        if not szamok(item) and not item.isalpha():
            return False
    return True

if all(szamok(item) for item in adat):
    print(f"A fájlban számok találhatóak. A fájlban található számok: {adat}")
elif all(betuk(item) for item in adat):
    print(f"A fájlban betűk találhatóak. A fájlban található betűk: {adat}")
else:
    print("A fájlban helytelen adatok találhaóak.")

def elem_beillesztese(adat, elem):  
    if valosadat(elem):
        adat.append(elem)

uj_elem = input("Adja meg az új elemet: ")
elem_beillesztese(adat, uj_elem)
print(f"Új elem beillesztve! {adat}")

if all(szamok(item) for item in adat):
    def buborek_rendezes(adat, csokkeno=False):
        n = len(adat)
        for i in range(n):
            for j in range(0, n-i-1):
                if (csokkeno and int(adat[j]) < int(adat[j+1])) or (not csokkeno and int(adat[j]) > int(adat[j+1])):
                    adat[j], adat[j+1] = adat[j+1], adat[j]

elif all(betuk(item) for item in adat):
    def buborek_rendezes(adat, csokkeno=False): 
        n = len(adat)
        for i in range(n):
            for j in range(0, n-i-1):
                if (csokkeno and adat[j].lower() < adat[j+1].lower()) or (not csokkeno and adat[j].lower() > adat[j+1].lower()):
                    adat[j], adat[j+1] = adat[j+1], adat[j]
        
buborek_opcio = input("Kérem üsse be, a buborék rendezés növekvő vagy csökkenő sorrendbe rendezze az elemeket ('nov', 'csok'): ") # A felhasználó itt döntheti el, milyen rendezést szeretne a buborék rendezésen belül.

if buborek_opcio == 'nov': 
    buborek_rendezes(adat)
    print(f"Buborék rendezés növekvő sorrendben: {adat}")

elif buborek_opcio == 'csok': 
    buborek_rendezes(adat, csokkeno=True)
    print(f"Buborék rendezés csökkenő sorrendben: {adat}")

def gyors_rendezes(adat, csokkeno=False): 
    if len(adat) <= 1:
        return adat
    
    pivot = adat[len(adat) // 2] 
    kev = []
    egy = []
    tobb = []

    for x in adat: 
        if (csokkeno and x.lower() > pivot.lower()) or (not csokkeno and x.lower() < pivot.lower()):
            kev.append(x)
        elif x == pivot:
            egy.append(x)
        else:
            tobb.append(x)
    return gyors_rendezes(kev, csokkeno) + egy + gyors_rendezes(tobb, csokkeno)

gyors_opcio = input("Kérem üsse be, a gyors rendezés növekvő vagy csökkenő sorrendbe rendezze az elemeket ('nov', 'csok'): ")

if gyors_opcio == 'nov':
    print(f"Gyors rendezés növekvő sorrendben: {gyors_rendezes(adat)}")

elif gyors_opcio == 'csok':
    print(f"Gyors rendezés csökkenő sorrendben: {gyors_rendezes(adat, csokkeno=True)}")