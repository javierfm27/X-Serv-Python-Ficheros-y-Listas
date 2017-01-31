#!/usr/bin/python3
fich=open("/etc/passwd")
lineas=fich.readlines()
fich.close()
for linea in lineas:
    print("login:" + (linea.split(":")[0]) + "  shell:" + linea.split(":")[-1][:-1])
