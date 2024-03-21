# cvičení 5 

# Napiš funkci na zpracování rodného čísla. Funkce vezme řetězec s rodným číslem bez lomítka a vrátí zjištěné hodnoty jako n-tici ve formátu (rok, měsíc, den, pohlaví). Například pro RČ 9057121234 vrátí hodnotu: (1990, 7, 12, 'žena').

# Rodné číslo není třeba kontrolovat (dělitelnost 11, ...).

# Pozn.: Pokud je část rodného čísla, která odpovídá roku, >= 54, jedná se o osoby narozené před rokem 2000. V opačném případě se osoba narodila v roce 2000 nebo později.

# Do řešení prosím nedávejte vlastní rodná čísla, ale pouze vymyšlená.

# Otestujte (například) pomocí:

# print(zpracuj_rodne_cislo('9057121234')) # (1990, 7, 12, 'žena')
# print(zpracuj_rodne_cislo('0007021234')) # (2000, 7, 2, 'muž')
def zpracuj_rodne_cislo(rodne_cislo):
    if int(rodne_cislo[:2]) >= 54:
        rok = 1900 + int(rodne_cislo[:2])
    else:
        rok = 2000 + int(rodne_cislo[:2])
    if int(rodne_cislo[2]) == 5 or int(rodne_cislo[2]) == 6:
        pohlavi = "žena"
    else:
        pohlavi = "muž"
    if pohlavi == "žena":
        mesic = int(rodne_cislo[2:4]) - 50
    else:
        mesic = int(rodne_cislo[2:4])
    den = int(rodne_cislo[4:6])
    return (rok, mesic, den, pohlavi)

print(zpracuj_rodne_cislo('9057121234'))
print(zpracuj_rodne_cislo('0007021234'))

# cvičení 6

# Rozšiř třídu Clovek tak, aby při vytváření vedle jména a příjmení zpracovala rodné číslo. Třída si do atributů uloží rok, měsíc a den narození a pohlaví. Následně rozšiř metodu kdo_jsi o nové informace.

# Pozn.: Lze použít funkci na zpracování rodného čísla z předchozí úlohy :)

# Do řešení prosím nedávejte vlastní rodná čísla, ale pouze vymyšlená.

# Otestujte (například) pomocí:

# osoba = Clovek('anna', 'nová', '9057121234')
# print(osoba.kdo_jsi()) # Jmenuji se Anna Nová, mé iniciály jsou AN, jsem žena rok narození 1990 a narozeniny mám 12.7.
# osoba = Clovek('jan', 'malý', '0007021234')
# print(osoba.kdo_jsi()) # Jmenuji se Jan Malý, mé iniciály jsou JM, jsem muž rok narození 2000 a narozeniny mám 2.7.
def format_jmena(jmeno):
    prvni_pismeno = jmeno[0]
    zbytek_pismen = jmeno[1:len(jmeno)]
    spravne_jmeno = prvni_pismeno.upper() + zbytek_pismen.lower()
    return spravne_jmeno

def zpracuj_rodne_cislo(rodne_cislo):
    if int(rodne_cislo[:2]) >= 54:
        rok = 1900 + int(rodne_cislo[:2])
    else:
        rok = 2000 + int(rodne_cislo[:2])
    if int(rodne_cislo[2]) == 5 or int(rodne_cislo[2]) == 6:
        pohlavi = "žena"
    else:
        pohlavi = "muž"
    if pohlavi == "žena":
        mesic = int(rodne_cislo[2:4]) - 50
    else:
        mesic = int(rodne_cislo[2:4])
    den = int(rodne_cislo[4:6])
    return (rok, mesic, den, pohlavi)

class Clovek:
    def __init__(self, jmeno, prijmeni,rodne_cislo):
        self.jmeno = format_jmena(jmeno)
        self.prijmeni = format_jmena(prijmeni)
        self.inicialy = self.jmeno[0] + self.prijmeni[0]
        self.rok = zpracuj_rodne_cislo(rodne_cislo)[0]
        self.mesic = zpracuj_rodne_cislo(rodne_cislo)[1]
        self.den = zpracuj_rodne_cislo(rodne_cislo)[2]
        self.pohlavi = zpracuj_rodne_cislo(rodne_cislo)[3]
    def kdo_jsi(self):
        return "Jmenuji se {} {} a mé iniciály jsou {}, jsem {} rok narození {} a narozeniny mám {}.{}.".format(self.jmeno, self.prijmeni, self.inicialy, self.pohlavi, self.rok, self.den, self.mesic)

osoba = Clovek('anna', 'nová', '9057121234')
print(osoba.kdo_jsi()) 
osoba = Clovek('jan', 'malý', '0007021234')
print(osoba.kdo_jsi())
