import boto3 #Importo librerias
import botocore.exceptions
from datetime import datetime

REGION = 'us-east-1' #La region donde se buscara los recursos
NOMBRE_BUCKET = 'alondra-reportes-19972411' #El nombre del bucket donde se guardara el reporte

def verificar_identidad(): #Se verifica que si tenga acceso a los servicios de AWS, osea credenciales
    sts = boto3.client('sts')
    try:
        identity = sts.get_caller_identity()
        print(f"Identidad AWS: {identity['Arn']}")
    except Exception:
        print("Error: No se encontraron credenciales de AWS.")
        return False
    return True

def asegurar_bucket_existe(): #Se asegura de que el bucket donde se guardara el documento exista
    s3_client = boto3.client('s3', region_name=REGION)
    try:
        s3_client.head_bucket(Bucket=NOMBRE_BUCKET)
        print(f"El bucket '{NOMBRE_BUCKET}' ya existe.") #Si existe manda este anuncio
    except botocore.exceptions.ClientError as e: #Si no, lo crea
        error_code = e.response['Error']['Code']
        if error_code == '404':
            print(f"El bucket no existe. Creándolo en la región {REGION}...")
            try:
                if REGION == 'us-east-1':
                    s3_client.create_bucket(Bucket=NOMBRE_BUCKET)
                else:
                    s3_client.create_bucket(
                        Bucket=NOMBRE_BUCKET,
                        CreateBucketConfiguration={'LocationConstraint': REGION}
                    )
                print(f"Bucket '{NOMBRE_BUCKET}' creado con éxito.")
            except Exception as e_creacion:
                print(f"Error al crear el bucket: {e_creacion}")
                return False
        else:
            print(f"Error de permisos o red: {e}")
            return False
    return True

def generar_super_reporte(): #Funcion para generar el reporte de instancias EC2 y buckets S3
    if not asegurar_bucket_existe():
        print("No se puede continuar sin el bucket.")
        return
    
    ec2 = boto3.client('ec2', region_name=REGION)
    s3 = boto3.client('s3', region_name=REGION)
    
    fecha_hoy = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Se toma la fecha actual
    archivo_reporte = f"reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt" #Se crea el reporte en formato txt con un nombre unico


    with open(archivo_reporte, "w", encoding="utf-8") as f:
        f.write(f"==========================================\n")
        f.write(f"Reporte de recuros - Reto DevOps\n")
        f.write(f"Fecha: {fecha_hoy}\n")
        f.write(f"==========================================\n\n")
        f.write("INSTANCIAS EC2\n")
        f.write("------------------------------------------\n")
        response_ec2 = ec2.describe_instances() #Se verifican todas las instancias EC2
        total_prendidas = 0 
        total_apagadas = 0
        for reservation in response_ec2['Reservations']:
            for inst in reservation['Instances']:
                id_inst = inst['InstanceId']
                estado = inst['State']['Name']
                tipo = inst['InstanceType']
                nombre = "Sin Nombre"
                if 'Tags' in inst:
                    for tag in inst['Tags']:
                        if tag['Key'] == 'Name':
                            nombre = tag['Value']
                if estado == 'running':
                    total_prendidas += 1
                elif estado == 'stopped':
                    total_apagadas += 1
                f.write(f"[*] {nombre} ({id_inst})\n")
                f.write(f"Estado: {estado} | Tipo: {tipo}\n")
        f.write(f"\nResumen EC2: Prendidas ({total_prendidas}) | Apagadas ({total_apagadas})\n\n")
        f.write("BUCKETS S3\n")
        f.write("------------------------------------------\n")
        response_s3 = s3.list_buckets() #Se verifican todos los buckets S3 y sus objetos, tomando como maximo 5
        for bucket in response_s3['Buckets']:
            nombre_b = bucket['Name']
            f.write(f"[+] Bucket: {nombre_b}\n")
            obj_res = s3.list_objects_v2(Bucket=nombre_b, MaxKeys=5)
            if 'Contents' in obj_res:
                f.write(f"Últimos archivos:\n")
                for obj in obj_res['Contents']:
                    f.write(f"- {obj['Key']} ({obj['Size']} bytes)\n")
            else:
                f.write("(Bucket vacío)\n")
        f.write(f"\n==========================================\n")
        f.write(f"Fin del reporte\n")
    print(f"Reporte generado con éxito en: {archivo_reporte}")  #Se crea el reporte en el entorno local
    s3.upload_file(archivo_reporte, NOMBRE_BUCKET, f"reportes/{archivo_reporte}") #Se sube al bucket S3 el reporte
    print(f"Reporte respaldado en S3: s3://{NOMBRE_BUCKET}/reportes/{archivo_reporte}") 

if __name__ == "__main__": #Se llama la funcion principal
    if verificar_identidad() == False:
        print("No tienes credenciales validas :()")
    else:
        generar_super_reporte()
