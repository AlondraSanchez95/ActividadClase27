#!/bin/bash

echo "Bienvenido, reporte inicial del entorno" #Mensaje de bienvenida

#Funcion para la instalacion de herramientas que necesitare por nombre de programa y su comando de instalacion"
instalaciones() { 
    PROGRAMA=$1
    COMANDO_INSTALACION=$2

    echo "Verificando $PROGRAMA..."
    if ! command -v "$PROGRAMA" &> /dev/null
    then
        echo "[!] $PROGRAMA no está instalado. Instalando ahora..."
        sudo yum update &> /dev/null
        sudo $COMANDO_INSTALACION
    else
        echo "[ OK ] $PROGRAMA ya está presente en el sistema."
    fi
}

#Llamo a la funcion dependiendo que necesite
echo "Verificacion de herramientas"

instalaciones "git" "yum install git -y"

instalaciones "vim" "yum install vim -y"

instalaciones "docker" "yum install docker -y"

instalaciones "python3" "yum install python3"

#Verifico si se tiene credenciales AWS IAM
if aws sts get-caller-identity &> /dev/null; then
    echo "[ OK ] AWS CLI tiene acceso (IAM Role activo)."
else
    echo "[!] ADVERTENCIA: AWS CLI no detecta credenciales o Rol."
fi

#Mensaje final
echo "Final del reporte inicial del entorno"
