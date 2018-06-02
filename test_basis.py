# -*- coding: utf-8 -*-

def changeZero(L):
	for x in range(len(L)-1):
		if L[x] == 0:
			L[x] = -100

def changeBack(L):
	for x in range(len(L)-1):
		if L[x] == -100:
			L[x] = 0

L = [0,-23,0,-45,0,-35]
changeZero(L)
print (L)
changeBack(L)
print (L)

L = ["czm","sy"]
L1 = ["czm","sy"]

if L[0] == L1[0]:
	print ("YES")