from pccccs2.pccccs2 import icd9cm_code_sets, icd10cm_code_sets

def test_code_sets():
    for k, v in icd9cm_code_sets.items():
        print str(k) + ': ' + str(v)
    
    for k, v in icd10cm_code_sets.items():
        print str(k) + ': ' + str(v)

if __name__ == '__main__':
    import sys
    import nose
    # This code will run the test in this file.'
    module_name = sys.modules[__name__].__file__

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-s', '-v'])