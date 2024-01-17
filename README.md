# **PROJEKTA DARBS**
*veidoja: Endija Romanova 231RDC001*

**PROJEKTA MĒRĶIS**

Projekta darba mērķis ir izveidot programmu, kura automatizē mobilo sakaru operatora "LMT" sniegto pakalpojumu rēķinu analīzes veidošanu, rezultātā izvadot pārskatāmu atskaiti par izvēlēto periodu. 
Programmas uzdevumi ir sekojoši:
1. Pārdēvēt rēķinu PDF failu nosaukumus
2. Izveidot tabulu, kurā ir secīgi attēloti:
- Gada mēneši
- Kopumā pavadītais laiks zvanos konkrētajā mēnesī (minūtēs)
- Kopumā patērētais interneta daudzums konkrētajā mēnesī (gb)
3. Izveidot kopsavilkumu, kurā ir aprakstīts:
- Mēnesis ar vislielāko/vismazāko zvanu ilgumu
- Mēnesis ar vislielāko/vismazāko interneta patēriņu
- Kopējais zvanu ilgums atlasītajā periodā
- Vidējais zvanu ilgums mēnesī
- Kopējais interneta patēriņa lielums atlasītajā periodā
- Vidējais interneta patēriņa lielums mēnesī
4. Izveidot papildus sadaļu, kurā ir attēlots:
- Vislētākais/visdārgākais rēķins atlasītajā periodā
- Kopumā samaksātā nauda rēķinos atlasītajā periodā

**IZMANTOTĀS PYTHON BIBLIOTĒKAS**

**os** tiek izmantota, lai varētu strādāt ar datnēm, mainot nosaukumus PDF failiem

**PyPDF2** tiek izmantota, lai nolasītu informāciju no PDF failiem

**pathlib** tiek izmantota, lai nodrošinātu piekļuvi failu sistēmai

**tabulate** tiek izmantota, lai izvadītu informāciju tabulas formātā

**PROGRAMMATŪRAS METOŽU APRAKSTS**

*failu_parsauksana.py*

Ar funkcijas *os.makedirs* palīdzību tiek izveidota jauna mape, kur tiks saglabāti PDF faili ar jaunajiem nosaukumiem. Pēc tam, izmantojot *for* ciklu, tiek iets cauri visiem sākotnējā mapē esošajiem failiem, ar funkciju *enumerate* iegūstot pašreizējo faila nosaukumu (*filename*) un numurāciju (*count*). Ar funkcijas *os.path.join* palīdzību mainīgajos "src" un "dst" tiek saglabāts ceļš uz sākotnējo un jauno failu. Pēdējā cikla rindiņa pārdēvē PDF failus uz pārceļ tos uz jauno mapi, izmantojot funkciju *os.rename*.

*programma.py*

Izmantojot funkciju *pathlib.Path* mainīgajā "adrese" tiek norādīts ceļš uz mapi, kurā atrodas pārdēvētie rēķini. Pēc tam, mainīgajā "visi_faili" tiek norādīts, ka ir vajadzīgs nolasīt no "adrese" visus failus, kuri satur paplašinājumu ".pdf". Lai panāktu šo, tiek izmantots *glob()*, kā arī papildus tiek izmantots *sorted()*, lai sakārtotu failus secīgi. 

Lielāko daļu programmas sastāda *for* cikls, kas ļauj iet caur visiem norādītajiem failiem. Zem šī cikla tiek izmantotas sekojošās funkcijas:
- *PyPDF2.PdfReader* , kas ļauj nolasīt informāciju no PDF datnes. Šī komanda tiek saglabāta mainīgajā "rekins";
- Ar funkciju *open()* tiek atvērti faili lasīšanai (*"rb"*);
- Mainīgajos "lapa1", "lapa3" un "lapa4" tiek saglabāta informācija par rēķina lapu atrašanās vietām, izmantojot *pages[]*;
- Mainīgajos "teksts1", "teksts3" un "teksts4" tiek saglabāts katras rēķina lapas teksts, izmantojot *extract_text()*;
- Ar metodi *find()* tiek atrastas nepieciešamo datu pozīcijas tekstos, kas rezultātā tiek saglabātas mainīgajos ar attiecīgajiem nosaukumiem;
- Ņemot vērā to, ka nolasītie dati ir nepieciešami aprēķiniem, tie tiek pārveidoti no *str* uz *float* un saglabāti jaunos mainīgajos;
- Ar metodi *append()* nolasītās un nepieciešamajā formātā pārveidotās vērtības tiek pievienotas sarakstam "rinda" (ja dati tiks izmantoti tabulai) un sarakstam "summas" (ja dati tiks izmantoti papildus sadaļai par rēķinu summām), kā arī saraksts "rinda" tiek pievienots sarakstam "data";
- Ar nosacījuma izteiksmi *if* un *elif* mainīgajam "menesis" tiek piešķirti mēnešu nosaukumi, balstoties uz iepriekš izvadīto mēneša numuru no rēķina perioda.

Tālāk tiek izmantota funkcija *sorted*, lai sakārtotu sarakstā "data" esošo informāciju hronoloģiskā secībā, balstoties uz *key* parametra sarakstā norādīto secību. Mainīgajā "rezultats" tiek izmantota metode *tabulate*, kas izvada sakārtoto sarakstu "data" tabulas formātā. Tabulas noformēšanai tiek izmantots *tablefmt* piedāvātais noformējums "simple_grid". 
Nākmajā programmas daļā ar funkcijām *max* un *min* tiek atrastas atlasīto datu minimālās un maksimālās vērtības, ar parametru *key* norādot kuru saraksta elementu ir nepieciešams salīdzināt. Ar *for* cikliem tiek saskaitītas kopumā norunātās minūtes, patērētais interneta daudzums un samaksātā summa, kā arī ar aritmētiskām darbībām tiek aprēķinātas vidējās vērtības. Izvadot datus, visas skaitliskās vērtības tiek noapaļotas ar diviem cipariem aiz komata izmantojot funkciju *round()*. 

Rezultātā terminālī ir izvadīta pārskatāmi noformēta atskaite par atlasīto periodu, kas šajā gadījumā ir 2023. gada analīze. 




