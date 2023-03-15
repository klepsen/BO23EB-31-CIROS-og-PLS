## [Timeliste](https://1drv.ms/x/s!An4Z2t_LGP8Egfc6DhIkCmNc5jDyEw?e=exzyWd)
## [Ganttplan](https://1drv.ms/x/s!An4Z2t_LGP8EgfdFcF29zzugesIIWw?e=vxi3Ss)
## [Møtereferat Fagskulen](https://1drv.ms/w/s!An4Z2t_LGP8EgftweCPkOZMYfNhzLg?e=A8fHtz)
# Logg-Bachelor

### 11.01.23 Daniel.
#### Industry 4.0 og HRC Kurs.

Idag gjennomførte jeg kursene for Industy 4.0 og HRC.

Industry 4.0 var nyttig fordi jeg lære mye om nye konsepter og begreper som vil være nyttige for bachelor rapporten vår.

Nyttige begreper:

Digital twin: 
Et virtuelt bilde av det virkelige produktet, som er i nåtid laget og utviklet.
Hensikten ved dette er å få virituell planlegging, verifisering og testen av mulige scenarioer før det faktisk skjer.
Dette er nyttig for dyre, og high quality products.

RFID-tags:
RFID står for "Radio frequency Identification" og bruker elektromagnetiske bølger for å identifisere objekter.
Dette er Transponder teknologi som spiller en økende viktig rolle i industrien, i tillegg til eksisterende automatiske identifikatorer som barcodes.
Fordeler med dette: Kontaktløs identifikasjon mellom chipen og sporer, så dette kan gjøres hensynsløst.
RFID kan også sende data til fysiske deler av fabrikken, dette kalles for cyber-physical systems.

Smart maintenance: 
Smart maintenance kombinerer konsepter av forutsigbar vedlikehold, maskin og prosess data analyse og kondisjonell monitering for intelegent vedlikehold.
Nøkkel forhold:
Dette linker sammen tradisjonelt vedlikehold som inspeksjoner, service, oppgraderinger og reprasjoner, med smarte sensorer/aktuatorer kombinert med 
forventingsfull software.

### 11.01.23 Josef.
Begynt å skrive forprosjektet. Utforming av dokumentet er ferdig.

### 11.01.23 Johannes
#### I4.0 og Ciros first steps kurs i festo learning
Fullførte industry 4.0 kurs mye generelt nyttig info. Fullførte også CIROS first step kurset og lister viktige punkter under

  Modell hierarki i CIROS MPS
  1. objects(en robot)
  2. groups (aksen av en robot)
  3. sleeves (den grafiske representasjon: en overflate eller kube f.eks)
  4. gripper points (sjette aksen til en robot arm)
  5. gripping points (work piece gripping point)
  
 I/O panel
  1. linje mellom input og output indikerer tilkobling
  2. farge av linjen indikerer verdi, ikke lik null grønn og lik null rød
  3. en output kan være koblet til mange input, men bare en output kan være koblet til hver input
  4. koblinger slettes alltid på siden av inputs for ryddighets skyld
  
 Programmering i CIROS
  1. F8 for å åpne teach in window for enkel programmering av robot arm. Kan brukes for å manuelt flytte på valgt kontroll objekt
  2. teach in window har både joint cordinate space og cartesian cordinate space
  3. posisjons liste programmeres i .mb4 filer og inneholder antall posisjoner en robot skal flyttes gjennom
  4. robot posisjon i kordinater (x,y,z og orientering av posisjon)
 
 Simulering i CIROS
  1.start/stopp shortcut f5
  2. Reset shortcut ctrl + F5
  3. Neste/forrige steg kommando (kun tilgjengelig hvis valgt vindu er enten posisjon liste eller en robot) shortcut F10

### 12.01.23 Daniel.
#### RFID intro kurs
The transponder is often referred to as the chip. The transponder has a globally unique serial number, which can be read out, but not overwritten. Often this is enough for identification, but the transponder is also able to store data, so if it´s desired, the user must determine the memory requirement of the chip.
The transponder also can have different design, depending on the use.

The RFID reading and writing devices are made up of an HF (high frequency) module, an antenna and a communication interface.
The HF and antenna is needed to create an electromagnetic field, to receive back data from the transponder. 
The communication interface is for data exchange with higher-order IT system. An IT system, e.g., a PLC uses the device for reading out or writing to transponders. 

The range of the RFID system we wants plays a big role, if we have wants a long range system, it can be cause a security problem.

Ranges:
Main interference include:
-Ambient conditions
-Materials
-Electromagnetic waves


### 12.01.23 Josef. 
Gjort ferdig kurs for industry 4.0. Fortsatt med skriving av forprosjekt og gjort alt eg kan med det før møte med veileder 13.01.23

### 13.01.23 Johannes
#### Introduksjons møte med HVL veilder Gerhard Nygaard

Tilstede
  Gerhard Nygaard
  Johannes Eidsvik
  Daniel Klepsvik
  Josef Heimset
  
 Bare kort introduksjon til hverandre og litt diskusjon om oppgaven fremover
 plan fremover å møtes hver fredag kl 10:30 på HVL M2 bygget
 
### 17.01.23 Daniel
Vi startet dagen med å fullføre registrering til fagskolen sitt IT system. Dermed fikk vi tilgang til google drive, som inneholder CIROS og Siemens TIA 15, som vi vil trenge. Problemet etter å ha kommet meg innpå google drive, var at det var en knapp som het «skjulte filer», oppe i høyre hjørne som ikke viste filene for meg. Men etter dette ble løst, kom jeg i gang med å laste ned Siemens TIA portal, der jeg lastet ned hele «SIEMENS» mappen.

Mens det holdt på å laste ned, lastet jeg ned VPN for å holde oss på skole nettet, slik at det er mulig å bruke CIROS uansett hvor vi er. Da gikk jeg inn på siden https://ssl.sfj.no/dana/home/index.cgi, og registrerte meg med brukernavn og passord + microsoft autenticator. Da ble jeg logget inn, og fikk lov å laste ned VPN’en. 

Når vi skal installere SIEMENS TIA, må vi laste ned hele mappen på google drive. Deretter på vi trykke innpå hver mappe, og trykke "start" filen. Den ønsker da å starte pc'en pånytt, for å så gi ut en feilmelding. Deretter vil du starte denne filen enda en gang, som da vil starte installasjons hjelper.

### 17.01.23 Johannes
#### Installasjon av VPN for lisens server
I dag ble vi registrert i fylkes kommunen sine systemer og fikk da tilgang til lisenser for CIROS og TIA v15. Har litt problemer med tilgang til google drive hvor filer for TIA v15 ligger så dette må løses senere, kom rundt dette for CIROS ved å laste ned CIROS 6 direkte fra festo sin nettside. Ellers lastet jeg ned VPN ivanta slik at jeg får tilgang til lisenser fra hvor som helst. Var noe problemer ved dette fikk blandt annet et SSL error som ble fikset ved å cleare SSL state på datamaskinen oppdaterer installasjons instruks dokument for å inkludere hvordan gjøre dette

### 17.01.23 Josef
Fått tilgang til kontoer og lisenser. Lastet ned CIROS 6.4 og gjort introduction to CIROS kurs på FESTO LX. Lastet ned VPN får å få tilgang til Fylkeskommunen sine nettsider og lisenser.

### 18.01.23 Daniel
I dag var Siemens programmet ferdig, så da skrev jeg installasjonsinstrukser. Når denne var ferdig skrevet, og lastet opp i Github, begynte jeg å laste ned CIROS. Mens jeg holdt på med dette, skrev jeg installasjonsinstrukser, inkludert problemer jeg møtte på underveis. Når Ciros var ferdig installert, lastet jeg filen opp i Github.

### 18.01.23 Josef
Fortsetter opplæring i CIROS både gjennom kurs og på egenhånd. Lastet ned TIA portalen v15 i forberedelse på å koble sammen TIA og CIROS.

### 18.01.23 Johannes
Dagen gikk til å få tilgang til google drive og laste ned programvare CIROS og TIA portal v15

### 19.01.23 Daniel
Idag begynte vi å teste PLS og CIROS sammen, med instruksjonsmalen vi fikk av Guttorm. Dette gikk fint, helt fram til jeg skulle starte begge simuleringene sammen, og samkjøre de. Da klikket CIROS, fikk opp feilmelding om at programmet ikke svarte, og det lukket seg automatisk. Dermed mistet jeg alt jeg hadde gjort i CIROS, og da gav eg meg for dagen.

### 19.01.23 Johannes
Idag fikk vi startet å prøve koble sammen CIROS og TIA. Vi fulgte oppskriften "PLCSIM-CIROS-Step-by-step" som vi har fått av Guttorm, kom så langt at vi fikk test kjørt problem er at CIROS henger seg helt opp med engang den kobler til PLCSIM

### 20.01.23 Johannes
#### Møtelogg
   
  Tilstede
  Gerhard Nygaard
  Johannes Eidsvik
  Daniel Klepsvik
  Josef Hellesen-Heimset
  
  1. Neste uke (27.01) gjennomgang av forprosjekt med Gerhard, hos bedriften han jobber i
  2. Ønske om å lage lab oppgaver i SCL til fagskole elevene siden skripting og høytnivå programmering er en viktig del av industrien. Hvilken hammer passer til            jobben?
  3. Fikk vist fram hvor langt vi er kommet i sammenkobling av TIA og CIROS
  4. Laget plan for videre utforming av forprosjekt
  5. Ny møteplass for møter fremover blir CDT, Thormølhensgate 49a Torsdager kl 1300
  6. Enighet om bruk av outlook fremover for organisering av møter

### 24.01.23 Daniel
Idag kjørte jeg PLS og CIROS sammen, dette fungerte fint uten at programmet kræsjet som sist. Jeg begynte å ekspremintere litt med å lage funskjonsblokk og skrive kode for å starte lyset på start knappen, når denne ble trykket inn. Dette gikk fint, videre startet jeg også belte på modulen, når start knappen ble trykket inn, som også fungerte. Problemet var at sourcen stoppet opp halveis på beltet og ville ikke kjøre lengre. Videre endte CIROS opp med å klikke litt, med at de nye opplastningene fra PLS´en ikke kom opp i CIROS. Prøve å stoppe PLS simmen, etter råd fra geniet Johannes, som endte opp med at hele CIROS klikket, og jeg måtte lukke CIROS og mistet alt... <br>
Nottat fra johannes: ikke skyld på mæ for at du gjør det feil idiot :hankey:

### 24.01.23 Johannes
Idag fortsatte jeg med å prøve å få CIROS og TIA til å samkjøre hvor jeg da møtte på en del problemer som jeg tror jeg fikk utredet. 
Uansett fikk CIROS og TIA til å samkjøre og bekreftet dette ved å se at taggen i TIA ble høy når start knappen ble trykket inn i CIROS.
under er en liste av problemene jeg møtte på og fikser 

  1. Problem med å laste opp prosjekt mapper på Github sin nettside siden de ikke lar en laste opp mer enn 100 filer omgange.
  Fiks er å benytte Github desktop å commit og pushe derfra ettersom den ikke har denne begrensningen
  2. Hvis noen utganger er feil i IO interfacen til den digitale PLSen i CIROS så henger CIROS ser opp når den kobler til PLCSIM advanced. 
  Fiks for dette er deklarer IO taggene rett og med adresse 42 isteden for 18. Hvis at CIROS fortsatt er hengt opp så kan det fikses med å starte PLCSIM instansen       pånytt eller slette instansen og lage en ny hvis ikke svenskemetoden går heller.
  3. IO tags må oppdateres i IO interface når de endres i TIA(pls programmet)

### 25.01.23 Daniel
Idag fortsatte jeg med det sammen, kjøre PLS og CIROS sammen. Jeg lastet ned programmene som Johannes har lastet opp. Det første problemet jeg møtte på, var at jeg ikke hadde riktig navn på PLCSIM instansen. Det ble fikset med at jeg lagde et nytt instansnavn med samme navn som PLS prosjektet mitt. Deretter måtte jeg laste opp prosjektet til simulatoren. Så måtte jeg inn på CIROS prosjetet, og skifte navn på simulatoren under SPS_A. Tok en sjekk på at I/O var riktig. Og da endte programmet opp med å kjøre godt. Da lagde jeg en funksjonsblokk som startet start knapp lyset, og beltet i framover rettning når startknappen ble trykket. Problemet da var at objektet ble stoppet midt på båndet, dette var pga inngang I1.4 ble høy. Dette er nok en simulering av CIROS av en RFID tag som gir signal om at objektet skal stoppe der.
 
 ### 25.01.23 Josef
 Begynte med å kjøre CIROS og TIA Portalen i lag, var på jobb når dei andre møtte i går så eg tok igjen det dei hadde gjort dagen før. 
 
 ### 25.01.23 Johannes
 Skrevet på forprosjekt rapport del drøfting av løsningner (2.2) og litt rettskriving og revidering ellers
 
 ### 26.01.23 Johannes
 Skrevet videre på forporsjekt rapport i forberedelse til møte med Gerhard senere idag
 
 ### 26.01.23 Josef
 ### Møtelogg
 
 Tilstede:
 Daniel Klepsvik <br>
 Gerhard nygaard <br>
 Johannes Eidsvik <br>
 Josef Hellesen-Heimset <br>

Planen for møtet denne gangen var hovedsaklig å vise fram forprosjektrapporten og få tilbakemelding på denne. Gerhard hadde flere forslag på ting vi kunne forbedre.

1. Lage eksempeloppgave for studentene på Fagskulen vi kan legge til i rapporten.
2. Legge inn element fra rapportmalen til HVL
3. Rette rapporten mer mot studentene på Fagskulen.

### Daniel 31.01.23
Idag skrev jeg kode for å få transportbåndet skulle virke. Jeg fikk det godt til, fikk endret at arbeidstykke stoppet på midten med PLS-en, dette gjorde jeg ved å endre Q1.7 til true, når carr.stopper.detectet ble true. Vidrer initialiserte jeg at hvis man trykket på reset btn så lyste den, og at båndet skiftet rettning det kjørte. Samt satt jeg meg inn i hvordan I/O oppbyggningen til CIROS fungerte.

### Johannes 31.01.23
Jobbet med forprosjekt rapport og skrevet ferdig valgt løsning (2.3)

### Josef 31.01.23
Jobbet litt med forprosjektrapporten, men hovedsaklig jobbet videre med modellen i CIROS og TIA

### Josef 01.02.23
Jobbet Videre med modellen min I CIROS og TIA. Laget ekstra funksjonalitet for knappene. Begynt å skrive kode i TIA som er i blokkdiagram og ikke SCL.

### Johannes 01.02.23
Skrevet videre på forprosjekt rapporten

### Johanens 02.02.23
Jobbet med forprosjekt rapport og møte med veileder ble flytte fra 02.02 til 03.02

### Josef 02.02.23
Arbeidet videre med modellen min i CIROS. Lagt på applokasjonsmodul og laget funksjonsblokk og tag-table for den.

### Daniel 07.02.23
Idag fikk jeg lagt til iDrill modulen til å stå oppå transportbåndet. Måten jeg gjorde dette på var ved å lagge den til fra "Model library", så fant jeg I/O på denne siden: https://ip.festo-didactic.com/InfoPortal/CPFactoryLab/hardware/application/datasheet.php?model=CP-AM-iDRILL&lang=en 
Deretter lagde jeg følgende I/O i tag table i TIA portalen. Det står på nettsiden at det er CECC I/O, men det funket helt fint å bruke disse som vanlig PLS I/O. Når disse var lagt inn i tag table, måtte jeg inn i SPS_A for CP_L_CONVEYOR, og la til de nye tagsene i CIROS. Når jeg såg at disse funket, koden jeg i fb´en, og gjorde slik at arbeidsstykket skulle stoppe på midten og bli borret på. Problemet med dette var at sourcen vår ikke gav arbeidstykke med front og bak deksel. Men jeg klarte å finne denne sourcen på en ferdiglaget drill inni model library. Når jeg fikk til denne fungerte drillen sånn halveis, neste steg vil være å legge til en timer som kan telle hvor lenge den skal borre fremme og bak på dekselet.

### Josef 07.02.23
Støtt på problemer med kontrollering av applikasjonsmodulen. Pressa kontrolleres vanligvis gjennom HMI-en og det kontrollsystemet er ikke tilgjgelig for meg. Prøver å finne en løsning på problemet men så langt uten hell. Har konaktet Guttorm for tilgang på forumet til FESTO CP og venter på å høre tilbakke.

### Johannes 07.02.23
Lest opp på navn konvensjoner i pls programmering fra plcopen og IEC. Ellers bare definert tag-table til lagerhus modellen og startet å gjøre meg kjent med modellen. Så langt kommet frem til at modellen har 2 pls-er 1 for transportbåndene og 1 for den kartesiske roboten

### Johannes 08.02.23
Jobbet videre med Highbay-storage modulen og gjort meg kjent med databladet til den. Merker spesielt nyttig med sekvens diagram i databladet

### Josef 08.02.23
Begynner arbeidet med å lage laboppgavene til studentene ved Fagskulen.

### Johannes 09.02.23
Lite fremgang idag mye problemere med CIROS som henger seg opp og diverse problemer daniel og josef har allerede utredet disse problemene før så jeg utdyper ikke her

### Johannes 09.02.23
#### Møtelogg
 Tilstede:
 Daniel Klepsvik <br>
 Gerhard nygaard <br>
 Johannes Eidsvik <br>

1. 1 tips Gerhard hadde til oss i dag var å få klar 1 oppgave så fort som mulig, Josef er allerede godt igang med oppgave 1 så han fortsetter på det
2. I oppgave 1b når vi sier modifiser programmet så kan jo dette introdusere feil i programmet har studentene ferdigheter til å debugge og feilsøke hvis bugs oppstår? Med dette i tankene må vi avklare med guttorm hvor studenten er i løpet i henhold til PLS programmering
3. Daniel viste frem en brukerveiledning han har laget i dokument form som Gerhard syntes var ganske bra Som da reiste spørsmålet om vi skal gå bort fra video for brukerveiledning. Kanskje dokument format passer bedre siden er lettere å finne fram i til en senere tid, mens video gir bruker kanskje en mer implisit forståelse når de blir vist nøyaktig hvordan
4. Legge til noe i forcetabel eller tag table slik at studentene får en forståelse for det også

### Johannes 14.02.23
Idag har jeg jobbet videre med Highbay-storage modulen. Det har vært lite fremgang i dag av synlige resultater, men har funnet ut endel om modulen. X og Z retningen til den cartesiske roboten styres via 2 servomotor-kontrollere av typen https://www.festo.com/net/SupportPortal/Files/380659/CMMP-AS-M3-HW_2012-03_760322g1.pdf via profinet. I morgen må jeg finne ut hvordan jeg kan skrive posisjons kommandoer fra hoved PLSen til servo motorene. Fant også ut hvordan å flytte roboten fra IO interfacen i CIROS ved å skrive verdier direkte til servocontroller target og så sette start utgangen høy.

### Josef 14.02.23
Fortstter arbeidet med laboppgavene, fokuserer på oppstartsmanualen i dag som vil være oppgave 1.

### Daniel 15.02.23
Idag jobbet jeg videre med å få timeren til iDrilling modulen til å fungere. Det fungerte sånn halvveis. Jeg la inn 3 timere som gjorde at det kan gå 5 sek med hver timer, der vi skal bruke 5 sek på å borre fremme, så 5 sek på å flytte borene bak, så 5 sek for å borre bak. Men problemet jeg møtte på var at alle timerene startet samtidig, som skapte problemer.

### Johannes 15.02.23
Jobbet videre med highbay storage ennå ikke funnet ut hvordan jeg kan styre servo-kontrollerene fra en tia pls

### Josef 15.02.23
Ferdigstiller laboppgave 1 idag før møte med Guttorm neste veke. Forventer litt tilbakemelding.

### Johannes 21.02.23
SpsA_lager har kanskje allerede noen utganger definert som ser ut til å gå til servo kontrollere så trenger kanskje ikke styre med bus ordning

### Møtereferat med veileder 23.02.23: 

    Lage en liste med typiske feilmeldinger 

    Ta skjermbilder av feil som skjer 

    Lage en Q&A i slutten av intro 

    Lage noen kontrollspørsmål på alle oppgaver 

    Eks oppg 1: hvor lenge stopper arbeidsstykke på midten, hvilke farge er arbeidsstykke? 

    Eks oppg 2: Hva skjer når de trykker på de forskjellige tingene? 


### Johannes 28.02.23
for å hente ut intern program fra ciros start en ferdig definert modell så minimer vinduet og vinduer med koden vises bakom
<br> notat: 0ca080f for blackmail av josef :smiling_imp:
utganger relevant for flytting av z og x akse i asrs32:

1. z_moveabs, x_moveabs
2. z_setpos, x_setpos
ref cpapplikasjon for virkemåte

### Møtereferat med Guttorm 15.03.23
#### Våre punkter:
•	Trenger vi å være til stede under lab testene? Siden vi har kanskje ikke tid pga. midtveispresentasjon. Kan legges opp til dette fra vår side.
•	Hvor lang tid får de til dispensasjon?
•	Har de CIROS og TIA lastet ned og klar?
•	Hvor mange laber kan vi få testet?
•	Kan vi gå ned og ta bilder av den fysiske fabrikken?
•	Johannes sin modul spørsmål.

#### Punkter underveid:
•	De er halveis i løpet, gjerne scl
•	Lage to zipper en oppgave og en løsning og sende til Guttorm
•	Får rikelig med tid
•	Kanskje klar CIROS til torsdag
•	13:20 – 15:45 på torsdag 23.03.23
•	Kan fordele labene på de
•	Kanskje skifte til nyere versjoner av TIA og SIM

#### Referat:
Vi skal møte klassen for å ha test oppgaver. De er 6 stk., de er halv veis i løpet, aka. holdt på i et år. De har holdt på med Python, men de kan ikke SCL. På torsdag er det fra 13:20-15:45, noen av de har forhåpentligvis fått lastet ned CIROS før dette, men vi må sannsynligvis hjelpe noen av de med nedlastning, før de kan starte med labbene. De får lengre tid enn kun torsdag, de har hele fredagen til rådighet, og eventuelt på nettet senere for å fullføre.

