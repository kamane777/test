# script by IJ 2017-11-30

# to count words

#################################
# STEP 1 >>> count the same words

from collections import Counter

i = 1			# count ALL files

while i <= 10 :

	open("stats_a%d_all.txt" % (i), "w")
	f = open("stats_a%d_all.txt" % (i), "a")

	r = open("rem_a%d.txt" % (i), "r")
#	r = open("zzzz%d.txt" % (i), "r")
	
	wordcount = Counter(r.read().split())
	for item in wordcount.items():
		#print("{}\t{}".format(*item))
#		f.write("{}\t{}\n".format(*item))
		f.write("{:30}{:7}\n".format(*item))
			
	
	i += 1

f.close()
r.close()

################################################################
# STEP 2 >>> remove non-existing words and count all words/score
	
from nltk.corpus import wordnet
	
a = 1

open("out0_stat.txt", 'w')
st0 = open("out0_stat.txt", 'a')

while a <= 10 :
	open("stats_a%d_few.txt" % (a), "w")
	out = open("stats_a%d_few.txt" % (a), "a")

	fil = open("stats_a%d_all.txt" % (a), "r")
	
	ln = 0	# count lines/words
	
	total_num = 0	# total number of words
	
	for line in fil :
		l = str(line)
		wo = l.split()[0]
		num = int(l.split()[1])
		
		total_num += num
		
		ln += 1
		
		if wordnet.synsets(wo):
			out.write("%s      %d \n" % (wo, num))
		else :
			print ("wrong word: %s" % (wo))
	
	st0.write("%02d   %d \n" % (a, total_num))
	print ("number of words in score %d is: %d. Total number of words is %d " % (a,ln, total_num))
	
	a += 1

st0.close()
fil.close()
out.close()

################################################################
# STEP 3 >>> remove non-existing words and count all words/score

n1=2067
n2=578
n3=649
n4=582
n5=586
n6=609
n7=957
n8=1469
n9=1093
n10=1410

from decimal import *

r_file = open("out0_stat.txt", 'r')
r_file.readline(0)

for line in r_file :
	l = str(line)
	x = int(l.split()[0])	# score
	tot = int(l.split()[1])			# total number of words in that score file
	
	open("stats_a%d_percent.txt" % (x), "w")
	out1 = open("stats_a%d_percent.txt" % (x), "a")

	fil = open("stats_a%d_few.txt" % (x), "r")
		
	for line in fil :
		h = str(line)
		wo = h.split()[0]
		num = int(h.split()[1])		# frequency of the same word that score file; to get percent = num/tot*100 %
			
		f_tot = float(tot)
		f_num = float(num)

		getcontext().prec = 8
		perc = Decimal(f_num) / Decimal(f_tot) * 100		
			
		print ("%s   %d    %.8f" % (wo,num, perc))
		out1.write("%s   %d    %.8f \n" % (wo,num, perc))
	out1.close()
	fil.close()
	x += 1
	
r_file.close()














