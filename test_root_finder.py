import pytest
from root_finder import *


class TestBissectionMethod:
	def test_if_root_is_not_guaranteed_to_exist_in_interval(self):
		function = lambda x: x
		interval = (1, 2)
		epsilon = 1e-5

		with pytest.raises(Exception):
			root = find_root(function, interval, epsilon)
