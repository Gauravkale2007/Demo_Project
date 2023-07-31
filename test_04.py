class Test_pytest_03():
    def test_mul(self):
        a = 5
        b = 4
        result = a * b
        print("Multiplication:",result)
        if result==20:
            assert True
        else:
            assert False
