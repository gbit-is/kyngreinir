# kyngreinir.py 

Python forrit til að kyngreina íslensk nöfn og gagnasett með kynja-upplýsingum um íslensk nöfn (byggt á þjóðskrá 1997)   

( Python program to determine the gender of Icelandic names and a dataset with names and gender info on icelandic names, based on the 1997 "Registers Iceland")


## Skrár:

	
### genderedNames.json
Nöfn með hversu mörg kk/kvk hafa það 

### kyngreinir.py
Safn af python functions til að safna upplýsingum um nöfn

### notkun.py
Dæmi um notkun á kyngreini, ásamt functions sem expand-a eiginleika þess    
(sumir functions krefjast að Levenshtein pakkinn sé aðgengilegur fyrir fuzz matching)


Tjekka kyn á nafni   
Tjekka kyn á lista af nöfnum   
Lista öll nöfn eftir lengd   
Kyngreining með minimum matches og ásættanlegum frávikum   
Fá kynja info um nafn   
Nota nafn sem er ekki með há og lágstafi rétta   
Nota nafn sem er kannski smá vitlaust skrifað   
vitlaust skrifað með sér fuzz limit-i   
finna nafn sem er ekki alveg rétt skrifað   
Finna svipuð nöfn 

### sjalfVirkt.py
cli forrit sem spyr um valmöguleika til að nýta functions úr notkun.py   
býður uppá helstu functions sem er lýst í notkun.py

