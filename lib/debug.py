#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb


Department.create_table()
#Department.drop_table()

payroll = Department.create("Pay", "Kimathi")
print(payroll)

# payroll.save()
# print(payroll)

hr = Department.create("Hr", "5th Floor")
print(hr)

hr.name = 'HR'
hr.location = "5th floor"
hr.update()
print(hr)

print("Delete Payroll")
payroll.delete()
print(payroll)

# hr.save()
# print(hr)

ipdb.set_trace()
