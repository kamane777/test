# script by IJ 2017-11-20
# check for wrong decodin/encoding files

import os
from unidecode import unidecode

i = 0

while i <= 9999 :

	read_file = open(os.path.join("C:/Users/Ilma/Documents/Applications_TASKS/VismaTestCase_Ilma/train/reviews%d.txt" % (i)), "r", encoding='utf-8')
	read_file.readline(0)

	open("Reviews_%d.txt" % (i), "w")
	re = open("Reviews_%d.txt" % (i), 'a')

	for line in read_file :
		s = str(line)
		t = unidecode(s)
		t.encode("ascii")
		re.write(t)

	print ("done:  review_%d" % (i))
		
	i += 1


#f = codecs.open("nump_HeadBody_train.txt", encoding='utf-8', errors="replace")
#for line in f :
#	l = str(line)
#	L = l[:-1]
#	try:
#		l.encode().decode('utf-8')
#		print(l)
#		print (LL)
#		re.write(L)
		
#	except UnicodeError :
#		print ("---error %d --- %s" % (error_num, l))
#		re.write("error \n")

		
		