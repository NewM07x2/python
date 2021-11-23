"""
  xmlファイルの利用方法

  以下のxmlファイルを想定とする
  <?xml version='1.0' encoding='utf-8'>
  <root>
    <employee>
      <employ>
        <id>100</id>
        <name>Tom</name>
      </employ>
      <employ>
        <id>200</id>
        <name>Mike</name>
      </employ>
    </employee>
  </root>

"""
import xml.etree.ElementTree as ET

root = ET.Element('root')
tree = ET.ElementTree(element=root)
employee = ET.SubElement(root, 'employee')

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '100'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Tom'

employ = ET.SubElement(employee, 'employ')
employ_id = ET.SubElement(employ, 'id')
employ_id.text = '200'
employ_name = ET.SubElement(employ, 'name')
employ_name.text = 'Mike'

# ファイルの作成or書き込み
tree.write('test.xml', encoding='utf-8', xml_declaration=True)

# 読み込み
tree = ET.ElementTree(file='test.xml')
root = tree.getroot()
for employee in root:
    for employ in employee:
        # print(employ.tag)
        for person in employ:
            print(person.tag, person.text)
