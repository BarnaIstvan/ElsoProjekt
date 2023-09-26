with open('ki.txt', 'r') as file: # A program beolvassa az adatokat.
    adat=file.read().split() 

def szamok(s): # Itt dönti el, hogy a fájlban számok találhatóak-e.
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def betuk(b): # Itt pedig a betűket fésüli át.
    return b.isalpha() # Utánna járással a legtöbb helyen az .isalpha parancsot láttam, így gondoltam leegyszerüsítem ezzel.
    
def valosadat(adat): #Itt nézi át hogy az adat reális-e.
    for item in adat:   
        if not szamok(item) and not item.isalpha():
            return False
    return True

# Itt pedig jelzi, hogy a fájlban milyen típusú adatok találhatóak, vagy ha nem megfelelőek az adatok.

if all(szamok(item) for item in adat):
    print(f"A fájlban számok találhatóak. A fájlban található számok: {adat}")
elif all(betuk(item) for item in adat):
    print(f"A fájlban betűk találhatóak. A fájlban található betűk: {adat}")
else:
    print("A fájlban helytelen adatok találhaóak.")

def buborek_rendezes(adat, csokkeno=False): # Végül a buborék rendezésnél maradtam, ezt láttam a legegyszerűbbnek az összes közül és erre volt a legtöbb példa is, így ezzel volt a legegyszerűbb dolgom.
    n = len(adat)
    for i in range(n):
        for j in range(0, n-i-1):
            # Itt a program összehasonlítja az egymás melletti elemeket, és ha kell ki is cseréli azokat.
            if (csokkeno and adat[j] < adat[j+1]) or (not csokkeno and adat[j] > adat[j+1]):
                adat[j], adat[j+1] = adat[j+1], adat[j]
        
buborek_opcio = input("Kérem üsse be, a buborék rendezés növekvő vagy csökkenő sorrendbe rendezze az elemeket ('nov', 'csok'): ") # A felhasználó itt döntheti el, milyen rendezést szeretne a buborék rendezésen belül.

if buborek_opcio == 'nov': # Ez felelős a növekvő sorrendért.
    buborek_rendezes(adat)
    print(f"Buborék rendezés növekvő sorrendben: {adat}")

elif buborek_opcio == 'csok': # Míg ez a csökkenőért. Mivel a 'csokkeno' parametert mar megadtuk, így csak igazra kellett állítani.
    buborek_rendezes(adat, csokkeno=True)
    print(f"Buborék rendezés csökkenő sorrendben: {adat}")

