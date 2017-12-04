# script by IJ 2017-11-29

# code removes non-latin symbols
# and
# extracts info from train data files into 4 separate files:
#	1. score + file name (i.e. file index) 					>>> all reviews
# 	2. file inddex + header									>>> reviews with the same score, i.e. separate filer per score
#	3. file index + review body text; one line per review 	>>> reviews with the same score, i.e. separate filer per score
#	4. file index + header + body; one line per review		>>> reviews with the same score, i.e. separate filer per score

import os
from unidecode import unidecode

open('test_score.txt', 'w')			# score + file name
ts = open('test_score.txt', 'a')

open('s1.txt', 'w')				# headers
s1 = open('s1.txt', 'a')
s1.close()
open('s2.txt', 'w')
s2 = open('s2.txt', 'a')
s2.close()
open('s3.txt', 'w')
s3 = open('s3.txt', 'a')
s3.close()
open('s4.txt', 'w')
s4 = open('s4.txt', 'a')
s4.close()
open('s5.txt', 'w')
s5 = open('s5.txt', 'a')
s5.close()
open('s6.txt', 'w')
s6 = open('s6.txt', 'a')
s6.close()
open('s7.txt', 'w')
s7 = open('s7.txt', 'a')
s7.close()
open('s8.txt', 'w')
s8 = open('s8.txt', 'a')
s8.close()
open('s9.txt', 'w')
s9 = open('s9.txt', 'a')
s9.close()
open('s10.txt', 'w')
s10 = open('s10.txt', 'a')
s10.close()

open('b1.txt', 'w')				# body text
b1 = open('b1.txt', 'a')
b1.close()
open('b2.txt', 'w')		
b2 = open('b2.txt', 'a')
b2.close()
open('b3.txt', 'w')	
b3 = open('b3.txt', 'a')
b3.close()
open('b4.txt', 'w')		
b4 = open('b4.txt', 'a')
b4.close()
open('b5.txt', 'w')		
b5 = open('b5.txt', 'a')
b5.close()
open('b6.txt', 'w')		
b6 = open('b6.txt', 'a')
b6.close()
open('b7.txt', 'w')		
b7 = open('b7.txt', 'a')
b7.close()
open('b8.txt', 'w')		
b8 = open('b8.txt', 'a')
b8.close()
open('b9.txt', 'w')		
b9 = open('b9.txt', 'a')
b9.close()
open('b10.txt', 'w')		
b10 = open('b10.txt', 'a')
b10.close()

open('a1.txt', 'w')				# header + review body
a1 = open('a1.txt', 'a')
a1.close()
open('a2.txt', 'w')		
a2 = open('a2.txt', 'a')
a2.close()
open('a3.txt', 'w')	
a3 = open('a3.txt', 'a')
a3.close()
open('a4.txt', 'w')		
a4 = open('a4.txt', 'a')
a4.close()
open('a5.txt', 'w')		
a5 = open('a5.txt', 'a')
a5.close()
open('a6.txt', 'w')		
a6 = open('a6.txt', 'a')
a6.close()
open('a7.txt', 'w')		
a7 = open('a7.txt', 'a')
a7.close()
open('a8.txt', 'w')		
a8 = open('a8.txt', 'a')
a8.close()
open('a9.txt', 'w')		
a9 = open('a9.txt', 'a')
a9.close()
open('a10.txt', 'w')		
a10 = open('a10.txt', 'a')
a10.close()

open('s0.txt', 'w')				# to catch errors
s0 = open('s0.txt', 'a')
s0.close()
open('b0.txt', 'w')		
b0 = open('b0.txt', 'a')
b0.close()


n1 = 0			# for statistics; counts reviews with the same score
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0
n0 = 0

cblank = 0		# count blanks
i = 0			# count file number

line_before = "blank"

while i <= 9999 :
	
	score = 0		# to catch errors
	
	read_file = open(os.path.join("C:/Users/Ilma/Documents/Applications_TASKS/VismaTestCase_Ilma/train/reviews%d.txt" % (i)), "r", encoding='utf-8')
	read_file.readline(0)
	
#	open("Reviews_%d.txt" % (i), "w")
#	train_file = open("Reviews_%d.txt" % (i), "a")
	
	for line in read_file :		
		s = str(line)
		L = unidecode(s)	# unidecoded line
		L.encode("ascii")	

#		train_file.write(L)		# creates unicoded files
		
		LL = L[:-1]
		LL_len = len(LL)
		
		#print (s)
		#print (L)
				
				# extracting score (4 cases)
				
				# 1/4 >> for normal coding with one score digit (1 to 9)
		if  line_before== "blank" and L not in ("\n", "\r\n") and L[0] in ("1", "2", "3", "4", "5", "6", "7", "8", "9")  and L[1] != "0" and LL_len <=2 and LL.isdigit() == True:
			score = int(L[0])
			
			print (score, type(score))
			ts.write("%02d :  reviews%d.txt \n" % (score,i))
			line_before = "score"
			if   score == 1 : n1+=1		# counts reviews ith the same score
			elif score == 2 : n2+=1
			elif score == 3 : n3+=1
			elif score == 4 : n4+=1
			elif score == 5 : n5+=1
			elif score == 6 : n6+=1
			elif score == 7 : n7+=1
			elif score == 8 : n8+=1
			elif score == 9 : n9+=1
			elif score == 10 : n10+=1

				# 2/4 >> for normal coding with two score digits (exact 10)
		if  line_before== "blank" and  L not in ("\n", "\r\n") and L[0] == "1" and L[1] == "0" and LL_len <=2 and LL.isdigit() == True :
			score = int(L[0:2])
			
			print (score, type(score))
			ts.write("%02d :  reviews%d.txt \n" % (score,i))
			line_before = "score"
			if   score == 1 : n1+=1		# counts reviews ith the same score
			elif score == 2 : n2+=1
			elif score == 3 : n3+=1
			elif score == 4 : n4+=1
			elif score == 5 : n5+=1
			elif score == 6 : n6+=1
			elif score == 7 : n7+=1
			elif score == 8 : n8+=1
			elif score == 9 : n9+=1
			elif score == 10 : n10+=1

				# 3/4 >> for NOT NORMAL coding with one score digit (1 to 9)
		elif line_before== "blank" and L not in ("\n", "\r\n") and L[0] not in ("1", "2", "3", "4", "5", "6", "7", "8", "9") and L[1] in ("1", "2", "3", "4", "5", "6", "7", "8", "9") and L[2] != "0" and LL_len <=2 and LL.isdigit() == True :
			score = int(L[1])

			print (score, type(score))
			ts.write("%02d :  reviews%d.txt \n" % (score,i))
			line_before = "score"
			if   score == 1 : n1+=1		# counts reviews ith the same score
			elif score == 2 : n2+=1
			elif score == 3 : n3+=1
			elif score == 4 : n4+=1
			elif score == 5 : n5+=1
			elif score == 6 : n6+=1
			elif score == 7 : n7+=1
			elif score == 8 : n8+=1
			elif score == 9 : n9+=1
			elif score == 10 : n10+=1

				# 4/4 >> for NOT NORMAL coding with two score digits (exact 10)			
		elif line_before== "blank" and L not in ("\n", "\r\n") and L[0] not in ("1", "2", "3", "4", "5", "6", "7", "8", "9") and L[1] == "1" and L[2] == "0" and LL_len <=2 and LL.isdigit() == True :
			score = int(L[1:3])
			
			print (score, type(score))
			ts.write("%02d :  reviews%d.txt \n" % (score,i))
			line_before = "score"
			if   score == 1 : n1+=1		# counts reviews ith the same score
			elif score == 2 : n2+=1
			elif score == 3 : n3+=1
			elif score == 4 : n4+=1
			elif score == 5 : n5+=1
			elif score == 6 : n6+=1
			elif score == 7 : n7+=1
			elif score == 8 : n8+=1
			elif score == 9 : n9+=1
			elif score == 10 : n10+=1
					
					# catch score errors
		elif line_before == "blank" and L not in ("\n", "\r\n") and L[0] not in ("1", "2", "3", "4", "5", "6", "7", "8", "9") and L[1] not in ("1", "2", "3", "4", "5", "6", "7", "8", "9") and L[2] != "0" and LL_len <=2 :
			score = 0
			n0 += 1
			line_before = "score"
			print (score, type(score))
			ts.write("%02d :  reviews%d.txt \n" % (score,i))

			
						
				# extracting header
		elif line_before == "score" and isinstance(line,str) == True and L not in ("\n", "\r\n") and LL_len >= 1 and LL.isdigit() ==  False :
			sf = open("s%d.txt" % (score), "a")
			sf.write("%04d :  %s" % (i,L))	
			sf.close()

			af = open("a%d.txt" % (score), "a")
			af.write("%04d :  %s " % (i,LL))	

			line_before = "header"
			
				# Extracting blank
		elif L in ("\r\n", "\n") and line_before == "header":
			print ("blank=%d" % cblank)
			cblank += 1
			line_before = "blank_for"
				
				# initiate body text file
			bf = open("b%d.txt" % (score), "a")
			bf.write("%04d :  " % (i))
			bf.close()			
			
				# Extracting review body text
				
		elif isinstance(line, str) == True and line_before in ("blank_for", "body") :
			bf = open("b%d.txt" % (score), "a")
			bf.write("%s " % (LL))
			
			af.write("%s " % (LL))	

			line_before = "body"
			
	bf.write("\n")		# puts end for comment line
	bf.close()

	af.write("\n")		# puts end for comment line
	af.close()
	
	i += 1
	line_before = "blank"
	
	
print ("STATISTICS: n1=%d, n2=%d, n3=%d, n4=%d, n5=%d, n6=%d, n7=%d, n8=%d, n9=%d, n10=%d, n0=%d" % (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n0))	
	
nall = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n0

print (">>>  %d   <<<  reviews in total" % (nall))