## [Timeliste](https://1drv.ms/x/s!An4Z2t_LGP8Egfc6DhIkCmNc5jDyEw?e=exzyWd)
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

### 19.01.23 Daniel
Idag begynte vi å teste PLS og CIROS sammen, med instruksjonsmalen vi fikk av Guttorm. Dette gikk fint, helt fram til jeg skulle starte begge simuleringene sammen, og samkjøre de. Da klikket CIROS, fikk opp feilmelding om at programmet ikke svarte, og det lukket seg automatisk. Dermed mistet jeg alt jeg hadde gjort i CIROS, og da gav eg meg for dagen.

### 20.01.23 Johannes
#### Møtelogg
   
  Tilstede
  Gerhard Nygaard
  Johannes Eidsvik
  Daniel Klepsvik
  Josef Heimset
  
  1. Neste uke (27.01) gjennomgang av forprosjekt med Gerhard, hos bedriften han jobber i
  2. Ønske om å lage lab oppgaver i SCL til fagskole elevene siden skripting og høytnivå programmering er en viktig del av industrien. Hvilken hammer passer til            jobben?
  3. Fikk vist fram hvor langt vi er kommet i sammenkobling av TIA og CIROS
  4. Laget plan for videre utforming av forprosjekt
  5. Ny møteplass for møter fremover blir CDT, Thormølhensgate 49a Torsdager kl 1300
  6. Enighet om bruk av outlook fremover for organisering av møter
