from xml.dom import minidom

root = minidom.Document()

xml = root.createElement("root")
root.appendChild(xml)

productChild = root.createElement("product")
productChild.setAttribute("name", "Python-To-Python")
xml.appendChild(productChild)
print(root)  # <xml.dom.minidom.Document object at 0x0000020D66B36570>
xml_str = root.toprettyxml()
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="Python-To-Python"/>
# </root>

save_path = "ptp.xml"
with open(save_path, "w") as f:
    f.write(xml_str)
