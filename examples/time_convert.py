def timeConvert(num):
    num = max(int(num), 0)
    return '{:02d}:{:02d}'.format(num // 60, num % 60)


assert (timeConvert(0) == '00:00', 'Test at 0')
assert (timeConvert(-6) == '00:00', 'Negative number')
assert (timeConvert(8) == '00:08', '8 minutes')
assert (timeConvert(32) == '00:32', '32 minutes')
assert (timeConvert(75) == '01:15', 'over an hour')
assert (timeConvert(63) == '01:03', 'over an hour')
assert (timeConvert(134) == '02:14', 'over two hours')
assert (timeConvert(180) == '03:00', 'three hours')
assert (timeConvert(970) == '16:10', 'over 16 hours')
assert (timeConvert(565757) == '9429:17', 'big numbers')
