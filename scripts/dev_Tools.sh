#!/bin/bash
echo "Iniciando configuracion de Python"
sudo yum update
sudo yum install python3 python3-pip -y
echo "Instalando boto3 para la interaccion con AWS"
pip3 install boto3
echo "Verificacion de instalaciones"
python3 --version
pip3 --version
python3 -c "import boto3; print('boto3 --version' + boto3.__version__)"
echo "Dependencias instaladas"
