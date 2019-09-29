"""
PDFTranslate

Copyright (c) 2019 3x-boy

This software is released under the MIT License.
http://opensource.org/licenses/mit-license.php
"""


class test:
    """
    Write docstring in Numpy style

    Parameters
    ----------
    test : str
        Enter str type
    """

    def __init__(self, test_1="test_1"):
        """
        Write docstring in Numpy style

        Parameters
        ----------
        test_1 : str
            Enter str type, default "test_1"
        """
        self.test_1 = test_1


    def test(self, test_2):
        """
        Write docstring in Numpy style

        Parameters
        ----------
        test_2 : str
            Enter str type

        Returns
        -------
        self.test_1 : str
            Enter str type
        """
        print(test_2)

        return self.test_1