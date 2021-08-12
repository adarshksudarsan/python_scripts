# importing required modules  
import PyPDF2
pagenumber = []
wordlist = []
#to convert a text file to list
with open("convert.txt") as file:
    listfile = []
    for line in file:
    	#checking is the line is empty or not
    	if line.strip():	
    		listfile.append(line.strip())
    print(listfile)
    print(len(listfile))
pdfFileObj = open('north.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
for i in range(0,456):
	pageObj = pdfReader.getPage(i)

	text=(pageObj.extractText())
	sentences=text.split(",")
	#text

    #keywords are given for searching inside pdf
	#search_keywords=['119371000006986','119371900001251']
	search_keywords = listfile



	for sentence in sentences:
		
		#print(sentence)
	    #lst = []
	    for word in search_keywords:
	        if word in sentence:
	        	print(word)
	        	wordlist.append(word)
	        	pagenumber.append(i+1)
	        	pagenumber.append(i+2)
	        	print("hurray",i)
print(pagenumber)
print(len(pagenumber))

#compare 2 list and find missing values 
set1 = set(listfile)
set2 = set(wordlist)

missing = list(sorted(set1 - set2))
added = list(sorted(set2 - set1))

print('missing:', missing)
print('added:', added)