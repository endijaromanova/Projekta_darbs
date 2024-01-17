import PyPDF2
import pathlib
from tabulate import tabulate

data=[]
summas=[]

adrese = pathlib.Path("rekini(parsaukti)")
visi_faili = sorted(adrese.glob("*.pdf"))

for f in range(len(visi_faili)):
    rinda = [] 
    rekins = PyPDF2.PdfReader(open(visi_faili[f], "rb"))

    lapa1 = rekins.pages[0]
    lapa3 = rekins.pages[2]
    lapa4 = rekins.pages[3]
    teksts1 = lapa1.extract_text()
    teksts3 = lapa3.extract_text()
    teksts4 = lapa4.extract_text()

    pos7 = teksts1.find("kopsumma")
    pos8 = teksts1.find("Bilance")
    summa_str = teksts1[pos7+8:pos8].strip()
    summa = float(summa_str)

    pos1 = teksts4.find("Veiktie zvani")
    pos2 = teksts4.find("min")
    minutes_str = teksts4[pos1+17:pos2].replace(":", ".").strip()
    minutes = round(float(minutes_str), 2)

    pos3 = teksts4.find("lietoýanu")
    pos4 = teksts4.find("GB")
    internets_str = teksts4[pos3+10:pos4].strip()
    internets = round(float(internets_str), 2)

    pos5 = teksts3.find("t.sk.LatvijÆ")
    pos6 = teksts3.find("Internets telefonÆ")
    periods = teksts3[pos5+14:pos6-7].strip()
    menesis_str = periods[3:5]
    menesis = int(menesis_str)

    if menesis == 1:
        menesis = "Janvāris"
    elif menesis == 2:
        menesis = "Februāris"
    elif menesis == 3:
        menesis = "Marts"
    elif menesis == 4:
        menesis = "Aprīlis"
    elif menesis == 5:
        menesis = "Maijs"
    elif menesis == 6:
        menesis = "Jūnijs"
    elif menesis == 7:
        menesis = "Jūlijs"
    elif menesis == 8:
        menesis = "Augusts"
    elif menesis == 9:
        menesis = "Septembris"
    elif menesis == 10:
        menesis = "Oktobris"
    elif menesis == 11:
        menesis = "Novembris"
    else: menesis = "Decembris"
    
    rinda.append(menesis)
    rinda.append(minutes)
    rinda.append(internets)
    summas.append(summa)

    data.append(rinda)

sakartots = sorted(data, key=lambda x:["Janvāris", "Februāris", "Marts", "Aprīlis", "Maijs", "Jūnijs", "Jūlijs", "Augusts", "Septembris", "Oktobris", "Novembris", "Decembris"].index(x[0]))
rezultats = tabulate(sakartots,headers=["Mēnesis", "Zvani, min", "Internets, gb"], tablefmt="simple_grid")

print("\n --- PĀRSKATS --- \n")
print(rezultats)
print("\n --- KOPSAVILKUMS --- \n")

minutesMAX = max(data, key=lambda x: x[1])
print(minutesMAX[0] + " bija visrunātīgākais mēnesis, jo kopumā tika pavadītas " + str(round(minutesMAX[1], 2)) + " minūtes zvanos.")
minutesMIN = min(data, key=lambda x: x[1])
print("Tomēr " + minutesMIN[0] + " tika pavadīts zvanoties pavisam maz, tika norunātas tikai " + str(round(minutesMIN[1], 2)) + " minūtes!")

print()

internetsMAX = max(data, key=lambda x: x[2])
print(internetsMAX[0] + " izcēlās ar interneta sērfošanu - kopumā tika iztērēti " + str(round(internetsMAX[2], 2)) + " GB.")
internetsMIN = min(data, key=lambda x: x[2])
print("Savukārt " + internetsMIN[0] + " bija laiks piedzīvojumiem ārpus interneta, tādēļ šajā mēnesī tika patērēti tikai " + str(round(internetsMIN[2], 2)) + " GB!")

print()

minutesKOPA = 0
for row in data:
    minutesKOPA += row[1]
    minutesKOPA = round(minutesKOPA, 2)
minutesAVG = round((minutesKOPA / len(data)), 2)

print("Kopumā atlasītajā periodā tika pavadītas " + str(round(minutesKOPA, 2)) + " minūtes zvanos, kas bija vidēji " + str(minutesAVG) + " minūtes mēnesī.")

internetsKOPA = 0
for row in data:
    internetsKOPA += row[2]
    internetsKOPA = round(internetsKOPA, 2)
internetsAVG = round((internetsKOPA / len(data)), 2)

print("Kopumā patērētais interneta daudzums atlasītajā periodā bija " + str(internetsKOPA) + " GB, kā rezultātā, vidēji mēnesī tika patērēti " + str(internetsAVG) + " GB!")

print("\n --- RĒĶINU KOPSUMMA ---")
print("(ieskaitot arī citus LMT sniegtos pakalpojumus) \n")

summaMIN = min(summas)
print("Vislētākais rēķins atlasītajā periodā bija " + str(round(summaMIN, 2)) + " eiro.")

summaMAX = max(summas)
print("Dārgāko rēķinu sastādīja " +  str(round(summaMAX, 2)) + " eiro.")

summaKOPA = 0
for row in data:
    summaKOPA += summa

print("Kopumā atlasītajā periodā rēķinos tika samaksāti " + str(round(summaKOPA, 2)) + " eiro.")
print()