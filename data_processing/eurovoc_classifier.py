#this whole thing is obsolete, i did not bother to finish it up properly, it has been replaced with a keyword extraction of a fixed top5 keyphrase output

import os
import subprocess
import shutil
import re
import unicodedata
from bs4 import BeautifulSoup
import sys


eurovoc_folder = '/en-eurovoc-1.0/'
tempfile = 'tempfile.txt'
document_folder = os.path.join(eurovoc_folder, "documents")
result_folder = os.path.join(eurovoc_folder, "result", "PostProcessedDocs")

# clean Eurovoc document folder
if os.path.exists(document_folder):
    shutil.rmtree(document_folder)
    os.mkdir(document_folder)

# clean Eurovoc results folder
if os.path.exists(result_folder):
    shutil.rmtree(result_folder)


def generate_eurovoc_classifications(text):

	#create path with temporary file name
	text_file = open(os.path.join(document_folder, tempfile), "w")
	n = text_file.write(text)
	text_file.close()

	# run Eurovoc classifier
	os.chdir(os.path.join(eurovoc_folder, "bin"))
	subprocess.run('. ./AllInOneStep.sh', shell=True)

	textfile = open(os.path.join(result_folder, tempfile), 'r')
	text = textfile.read()
	textfile.close()
	if text=='':
		return ''


	soup = BeautifulSoup(text,'xml')
	# Extract all categories and weights
	for cat in soup.find_all('category'):
	# List of BroaderTerms
		bt = []
		for term in cat.find_all('BroaderTerm'):
	    		bt.append(term['label'])
	# List of RelatedTerms
		rt = []
		for term in cat.find_all('RelatedTerm'):
			rt.append(term['label'])

	eurovoc = {           'category' : cat['label'],
		              'weight': float(cat['weight']),
		              'broader_terms': bt,
		              'related_terms': rt}
	
	return eurovoc
