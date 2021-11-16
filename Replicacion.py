import time
import os

def nombre_archivo():
    t =time.localtime()
    dia = t.tm_mday
    mes = t.tm_mon
    ano = t.tm_year

    hora = t.tm_hour
    minutos = t.tm_min
    seg = t.tm_sec

    nombre = '%s%s%s-%s%s%s' % (dia,mes,ano,hora,minutos,seg)
    return nombre

def  leer_config():
    diccionario={}
    for linea in open("config.cfg"):

        if linea[0] != '#':

            separar = linea.split('=')
            if len(separar) > 1:

                dicc_clave = separar[0]
                dicc_valor = separar[1].rstrip() #rstrip elimina el retorno de carro
                diccionario[dicc_clave]=dicc_valor

    return diccionario


def respaldo_pg():
    diccio = leer_config()
    dic_ipservidor = diccio['ipservidor']
    dic_nombrebasedatos = diccio['nombrebasedatos']
    dic_usuariobasedatos = diccio['usuariobasedatos']
    dic_rutarespaldo = diccio['rutarespaldo']
    dic_nombrearchivo = diccio['nombrearchivo']
    dic_schema =diccio['schema']

    archivofinal = os.path.join(dic_rutarespaldo,dic_nombrearchivo+'.sql')
    comando = 'pg_dump'

    comando_a_ejecutar='%s -h %s -U %s --file %s --schema %s %s' % \
    (comando,dic_ipservidor,dic_usuariobasedatos,archivofinal,dic_schema,dic_nombrebasedatos)
    return comando_a_ejecutar



if __name__ == '__main__':

    print('Espere un momento ejecutando Proceso de Respaldo…')
    respaldar = respaldo_pg()
    print(respaldar)
    os.system(respaldar)
    print ('*** Respaldo Realizado con Exito ***')