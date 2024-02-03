'''
Cal buscar la informació que es demana de la següent list:
areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
(Cal utilitzar els “:” per a que siguin vàlids els prints següents)
    Imprimir el segon element
    Imprimir l’últim element
    Imprimir l’àrea de la terrassa
    Imprimir del primer element al tercer element
    Imprimir del tercer element a l’últim
    Imprimir el total de l'àrea de les dues habitacions
    Modificar l’àrea del lavabo i imprimir la nova list area
    Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
    Imprimir el total de l’àrea del pis.

'''
areas_pis = ['Menjador', 10.15, 'Rebedor', 9.56, 'Habitació1', 12.34, 'Terrassa', 15.55, 'Lavabo', 7.98, 'Cuina', 12, 'Habitació2', 12.23]

print("Segon element:", areas_pis[1])
print("Ultim element:", areas_pis[-1])
#Encontrar index terrassa e imprimir
index_terr = areas_pis.index("Terrassa")
print("Àrea de la terrassa:",areas_pis[index_terr+1])
print("Del primer element al tercer", areas_pis[:3])
print("Del tercer al ultim:", areas_pis[2:])
print("Total de l'àrea de les dues habitacions:", areas_pis[5]+areas_pis[11])
#modificar area lavabo
areas_pis[9] = 12
print("Modificar l’àrea del lavabo:",areas_pis)
#extender lista
areas_pis.extend(["Pati interior",2.78])
print("Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions:",areas_pis)
#area total
area_total = sum([area for area in areas_pis[1::2] if isinstance(area, (int, float))])
print("Àrea total del pis:", area_total)