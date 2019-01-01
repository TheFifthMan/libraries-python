class Error(Exception):
    pass

class InputError(Error):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return self.message


def test_exception():
    i = 1 
    if i == 1:
        raise InputError("the number can't equal to 1")
    
try:
    test_exception()
except InputError as e:
    print(e)