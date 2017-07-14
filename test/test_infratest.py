import infratest
import nose
import os

def _standup_file_exists(path):
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            f.write('file exists test')

def _cleanup_file_exists(path):
    os.remove(path)

def test_file_exists():
    test_file_path = "./test/file_exists"
    _standup_file_exists(test_file_path)
    result_dict = infratest.file_exists(test_file_path, True)
    nose.tools.eq_(len(result_dict['Passed']), 1, msg=result_dict)
    _cleanup_file_exists(test_file_path)
