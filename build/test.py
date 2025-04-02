from build.utils import functionality

def test():
    res = functionality(4)
    if "False" in res or "0" in res:
        print("TESTS PASSED")
    else:
        print("TESTS FAILED")