from contextlib import closing

class TestObj():
    def __init__(self):
        print("init test obj")
    def test(slef):
        print("test")
    def close(self):
        print("close")
    

with closing(TestObj()) as t:
    t.test()