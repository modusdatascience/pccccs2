from pccccs2.pccccs2 import code_sets
from clinvoc.icd10 import ICD10CM, ICD10PCS
from clinvoc.icd9 import ICD9CM, ICD9PCS
from nose.tools import assert_equal


def test_code_sets():
    icd9cm = ICD9CM()
    icd9pcs = ICD9PCS()
    icd10cm = ICD10CM()
    icd10pcs = ICD10PCS()
    for k, v in code_sets.items():
        assert k[-1] in {'icd9cm', 'icd10cm', 'icd9pcs', 'icd10pcs'}
        if k[-1] == 'icd9cm':
            assert_equal(icd9cm.filter(v), v)
        elif k[-1] == 'icd10cm':
            assert_equal(icd10cm.filter(v), v)
        if k[-1] == 'icd9pcs':
            assert_equal(icd9pcs.filter(v), v)
        elif k[-1] == 'icd10pcs':
            assert_equal(icd10pcs.filter(v), v)

if __name__ == '__main__':
    import sys
    import nose
    # This code will run the test in this file.'
    module_name = sys.modules[__name__].__file__

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-s', '-v'])