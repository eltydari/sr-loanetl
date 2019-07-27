# -- FILE: features/steps/lib/assertions.py

def assertItemsEqual(observed, expected, message=''):
    assert len(observed) == len(expected) and sorted(observed) == sorted(expected), message