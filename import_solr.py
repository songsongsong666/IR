import csv
import re, sys, os, operator, math, collections
import numpy as np
from urllib.request import urlopen
import pysolr
import csv
import json
csv_path = 'path'
collection_name = 'project'
output = "myjson.json"
def processCsv(path):
	with open(path, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)
		header = []
		info = []
		row0 = next(csv_reader)
		cnt = 0
		for each in row0:
			header.append(each)
		for line in csv_reader:
			single = {}
			i = 0
			for each in line:
				single[header[i]] = each
				i+=1			
			if single['Species'] != '':
				cnt+=1
				info.append(single)
				
		print(str(cnt))
		return info



def toSolr(info, solr):
	solr.add(info, commit = True)
	print("finished processing")
	


def main():
	##connect to the local host of solr
	url = 'http://localhost:8983/solr/'+ collection_name
	solr1 = pysolr.Solr(url)

	solr1.delete(q='*:*') 	

	infos = processCsv(csv_path)

	toSolr(infos, solr1)
	

		



if __name__== "__main__":
	main()






