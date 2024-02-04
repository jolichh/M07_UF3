'''
Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). 
La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
    - Un root de nom students.
    - Cinc childs (del root) amb nom student.
    - Cada child student ha de tindre 4 subchilds:
        name
        surname
        email
        dni
    - Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
    - El text de cada etiqueta serà de la vostra elecció.

'''
import xml.etree.ElementTree as ET

def crear_xml():
    # Crear l'element root de nom students
    root = ET.Element("students")

    # Crear cinc childs "student" 
    for i in range(1, 6):
        student = ET.SubElement(root, "student")

        # Afegir atribut
        student.set("id", str(i))

        # Crear els quatre subchilds
        name = ET.SubElement(student, "name")
        surname = ET.SubElement(student, "surname")
        email = ET.SubElement(student, "email")
        dni = ET.SubElement(student, "dni")

        # Afegir atribut als subelements
        name.text = f"Nom{i}"
        surname.text = f"Cognom{i}"
        email.text = f"correu{i}@exemple.com"
        dni.text = f"DNI{i}"

    # Crear un objecte de l'arbre XML
    tree = ET.ElementTree(root)

    # Guardar l'arxiu XML
    tree.write("students.xml")

    # obrir XML i mostra per consola
    with open("students.xml", "r") as f:
        contingut_xml = f.read()
        print("Contingut de l'arxiu XML:")
        print(contingut_xml)

# Cridar la funció
crear_xml()