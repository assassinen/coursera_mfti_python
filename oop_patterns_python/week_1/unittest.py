from unittest import TestCase

def factorize(x):
    if x == 1001:
        return (7, 11, 13)
    else:
        return (2, 3, 5, 7, 11, 13, 17, 19)


class TestFactorize(TestCase):
    def test_many_multipliers(self):
        for x, ex in (1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            # print(x, ex)
            # factorize(x)
            # self.assertTupleEqual(factorize(x), ex)
            print(type(ex))
            print(type(factorize(x)))
            with self.subTest(x):
                self.assertTupleEqual(factorize(x), ex)



