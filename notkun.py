#! /usr/bin/python3
import sys 


from kyngreinir import *



def basic(name):
	kyn = getGenderOfName(name)
	print(str(name).ljust(17) + " er " + kyn + " nafn")

def multipleNames(names):

	for name in names:
		basic(name)



def listAllNamesByLength():
	names = getNameList("all","return")
	nameList = [ ]
	
	for name in names:
		nameList.append(name[0])

	nameList = list(sorted(nameList, key = len))

	for name in nameList:
		print(name)
	

def advanced(name):
	
	# Lágmarks magn af fólki í þjóðskrá með þetta sem fyrsta nafn til þess að gögnin á bakvið nafnið teljist trúverðuleg
	mm = 20

	# Ef nafn er til sem bæði kk og kvk, þá er þetta hámarks fráviks prósenta sem er leyfð
	# Segjum að 100 manneskjur heiti "Skrifborð" 
	# af þeim eru 97 kk og 3 kvk 
	# þá með að hafa mp sem 3 er það ásættanlegt frávik, en ef mp er 2 þá er það of mikið frávik og kynið verður "na"
	mp = 4

	data = getGenderOfName(name,mm,mp)
	print(data)


def getInfoOnName(name):
	match,data = lookupName(name)

	if match:
		kk = data["kk"]
		kvk = data["kvk"]

		print("Nafn: " + str(name))
		print("KK  með nafnið:  " + str(kk))
		print("KVK með nafnið: " + str(kvk))
	else:
		print("Nafnið: " + str(name) + " fannst ekki í þessu gagnasetti :(")

def getSimilarNames(name,fuzzLevel):
	fuzzMatches = findNameFuzzy(name,fuzzLevel)

	fuzzMatches = sorted(fuzzMatches, key = lambda x: x[1])
	
	ll = [ ]
	for m in fuzzMatches:
		ll.append(len(m[0]))
	ll = max(ll) + 2


	for match in fuzzMatches:
		name = match[0] 
		name = name.ljust(ll) 
		fuzz = match[1]
		fuzz = fuzz * 100
		fuzz = round(fuzz,2)
		print(name + " : " + str(fuzz) + "%")

### Tjekka kyn á nafni, basic
#basic("Sigfús")

### Tjekka kyn á lista af nöfnum
#multipleNames([ "Sigfús","Jónína","Pétur","Ína","lampi" ])

### Lista öll nöfn eftir lengd
#listAllNamesByLength()

### Kyngreining með minimum matches og ásættanlegum frávikum
#advanced("Sigfús")

### Fá kynja info um nafn
#getInfoOnName("sigfús")

### Nota nafn sem er ekki með há og lágstafi rétta
#getInfoOnName(formatName("SIGFÚS"))

##################
#
# ALLT FYRIR NEÐAN KREFST AÐ FUZZ SÉ ENABLED Í kyngreinir.py
#
#################


### Nota nafn sem er kannski smá vitlaust skrifað 
#print(getGenderOfNameFuzzy("Sigfus"))

### vitlaust skrifað með sér fuzz limit-i (og finnur svo ekki rétt nafn, fuzz er ekki fullkomið) ´
#print(getGenderOfNameFuzzy("Sygfus",0.7))

### bara finna nafn sem er ekki alveg rétt skrifað
#print(findNameFuzzy("Sigfus",0.8))

### Finna svipuð nöfn 
#getSimilarNames("Sigfús",0.6)

