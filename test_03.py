class Test_pytest04():
    def test_div(self):
        a = 10
        b = 2
        Result = a/b
        print("Division is :", Result)
        if Result ==5:
            assert True
        else:
            assert False
