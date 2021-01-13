#! /usr/bin/python3

import json



nameDataFile = "genderedNames.json"
nameData = None

enableFuzz = True
enableFuzz = False

if enableFuzz:
	try:
		import Levenshtein as lev
	except:
		print("Cannot import import Levenshtein")
		print("Disable the feature or install the module")
		exit()


def findNameFuzzy(name,fuzzLimit):

	namesToFuzz = getNameList("all","return")
	fuzzMatches = [ ]

	for tsName in namesToFuzz:
		tsName = tsName[0]
		fuzzLevel = lev.ratio(name,tsName)
		if fuzzLevel > fuzzLimit:
			fuzzMatches.append([tsName,fuzzLevel])
	return fuzzMatches


def getGenderOfNameFuzzy(name,fuzzLimit=0.8,minimumMatches = 10,tolerance = 3,verbose = False):

	normal_attempt = getGenderOfName(name,minimumMatches,tolerance,verbose)	
	if normal_attempt != "no_match":
		return normal_attempt
	namesToFuzz = getNameList("all","return")

	fuzzMatches = [ ]

	for tsName in namesToFuzz:
		tsName = tsName[0]

		fuzzLevel = lev.ratio(name,tsName)

		if fuzzLevel > fuzzLimit:
			fuzzMatches.append([tsName,fuzzLevel])

	if len(fuzzMatches) == 0:
		return "no_fuzz_match"
	elif len(fuzzMatches) > 1:
		#print(fuzzMatches)
		return "multiple_fuzz_matches",fuzzMatches
		
	fuzzName = fuzzMatches[0][0]

	fuzz_attempt = getGenderOfName(fuzzName,minimumMatches,tolerance,verbose)
	return fuzz_attempt


def getNameList(type = "all",method = "print"):

	if not nameData:
		loadNameData()

	nameList = [ ]

	if type == "all":
		for name in nameData:
			#print(name,nameData[name])
			nameList.append([name,nameData[name]])
	elif type == "male":
		for name in nameData:
			if getGenderOfName(name) == "kk":
				nameList.append(name)
				#print(name)
	elif type == "female":
		for name in nameData:
			if getGenderOfName(name) == "kvk":
				nameList.append(name)
				#print(name)
	elif type == "unsure":
		unsureList = [ ]
		for name in nameData:
			if getGenderOfName(name) == "na":
				nameList.append(name)
				#print(name)

	if method == "print":
		for name in nameList:
			print(name)
	elif method == "return":
		return nameList
	



def loadNameData():
	global nameData

	try:
		with open(nameDataFile) as json_file:
			nameData = json.load(json_file)
	except:
		print("Unable to load genderedNames.json")

			
def unLoadNameData():
	global nameData
	nameData = None

def lookupName(name):
	if not nameData:
		loadNameData()

	if name in nameData:
		return True, nameData[name]
	else:
		return False, None
		
def getGenderOfName(name,minimumMatches = 10,tolerance = 3,verbose = False):
	
	match,data = lookupName(name)
	if not match:
		if not verbose:
			return "no_match"
		else:
			print("The name: " + str(name) + " was not found.")
			return "no_match"
		
	if verbose:
		#print(match,data)
		pass

	kk = data["kk"]
	kvk = data["kvk"]
	entries = kk + kvk

	if entries < minimumMatches:
		if verbose:
			print("Not enough matches to know what gender: " + str(name) + " is")
		return "na"
	
	
	if kk == kvk:
		if verbose:
			print("Equal number of KK and KVK with name: " + str(name))
		return "na"

	elif kk > kvk:
		gender = "kk"
		if kvk == 0:
			return gender
		if verbose:
			print(str(name) + " is mostly a KK name but there is/are: " + str(kvk) + " KVK who have it")

		overlap = kvk / kk 
		overlap = overlap * 100

		if overlap < tolerance:
			return gender

		else:
			gender = "na"
			return gender


	elif kvk > kk:
		gender = "kvk"
		
		if kk == 0:
			return gender
	
		if verbose:
			print(str(name) + " is mostly a KK name but there is/are: " + str(kvk) + " KVK who have it")
		overlap = kk / kvk
		overlap = overlap * 100

		if overlap < tolerance:
			return gender 
		else:
			gender = "na"
			return gender

def formatName(name):
	name = name.capitalize() 
	return name



