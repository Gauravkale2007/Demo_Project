class Test_pytest_01():
    def test_sub(self):
        a = 20
        b = 5
        sub = a - b
        print("Substraction :",sub)
        if sub==15:
            assert True
        else:
            assert False
