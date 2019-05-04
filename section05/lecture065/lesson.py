#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = [1, 2, 3]
i = 5
del l

try:
    l[0]

except IndexError as ex:
    print("Don't worry {}".format(ex))

except NameError as ex:
    print(ex)

except Exception as ex:
    print(ex)

else:
    print('done')

finally:
    print('Clean up')
