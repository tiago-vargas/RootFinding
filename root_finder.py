from typing import Callable


def find_root(func: Callable[[float], float], interval: tuple[float, float], precision: float) -> float:
	(a, b) = interval

	if func(a) * func(b) >= 0:
		raise Exception('No root guaranteed to exist in the interval ' + str(interval))

	if precision >= b - a:
		return (a + b) / 2
