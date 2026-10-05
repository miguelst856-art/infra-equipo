#!/usr/bin/env python3
"""Reporte basico del sistema para el laboratorio de infraestructura."""
import os
import platform
import shutil
import socket
from datetime import datetime


def memoria_mb():
    datos = {}
    with open("/proc/meminfo") as f:
        for linea in f:
            clave, valor = linea.split(":")
            datos[clave] = int(valor.split()[0]) // 1024
    return datos["MemTotal"], datos["MemAvailable"]


def main():
    total, libre = memoria_mb()
    disco = shutil.disk_usage("/")
    carga = os.getloadavg()

    print("=" * 42)
    print(" REPORTE DEL SISTEMA - infra-equipo")
    print("=" * 42)
    print(f"Fecha        : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Host         : {socket.gethostname()}")
    print(f"Sistema      : {platform.system()} {platform.release()}")
    print(f"Python       : {platform.python_version()}")
    print(f"Memoria      : {libre} MB libres de {total} MB")
    print(f"Disco (/)    : {disco.free // 2**30} GB libres de {disco.total // 2**30} GB")
    print(f"Carga (1/5/15 min): {carga[0]:.2f} / {carga[1]:.2f} / {carga[2]:.2f}")


if __name__ == "__main__":
    main()
