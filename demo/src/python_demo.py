def return_const_str():
    return "const_str"


def return_input(input):
    return input


def numpy_demo():
    import numpy as np
    print('numpy version: %s' % np.__version__)
    res = np.arange(3)

    # serialize by converting to string
    serialized = np.array_str(res)

    return serialized

# def pandas_demo():
#     import pandas as pd
#     print('pandas version: %s' % pd.__version__)
#     return pd.date_range('20170101', periods=3)

