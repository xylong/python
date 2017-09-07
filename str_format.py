# -*- coding: utf-8 -*-

s = '{0} love {1}'.format('I', 'U')
print(s)

s1 = '{a} love {b}'.format(b = 'jingjing', a = 'I')
print(s1)

s2 = '{0} love {a}'.format('I', a = 'jingjing')
print(s2)

s3 = '{0:.1f}{1}'.format(27.648, 'GB')
s4 = '{0:.2f}{1}'.format(27.648, 'GB')
print(s3, s4) # 27.6GB 27.65GB（四舍五入）
