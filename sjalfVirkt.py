#! /usr/bin/python3
import sys 


from notkun import *

DEBUG = False
DEBUG = True


def auto():
	print("\nValmöguleikar: (* krefst að fuzz sé enabled)")
	print("\t1: Fletta upp kyni á nafni")
	print("\t2: Fá kynja upplýsingar um nafn")
	print("\t3: Fá kynja upplýsingar um nafn með mögulega ranga lá og hástafi")
	print("\t4: Fá kynja upplýsingar um nafn sem er kannski með minniháttar villu *")
	print("\t5: Finna nafn, kannski með minniháttar villu *")
	print("\t6: Finna svipuð nöfn *")
	print("\t7: Lista öll nöfn, eftir lengd\n")

	val = input('\tþitt val: ') 
 

	try:
		val = int(val)
		if 1 <= val <=6:
			nafn = input('\tSláðu inn nafn: ')
			
			if val == 1:
				basic(nafn)
			elif val == 2:
				getInfoOnName(nafn)	
			elif val == 3:
				getInfoOnName(formatName(nafn))
			elif val == 4:
				print(getGenderOfNameFuzzy(nafn,0.7))
			elif val == 5:
				res = findNameFuzzy(nafn,0.8)
				for r in res:
					print(r)
			elif val == 6:
				getSimilarNames(nafn,0.6)
				
		elif val == 7:
			listAllNamesByLength()
		else:
			exit()
		


	except Exception as e:
		print("\n\n\tVilla í vali\n\tLoka Forriti\n")
		if DEBUG:
			print(e)
		exit()
auto()
