import math

class Foci:
    def __init__(sor, sorsorszam:int, orszag:str, helyezes:int, ev:int, helyszin:str):
        sor.sorszam=sorsorszam
        sor.orszag=orszag
        sor.helyezes=helyezes
        sor.ev=ev
        sor.helyszin=helyszin

def readfile():
    list=[]
    with open("input.txt", encoding="utf-8") as f:
        for sor in f:
            tomb=sor.strip().split('\t')
            list.append(Foci(int(tomb[0]),tomb[1],int(tomb[2]),int(tomb[3]),tomb[4]))
    return list

foci=readfile()

def helyezesek(orszag1):
    helyezesek=[]
    evek=[]
    helyszin=[]
    for f in foci:
        if f.orszag==orszag1:
            helyezesek.append(f.helyezes)
            evek.append(f.ev)
            helyszin.append(f.helyszin)
    print(f"{orszag1} által elért helyezések: {helyezesek} az adott években: {evek} az adott helyszíneken: {helyszin} történtek.")

helyezesek("Magyarország")

def evtizednyertes(evtized):
    nyertesek=[]
    for f in foci:
        if f.helyezes==1 and (f.ev-evtized)<10 and (f.ev-evtized)>0:
            nyertesek.append(f.orszag)
    print(f"{evtized} nyertesei: {nyertesek}")

evtizednyertes(1960)

def kijut(orszag1):
    ossz=0
    for f in foci:
        if f.orszag==orszag1:
            ossz+=1
    print(f"{orszag1} összesen ennyi alkalommal jutott ki a világbajnokságra: {ossz}")

kijut("Magyarország")

def nyertes(evszam):
    nyertes="Nem volt VB."
    for f in foci:
        if f.helyezes==1 and f.ev==evszam:
            nyertes=f.orszag
    if nyertes!="Nem volt VB.": print(f"{evszam}. évben {nyertes} lett a világbajnok.")
    else: print(nyertes)

nyertes(1940)

def masodik(evszam):
    masodik="Nem volt VB."
    for f in foci:
        if f.helyezes==2 and f.ev==evszam:
            masodik=f.orszag
    if masodik!="Nem volt VB.": print(f"{evszam}. évben {masodik} lett a második.")
    else: print(masodik)

masodik(1940)

def legkorabbivb():
    evszam=20000
    for f in foci:
        if f.ev<evszam:
            evszam=f.ev
    print(f"{evszam}. éveben volt a legkorábban VB.")

def hanyszornyert(orszag1):
    ossz=0
    for f in foci:
        if f.orszag==orszag1 and f.helyezes==1:
            ossz+=1
    print(f"{orszag1} összesen {ossz} alkalommal nyert VB-t.")

hanyszornyert("Brazília")

def legjobbhelyezes(orszag1):
    legjobb=100
    for f in foci:
        if f.orszag==orszag1 and f.helyezes<legjobb:
            legjobb=f.helyezes
    if legjobb!=100:
        print(f"{orszag1} legjobb helyezése {legjobb}.")
    else: print("Nem jutott ki egyszer sem a VB-re.")

legjobbhelyezes("Mongólia")

def rendezo(orszag1):
    nyertesek=[]
    evszam=[]
    volt=False
    for f in foci:
        if f.helyszin==orszag1 and f.helyezes==1:
            nyertesek.append(f.orszag)
            evszam.append(f.ev)
            volt=True
    if volt==True:
        print(f"Ezek az országok nyertek az {orszag1} által rebdezett VB-ken: {nyertesek} az adott években: {evszam}")
    else:
        print("Ez az ország nem tartott VB-t")

rendezo("Anglia")

def dobogos(orszag1):
    nyertesek,evszamok=([],[])
    volt=False
    for f in foci:
        if f.helyezes==1 or f.helyezes==2 or f.helyezes==3:
            if f.orszag==orszag1:
                evszamok.append(f.ev)
                volt=True
    for f in foci:
        if f.ev in evszamok and f.helyezes==1:
            nyertesek.append(f.orszag)
    if volt==True:
        print(f"Amikor {orszag1} dobogós lett ezek az országok nyertek: {nyertesek} ezekben az években: {evszamok}")
    else:
        print("Ez az ország nem volt dobogós VB-n") 

dobogos("Magyarország")

def donto(orszag1):
    dontosok=[]
    evszamok=[]
    for f in foci:
        if  f.helyezes==1 or f.helyezes==2:
            if f.orszag==orszag1:
                evszamok.append(f.ev)
    for f in foci:
        if  f.ev in evszamok and f.orszag!=orszag1:
            if f.helyezes==1 or f.helyezes==2:
                dontosok.append(f.orszag)
    print(f"{orszag1} ezekkel az országokkal játszott döntőt: {dontosok} ilyenkor: {evszamok}")

donto("Magyarország")

def tobbszornyer():
    tobbszor=[]
    egyszer=[]
    for f in foci:
        if f.helyezes==1:
            egyszer.append(f.orszag)
    for f in foci:
        if f.orszag in egyszer and f.helyezes==1 and f.orszag not in tobbszor:
            tobbszor.append(f.orszag)
    print(f"Ezek az országok nyertek többször VB-t: {tobbszor}")

tobbszornyer()

def tobbszorrendez():
    tobbszor=[]
    egyszer=[]
    egyszerev=[]
    for f in foci:
        if f.helyszin not in egyszer:
            egyszer.append(f.helyszin)
            egyszerev.append(f.ev)
    for f in foci:
        if f.helyszin in egyszer and f.ev not in egyszerev and f.helyszin not in tobbszor:
            tobbszor.append(f.helyszin)
    print(f"Ezek az országok rendeztek többször VB-t: {tobbszor}")

tobbszorrendez()

def legtobbszorszamol(List):
    counter=0
    ossz=List[0]
    for i in List:
        curr_frequency=List.count(i)
        if(curr_frequency>counter):
            counter =curr_frequency
            ossz=i
    return ossz
    
def legtobbszornyer():
    legtobbszor=""
    nyertesek=[]
    for f in foci:
        if f.helyezes==1:
                nyertesek.append(f.orszag)            
    legtobbszor=legtobbszorszamol(nyertesek)
    hanyszor=nyertesek.count(legtobbszor)
    print(f"Legtöbbször ez az ország nyert VB-t: {legtobbszor} ennyiszer: {hanyszor}")

legtobbszornyer()

def legtobbszorrendez():
    legtobbszor=[]
    rendezett=[]
    for f in foci:
        if f.helyszin==f.orszag:
                rendezett.append(f.orszag)          
    legtobbszor=legtobbszorszamol(rendezett)
    hanyszor=rendezett.count(legtobbszor)
    print(f"Legtöbbször ez az ország rendezett VB-t: {legtobbszor} ennyiszer: {hanyszor}")

legtobbszorrendez()

def legtobbszormasodik():
    legtobbszor=[]
    masodik=[]
    for f in foci:
        if f.helyezes==2:
            masodik.append(f.orszag)
    legtobbszor=legtobbszorszamol(masodik)
    hanyszor=masodik.count(legtobbszor)
    print(f"Legtöbbször ez az ország lett 2.: {legtobbszor} ennyiszer: {hanyszor}")

legtobbszormasodik()

def hanyszorinput():
    orszagok=[]
    orszagokszam=[]
    szerepelt=[]
    i=0
    for f in foci:
        if f.orszag not in orszagok:
            orszagokszam.append(f.orszag)
        orszagok.append(f.orszag)         
    for f in range(len(orszagokszam)):
        szerepelt.append(orszagok.count(orszagokszam[i]))
        i+=1
    print(f"{orszagokszam} ennyiszer szerepeltek: {szerepelt}")

hanyszorinput()

def helyszinek():
    helyek=[]
    for f in foci:
        if f.helyszin==f.orszag and f.helyszin not in helyek:
            helyek.append(f.helyszin)
    print(f"Itt zajlottak VB-k: {helyek}")

helyszinek()

def merkozes():
    orszagok=[]
    for f in foci:
        if f.orszag not in orszagok:
            orszagok.append(f.orszag)
    print(f"Ezek az országok játszottak mérkőzéseket: {orszagok}")

merkozes()

def legtobbadatev():
    legtobb=0
    legtobbev=""
    i=0
    evek=[]
    evekszam=[]
    for f in foci:
        if f.ev not in evek:
            evekszam.append(f.ev)
        evek.append(f.ev)
    for f in range(len(evekszam)):
        szam=(evek.count(evekszam[i]))
        if szam>legtobb: 
            legtobb=szam
            legtobbev=evekszam[i]
        i+=1
    print(f"A legtöbb adat ebből az évből száramzik: {legtobbev} ennyi:{legtobb}")

legtobbadatev()

def legtobbadatevtized():
    legtobb=0
    legtobbev=""
    i=0
    evek=[]
    evekszam=[]
    for f in foci:
        evtized=math.floor(f.ev/10)
        if evtized not in evek:
            evekszam.append(evtized)
        evek.append(evtized)
    for f in range(len(evekszam)):
        szam=(evek.count(evekszam[i]))
        if szam>legtobb: 
            legtobb=szam
            legtobbev=evekszam[i]*10
        i+=1
    print(f"A legtöbb adat ebből az évtizedből száramzik: {legtobbev} ennyi:{legtobb}")

legtobbadatevtized()

def helyadat():
    i=1
    helyek={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,}
    for f in foci:
        helyek[f.helyezes]=helyek[f.helyezes]+1
    for f in range(len(helyek)):
        print(f"{i}. helyezésből {helyek[i]} db")
        i+=1

helyadat()

def pontok():
    orszagok={}
    for f in foci:
        if f.orszag not in orszagok:
            orszagok[f.orszag]=0
    for f in foci:
        if f.helyezes==1:orszagok[f.orszag]+=6
        if f.helyezes==2:orszagok[f.orszag]+=5
        if f.helyezes==3:orszagok[f.orszag]+=4
        if f.helyezes==4:orszagok[f.orszag]+=3
        if f.helyezes==5:orszagok[f.orszag]+=2
        if f.helyezes==6:orszagok[f.orszag]+=1
    legtobborszag = max(orszagok, key=orszagok.get)
    legtobbpont = max(orszagok.values())
    print(f"Legtöbb ponttal rendelkező ország: {legtobborszag}: {legtobbpont}")


pontok()

    

    
            


    

