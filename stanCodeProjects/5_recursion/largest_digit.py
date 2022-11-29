"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the digit input
	:return: the largest number
	"""
	num = 0
	if n < 0:																# if negative
		n = -n
	return find_largest_digit_helper(n, num)


def find_largest_digit_helper(n, num):										# ask TA Yipin
	if n / 10 > 1:
		num = n % 10
		max_2 = find_largest_digit_helper(n//10, num)
		return max(num, max_2)
	else:																	# if n is the first digit
		return max(n, num)													# max btw the first and the second digit


if __name__ == '__main__':
	main()
