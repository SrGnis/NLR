import sys
import csv

lemas=[]
tipos=[]
generos=[]
numeros=[]
todo=[]
header=[]

with open('./data/csv/noun.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    coun = True
    for row in reader:
        if(coun):
            header = row
            coun = False
        else:
            todo.append(row)

with open('./sql/nouns.sql', 'w') as of:
'''
    of.write("INSERT IGNORE INTO PALABRAS (lema, raiz) VALUES")
    for p in todo:
        of.write("(\"{lema}\",NULL),\n".format(lema=p[0]))
    of.write(';')

    of.write('\n')
'''
    of.write("INSERT INTO CATEGORIAS (id_palabra, id_tipo_categoria) VALUES")
    for p in todo:
        of.write("((SELECT (id_palabra) FROM PALABRAS WHERE lema=\"{lema}\"),(SELECT (id_tipo_categoria) FROM TIPOS_CATEGORIAS WHERE tipo_categoria=\'N\')),\n".format(lema=p[0]))
    of.write(';')

    of.write('\n')
'''
    of.write("INSERT INTO SENTIDOS (id_categoria) VALUES")
    for p in todo:
        of.write("(SELECT (id_categoria) FROM CATEGORIAS WHERE id_palabra=")
    of.write(';')

    of.write('\n')

    of.write("INSERT INTO PROPIEDADES (id_tipo_propiedad, id_palabra, id_categoria, valor) VALUES")
    for r in todo:
        if '_' not in r[0]:
            for x in range(2,len(r)):
                of.write("((SELECT (id_tipo_propiedad) FROM TIPOS_PROPIEDADES WHERE tipo_propiedad=\"{tipo_propiedad}\"),(SELECT (id_palabra) FROM PALABRAS WHERE lema=\"{lema}\"), (SELECT (id_tipo_categoria) FROM TIPOS_CATEGORIAS WHERE tipo_categoria=\"SUS\"), (\"{valor}\")),\n".format(tipo_propiedad=header[x].lower(),lema=r[0],valor=r[x].lower()))
    of.write(';')
'''

