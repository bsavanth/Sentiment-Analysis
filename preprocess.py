import math
import string
def word2vec(f, choice, fll):

	poswords=[]
	negwords=[]
	pronouns = ["i", "me","mine","my","you","your","yours","we","us","ours"]
	negation = ["no","but","nothing","never","nope"]
	
	f1 = open('positive-words.csv', 'r+')
	for line in f1:
		poswords.append(line.strip())
	f1.close()
		
	f2 = open('negative-words.csv', 'r+')
	for line in f2:
		negwords.append(line.strip())
	f2.close()
	
				
	for line in f:
	
		x1=0
		x2=0
		x31=0
		x4=0
		Y=choice
		new_line =line.translate(str.maketrans('', '', string.punctuation))
		temp = new_line.split(" ")

		for token in temp:
			
			if token in poswords:
				x1+=1
			if token in negwords:
				x2+=1
			if token in negation:
				x31 = 1
			if token in pronouns:
				x4+=1
		x5 = math.log(len(temp))

		x32 = 1-x31 #dummy coded categorical variable
		
		final = str(x1)+','+str(x2)+','+str(x31)+','+str(x32)+','+str(x4)+','+str(x5)+','+str(Y)+'\n'
		fll.write(final)
		 
			
		
def main():


	fll = open('word2vec.txt', 'w')

	f1 = open('positive.txt', 'r+')
	word2vec(f1, 1, fll)
	f1.close()
	
	f2 = open('negative.txt', 'r+')
	word2vec(f2, 0, fll)
	f2.close()
	
	fll.close()
	
	
		
main()
 		