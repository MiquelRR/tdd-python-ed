import pytest

from ejercicios.operaciones import *

class DivisionTestClass:

    def test_division(self):
        assert division(5,2) == 2.5
        assert division(-1,-2) == .5
        assert division(-7,2) == -3.5
        assert division(-7,0) == 0