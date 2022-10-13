import pytest
from root_finder import *


class TestBissectionMethod:
	def test_if_root_is_not_guaranteed_to_exist_in_interval(self):
		function = lambda x: x
		interval = (1, 2)
		precision = 1e-5

		with pytest.raises(Exception):
			root = find_root(function, interval, precision)


	def test_finding_root_of_linear_function(self):
		function = lambda x: 2*x + 1
		interval = (-1, 0)
		precision = 1e-5

		root = find_root(function, interval, precision)

		assert -0.5 - precision < root < -0.5 + precision

