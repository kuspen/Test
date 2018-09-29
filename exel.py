#!/usr/bin/env python
# -*- coding: utf8 -*-
import openpyxl

#新規作成
wb = openpyxl.Workbook()

sheet = wb.active
sheet.title

id = 'TCG Tournament TEST'

sheet.title = id
IDs = ["1","2","3","4"]
Player = ["p1","p2","p3","p4"]

i = 1
for name in Player:
    sheet.cell(row=i,column=2).value = name
    i = i+1

k = 1
for ids in IDs:
    sheet.cell(row=i,column=1).value = ids
    k = k+1

#保存
wb.save(id + '.xls')