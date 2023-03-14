# test_simple_math.py
import simple_math

def test_simple_math():
	assert simple_math.simple_add(3, 4) == 7
	assert simple_math.simple_sub(3, 4) == -1
	assert simple_math.simple_mult(3, 4) == 12
	assert simple_math.simple_div(3, 4) == 0.75
	assert simple_math.poly_first(2, 3, 4) == 11
	assert simple_math.poly_second(1, 2, 3, 4) == 9

