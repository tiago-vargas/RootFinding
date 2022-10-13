import pytest
from root_finder import *


class TestBissectionMethod:
	# def test_linear_function_with_high_precision(self):
	# 	function = lambda x: 2*x + 1

	# 	epsilon = 1e-5

	# 	root = find_root(function, (-2, 0), epsilon)

	# 	assert -1 - epsilon <= root <= -1 + epsilon


	# def test_linear_function_with_low_precision(self):
	# 	function = lambda x: 2*x + 1

	# 	epsilon = 4

	# 	root = find_root(function, (-2, 0), epsilon)

	# 	assert -1 - epsilon <= root <= -1 + epsilon


	def test_if_root_is_not_guaranteed_to_exist_in_interval(self):
		function = lambda x: x
		interval = (1, 2)
		epsilon = 1e-5

		with pytest.raises(Exception):
			root = find_root(function, interval, epsilon)
