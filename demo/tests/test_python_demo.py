import unittest


class TestPythonDemo(unittest.TestCase):
    def test_return_const_str(self):
        from demo.src.python_demo import return_const_str
        self.assertEqual("const_str", return_const_str())

    def test_return_input(self):
        from demo.src.python_demo import return_input
        self.assertEqual("test_input", return_input("test_input"))

    def test_numpy_demo(self):
        from demo.src.python_demo import numpy_demo
        import numpy as np
        from numpy.testing import assert_array_equal
        expected = np.array([0, 1, 2])
        assert_array_equal(np.array_str(expected), numpy_demo())

    # def test_pandas_demo(self)
    #     from demo.src.python_demo import pandas_demo:
    #     from numpy.testing import assert_array_equal
    #     from pandas import DatetimeIndex
    #     expected = DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03'], dtype='datetime64[ns]', freq='D')
    #     assert_array_equal(expected, pandas_demo())

if __name__ == "__main__":
    unittest.main()
