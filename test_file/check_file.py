import sys
import os

fd = open('./123.xlsx', 'rb')
header = fd.read(100)
fd.close()
print(header)
