# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12xcypef90SKJeowwkGloRnGeiWEaT995
"""

# -*- coding: utf-8 -*-
"""IDS_20200424_1.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1aLXOD5PEGZTGkZezwzDM5IHosdhm9qww
"""

x = int(input("請輸入起始的正整數:"))
y = int(input("請輸入終止的正整數"))
i = x
while i <= y:
    if i % 2 == 1:
      print(i)
    i += 1