def encodage():
	with open('/home/aline/Documents/BDDR/catalogue.sql','r') as f:
		a = f.readlines()
	liste = []
	for line in a:
		car1 = "Ã©"
		car2 = "Ã¨"
		car3 = "Ãª"
		car4 = "Ã¤"
		car5 = "Ã¶"
		car6 = "Ã¹"
		car7 = "Ã¸"
		car8 = "Ã¯"
		car9 = "Ã«"
		car10 = "Ã¡"
		car11 = "Ã¢"
		car12 = "Ã§"
		car13 = "Â°"
		car14 = "Ã´"
		car15 = "Ã®"
		car16 = "Ã"
		car17 = "\\"
		if car1 == "Ã©":
			l1 = line.replace("Ã©","é")
			#~ liste.append(l1)
		if car2 == "Ã¨" :
			l2 = l1.replace("Ã¨","è")
			#~ liste.append(l2)
		if car3 == "Ãª" :
			l3 = l2.replace("Ãª","ê")
			#~ liste.append(l3)
		if car4 == "Ã¤" :
			l4 = l3.replace("Ã¤","ä")
			#~ liste.append(l4)
		if car5 == "Ã¶" :
			l5 = l4.replace("Ã¶","ö")
			#~ liste.append(l5)
		if car6 == "Ã¹" :
			l6 = l5.replace("Ã¹","ù")
			#~ liste.append(l6)
		if car7 == "Ã¸" :
			l7 = l6.replace("Ã¸","ø")
			#~ liste.append(l7)
		if car8 == "Ã¯" :
			l8 = l7.replace("Ã¯","ï")
			#~ liste.append(l8)
		if car9 == "Ã«" :
			l9 = l8.replace("Ã«","ë")
			#~ liste.append(l9)
		if car10 == "Ã¡" :
			l10 = l9.replace("Ã¡","á")
			#~ liste.append(l10)
		if car11 == "Ã¢" :
			l11 = l10.replace("Ã¢","â")
			#~ liste.append(l11)
		if car12 == "Ã§" :
			l12 = l11.replace("Ã§","ç")
			#~ liste.append(l12)
		if car13 == "Â°" :
			l13 = l12.replace("Â°","°")
			#~ liste.append(l13)
		if car14 == "Ã´" :
			l14 = l13.replace("Ã´","ô")
			#~ liste.append(l14)
		if car15 == "Ã®" :
			l15 = l14.replace("Ã®","î")
			#~ liste.append(l15)
		if car16 == "Ã" :
			l16 = l15.replace("Ã","à")
			#~ liste.append(l16)
		if car17 == "\\" :
			l17 = l16.replace("\\","")
			liste.append(l17)
		else:
			liste.append(line)
	return(liste)

res = encodage()
#~ print(res)

g = open("nouv_cata","w")
for i in res:
	g.write(i)
g.close()

# ceci est un test pour git !!! >.<
