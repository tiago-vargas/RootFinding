from typing import Callable


def find_root(func: Callable[[float], float], interval: tuple[float, float], precision: float) -> float:
	(a, b) = interval
	interval_length = b - a

	if func(a) * func(b) >= 0:
		raise Exception('No root guaranteed to exist in the interval ' + str(interval))

	if precision >= interval_length:
		return (a + b) / 2

	mean = (a + b) / 2

	if func(mean) * func(b) < 0:
		new_interval = (mean, b)

	if func(a) * func(mean) < 0:
		new_interval = (a, mean)

	if func(mean) == 0:
		return mean

	return find_root(func, new_interval, precision)
