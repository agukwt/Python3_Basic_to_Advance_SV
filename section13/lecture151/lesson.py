#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET


HEAD_PATH = r'C:\Programing\SiliconValleyPython\section13\lecture151' + '\\'

# xmlデータの作成・書き込み
root = ET.Element('root')
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, 'employee')

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '111'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Mike'

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '222'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Nancy'

tree.write(HEAD_PATH + 'test.xml', encoding='utf8', xml_declaration=True)

# xmlデータの読み込み・参照
tree = ET.ElementTree(file=HEAD_PATH + 'test.xml')
root = tree.getroot()

for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)
