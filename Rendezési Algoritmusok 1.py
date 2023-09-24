import random
import string

while True:

    choice = input('Mit csináljon a program ("számgenerálás" vagy "1"), ("szöveggenerálás" vagy "2"), ("számbeolvasás" vagy "3"), ("szövegbeolvasás" vagy "4"): ')


    #>-------|SZÁMGENERÁLÁS|-------<#


    if choice.lower() == "számgenerálás" or choice == "1":

        #Határok beolvasása

        while True:
            try:
                lowerlimit, upperlimit = input("Add meg az alsó és felső határt (2 db egész szám) szóközzel elválasztva: ").split()
                try:
                    int(lowerlimit)
                    int(upperlimit)
                    if int(lowerlimit) > int(upperlimit):
                        print('\033[31m'"Az alsó határ nem lehet nagyobb mint a felső!"'\033[0m')
                        continue
                    if int(lowerlimit) == int(upperlimit):
                        print('\033[31m'"A két szám nem lehet azonos!"'\033[0m')
                        continue
                except ValueError:
                    print('\033[31m'"Csak egész számokat adj meg!"'\033[0m')
                    continue
            except ValueError:
                print('\033[31m'"Két értéket adj meg!"'\033[0m')
                continue
            break

        #Darabszám beolvasása

        while True:
            try:
                amount = int(input("Hány számot generáljon a program: "))
                if amount < 1:
                    print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                    continue
            except ValueError:
                print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                continue
            break

        #Számok generálása és kiíratása

        with open("ki.txt", "w") as f:
            print('\033[34m'f"{amount} db véletlenszerűen generált szám {lowerlimit} és {upperlimit} között: "'\033[0m',end='')
            for i in range(0, amount):
                generatednumber = random.randint(int(lowerlimit), int(upperlimit))
                print('\033[35m'f"{generatednumber}", end='; ''\033[0m')
                f.write(str(generatednumber)+";")
        break


    #>--------|SZÖVEGGENERÁLÁS|--------<#


    elif choice.lower() == "szöveggenerálás" or choice == "2":
        letters = string.ascii_letters

        #Darabszám beolvasása

        while True:
            try:
                amount=int(input("Hány db szöveget generáljon a program: "))
                if amount < 1:
                    print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                    continue
            except ValueError:
                print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                continue
            break
        
        #Szöveg generálása és kiíratása

        with open("ki.txt", "w") as f:
            print('\033[34m'f"{amount} db véletlenszerűen generált szöveg 1 és 20 betű hosszúság között: "'\033[0m',end='')
            for i in range(0, amount):
                textlength = random.randint(1, 20)
                randomtext = ''.join(random.choices(letters, k = textlength))
                print('\033[35m'f"{randomtext}", end=' ''\033[0m')
                print('\033[34m'f"({textlength})", end='; ''\033[0m')
                f.write(randomtext+";")
        break


    #>--------|SZÁMBEOLVASÁS|--------<#

            
    elif choice.lower() == "számbeolvasás" or choice == "3":

        while True:

        #Határok beolvasása

            while True:
                    try:
                        lowerlimit, upperlimit = input("Add meg az alsó és felső határt (2 db egész szám) szóközzel elválasztva: ").split()
                        try:
                            int(lowerlimit)
                            int(upperlimit)
                            if int(lowerlimit) > int(upperlimit):
                                print('\033[31m'"Az alsó határ nem lehet nagyobb mint a felső!"'\033[0m')
                                continue
                            if int(lowerlimit) == int(upperlimit):
                                print('\033[31m'"A két szám nem lehet azonos!"'\033[0m')
                                continue
                        except ValueError:
                            print('\033[31m'"Csak egész számokat adj meg!"'\033[0m')
                            continue
                    except ValueError:
                        print('\033[31m'"Két értéket adj meg!"'\033[0m')
                        continue
                    break

            #Darabszám beolvasása
            
            while True:
                    try:
                        amount = int(input("Hány szám van az állományban: "))
                        if amount < 1:
                            print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                            continue
                    except ValueError:
                        print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                        continue
                    break

            #Dokumentum beolvasása

            with open("ki.txt", "r", encoding="utf-8") as f:
                numbers = f.read().strip().split(";")[:-1]

            #Feltételek ellenőrzése

            valuesarebetweenlimits = True

            for x in numbers:
                try:
                    if int(lowerlimit) <= int(x) <= int(upperlimit): 
                        valuesarebetweenlimits = True
                    else:
                        valuesarebetweenlimits = False     
                except ValueError:
                    print('\033[31m'"Az állományban nem egész számok vannak."'\033[0m')
                    exit()

            if valuesarebetweenlimits == False:
                print('\033[31m'"Az állományban lévő számok nem a megadott határok között vannak."'\033[0m')

            elif valuesarebetweenlimits == True and amount > len(numbers):
                print('\033[31m'"Kevesebb szám van az állományban mint a megadott érték."'\033[0m')

            elif valuesarebetweenlimits == True and amount < len(numbers):
                print('\033[31m'"Több szám van az állományban mint a megadott érték."'\033[0m')

            else:
                print('\033[34m'"Az adatok megfelelnek a feltételeknek."'\033[0m')
                exit()

            #Újrapróbálkozás lehetősége

            while True:
                retry=input('Szeretnél újrapróbálkozni? ("igen" vagy "nem"): ')
                if retry.lower() == "igen":
                    break

                elif retry.lower() == "nem":
                    exit()
                
                else:
                    print('\033[31m'"Érvénytelen válasz."'\033[0m')
                    continue

            
    #>--------|SZÖVEGBEOLVASÁS|--------<#


    elif choice.lower() == "szövegbeolvasás" or choice == "4":

        while True:
        
        #Dokumentum beolvasása

            with open("ki.txt", "r", encoding="utf-8") as f:
                text = f.read().strip().split(";")[:-1]

            #Szöveg hosszának és tartalmának ellenőrzése

            englishalphabetonly = True
            for x in text:
                for char in x:
                    if char not in string.ascii_letters:
                        englishalphabetonly = False 
                        
                if englishalphabetonly == True and len(x) < 1 or len(x) > 20:
                    print('\033[31m'"Az állományban lévő szöveg(ek) hossza nem 1 és 20 betű között van."'\033[0m')
                    exit()

                elif englishalphabetonly == False:
                    print('\033[31m'"Az állományban nem csak az angol abc nagy és kis betűi szerepelnek."'\033[0m')
                    exit()

            #Darabszám beolvasása

            while True:
                try:
                    amount=int(input("Hány db szöveg van az állományban: "))
                    if amount < 1:
                        print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                        continue
                except ValueError:
                    print('\033[31m'"\033[4mEgy pozitív egész\033[0m \033[31mszámot adj meg!"'\033[0m')
                    continue
                break

            #Darabszám ellenőrzése

            if len(text) == amount and englishalphabetonly == True and 1 <= len(x) <= 20:
                    print('\033[34m'"Az adatok megfelelnek a feltételeknek."'\033[0m')
                    exit()

            elif len(text) < amount:
                print('\033[31m'"Az állományban kevesebb db szöveg van mint a megadott érték."'\033[0m')

            else:
                print('\033[31m'"Az állományban több db szöveg van mint a megadott érték."'\033[0m')

            #Újrapróbálkozás lehetősége

            while True:
                retry=input('Szeretnél újrapróbálkozni? ("igen" vagy "nem"): ')
                if retry.lower() == "igen":
                    break

                elif retry.lower() == "nem":
                    exit()
                        
                else:
                    print('\033[31m'"Érvénytelen válasz."'\033[0m')
                    continue

    else:
        print('\033[31m'"Érvénytelen válasz."'\033[0m')
        continue