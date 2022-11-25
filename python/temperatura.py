import numpy
import matplotlib.pyplot as plt

def CtoK(T):
	return T + 273.15

Ti = 10
Tf = 30
dT = (Tf-Ti)/10

print("i TC TK")
for i in range(0,9):
	T = Ti + i*dT
	Tk = CtoK(T)
	print(i, T, Tk)
