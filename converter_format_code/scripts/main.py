import xml.etree.ElementTree as ET
import encore

def export_enc_to_xml(enc_file_path, xml_file_path):
    # Leer el archivo .enc
    enc_data = encore.read(enc_file_path)
    
    # Crear el elemento raíz del XML
    root = ET.Element("EncoreData")
    
    # Convertir los datos del archivo .enc a XML
    for key, value in enc_data.items():
        item = ET.SubElement(root, "Item")
        key_element = ET.SubElement(item, "Key")
        key_element.text = str(key)
        value_element = ET.SubElement(item, "Value")
        value_element.text = str(value)
    
    # Crear el árbol XML y escribirlo en un archivo
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

# Ejemplo de uso
export_enc_to_xml("ruta/al/archivo.enc", "ruta/al/archivo.xml")
