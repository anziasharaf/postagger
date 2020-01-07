

def main_program(infile):
	print(infile)
	from POSTagging import POStagger
	file1=open(infile,"r")
	f=open("out.txt","w")
	line=file1.readlines()
	print(line)
	for content in line:		
		tokens=content.split(' ')
		print(tokens)
		for item in tokens:
			f.write("%s\n" % item)



	
	f.close()
	file1.close()
	POStagger.postagger()
	bad_words =['%']
	with open('tagged_text.txt') as oldfile, open('newfile.txt', 'w') as newfile:
		for line in oldfile:
			if not any(bad_word in line for bad_word in bad_words):
            			newfile.write(line)
	newfile.close()
	file3=open('newfile.txt','r')
	file_contents = file3.read()
	print (file_contents)
	file3.close()
	return file_contents
