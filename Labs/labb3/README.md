# Laboration 3: Linjär Klassificering.
Syftet med denna laboration är att utföra en linjär klassificering av datapunkter genom att passa en linje som delar dem så jämnt så möjligt. 
### Steg 1:
 - Första steget är att importera olika python-bibliotek såsom: pandas(hantera datan i filen), matplotlib(plotting av grafer) och numpy(numeriska beräkningar).

### Steg 2: read_data funktion
 - Läsa in data från filen.
 - Dela data i två olika listor(first column, second column).
 - Returnera datan och listorna.

### Steg 3: plotting_data funktion 
 - Anropa datan och plotta punkterna på en graf. 
 - Passa en linje av formen 'y = kx + m' coh visa den i grafen.
 - Returnera värdena för 'k, m'.
### Steg 4: classify_points funktion

 - En tom lista.
 - For loop för att gå igenom datapunkter och avgöra om de ligger ovenför eller under linjen:
  - Lägg till 1 i listan om punkten är ovanför linjen.
  - Lägg till 0 i listan om punkten är under linjen.
 - Lägg den nya kolumnen i datan.
 - Spara den nya data i en ny fil.
 - En graf visar datapunkter med olika färger. 
 - Räkna och skriv ut antalet punkter.
 
### Körning:
 - Anropa alla funktioner för att läsa in data och köra porgramet.
 - Efter körning kommer programmet att generera en file'labelled_data.csv'.