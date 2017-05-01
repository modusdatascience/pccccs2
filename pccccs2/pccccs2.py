import csv
import os
from .resources import resources
from clinvoc.icd9 import ICD9CM
from clinvoc.icd10 import ICD10CM


def _read_file(filename):
    icd9_vocab = ICD9CM()
    icd10_vocab = ICD10CM()
    icd9 = {}
    icd10 = {}
    with open(filename, 'rb') as infile:
        reader = csv.reader(infile)
        reader.next()
        for row in reader:
            
            try:
                if row[3].strip().replace('/', '').upper() != 'NA':
                    icd9[(row[1], row[2])] = icd9_vocab.parse(row[3], delimiters=',.')
            except:
                print row[3]
                raise
            try:
                if row[4].strip().replace('/', '').upper() != 'NA':
                    icd10[(row[1], row[2])] = icd10_vocab.parse(row[4])
            except:
                print row[4][130:]
                raise
    
    return icd9, icd10

icd9cm_code_sets, icd10cm_code_sets = _read_file(os.path.join(resources, 'extracted_codes.csv'))