import csv
import os
from .resources import resources
from clinvoc.icd9 import ICD9PCS, ICD9CM
from clinvoc.icd10 import ICD10CM, ICD10PCS
import pickle
from clinvoc.code_collections import codecoll

# icd9_corrections = {'81.09': None,
#                     '06.88': '996.88',
#                     '428.83': None}
# icd10_correction = {}

def _read_file(filename):
    icd9cm_expanded_vocab = ICD9CM(use_decimals=True)
    icd9pcs_vocab = ICD9PCS(use_decimals=True)
    icd9mixed_vocab = ICD9CM(use_decimals=True) | ICD9PCS(use_decimals=True)
    icd10cm_vocab = ICD10CM(use_decimals=True)
    icd10pcs_vocab = ICD10PCS(use_decimals=True)
    icd10mixed_vocab = ICD10CM(use_decimals=True) | ICD10PCS(use_decimals=False)
    result = {}
    with open(filename, 'rb') as infile:
        reader = csv.reader(infile)
        reader.next()
        for row in reader:
            if row[3].strip().replace('/', '').upper() != 'NA':
                all_codes = icd9mixed_vocab.parse(row[3])
                result[(row[1], row[2], icd9cm_expanded_vocab.vocab_name)] = icd9cm_expanded_vocab.filter(all_codes)
                result[(row[1], row[2], icd9pcs_vocab.vocab_name)] = icd9pcs_vocab.filter(all_codes)
#                 res = (all_codes) - (result[(row[1], row[2], 'icd9cm')] | result[(row[1], row[2], 'icd9pcs')])
#                 if res:
#                     print 'icd9:', res
            if row[4].strip().replace('/', '').upper() != 'NA':
                all_codes = icd10mixed_vocab.parse(row[4])
                result[(row[1], row[2], icd10cm_vocab.vocab_name)] = icd10cm_vocab.filter(all_codes)
                result[(row[1], row[2], icd10pcs_vocab.vocab_name)] = icd10pcs_vocab.filter(all_codes)
#                 res = (all_codes) - (result[(row[1], row[2], 'icd10cm')] | result[(row[1], row[2], 'icd10pcs')])
#                 if res:
#                     print 'icd10:', res
    return result

try:
    with open(os.path.join(resources, 'cache.pickle'), 'rb') as infile:
        _code_sets = pickle.load(infile)
except:
    _code_sets = _read_file(os.path.join(resources, 'extracted_codes.csv'))
    with open(os.path.join(resources, 'cache.pickle'), 'wb') as outfile:
        pickle.dump(_code_sets, outfile)

Pccccs2Collection = codecoll('pcccs2', ['category', 'subcategory', 'vocabulary'])
code_sets = Pccccs2Collection(*_code_sets.items())

