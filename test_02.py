class Test_pytest02():
    def test_add(self):
        a = 10
        b = 20
        sum =  a + b
        print("Addition :",sum)
        if sum == 30:
            assert True
        else:
            assert False
