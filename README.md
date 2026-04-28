# ActividadClase27
ACTIVIDAD DE CLASE: RESPUESTA DEVOPS POR ALONDRA BERENICE SANCHEZ CORTES
Caso de estudio:
Imagina que formas parte de un equipo de ingeniería en Netflix, dedicada a ofrecer una plataforma de streaming con millones de usuarios. Durante una actualización reciente de uno de sus servicios internos, el equipo detectó problemas graves:

•	La aplicación funciona correctamente en algunas computadoras, pero falla en otras.
•	Los servidores tienen configuraciones distintas entre sí.
•	Los despliegues se realizan manualmente y toman demasiado tiempo.
•	No existe una forma clara de validar automáticamente si una nueva versión está lista para desplegarse.
•	El monitoreo actual no permite detectar rápidamente errores de desempeño.

El director técnico solicita una propuesta rápida pero sólida para estandarizar el entorno, automatizar tareas clave y preparar un flujo de despliegue más confiable.
Tu tarea será actuar como consultor DevOps y generar una solución inicial que ayude a reducir estos problemas.

# Análisis:
La compañía tiene como problemas técnicos lo siguiente:
•	No existe compatibilidad de sistemas operativos.
•	Las versiones no tienen una organización adecuada.
•	No existe un monitoreo centralizado.
•	No se realizan pruebas a profundidad del servicio.
Debido a estos problemas la velocidad del despliegue se ve afectada debido a los errores humanos que se cometen, la tardanza de validar cada versión y la incompatibilidad. Eso a su vez hace que la calidad del servicio disminuya ya que no se tiene una versión base funcional y no se puede deducir errores de desempeño antes de que afecte al cliente. Cuestiones como la estabilidad y escalabilidad también se ven comprometidas ya que podría tener menos recurso de lo que se necesita y eso produce fallas en el servicio.
Proponiendo una solución DevOps, podríamos observar que:
•	Al emplear pruebas automatizadas se puede solucionar una problemática:  la tardanza del despliegue. Con pruebas automatizadas te olvidas de los errores humanos y con gran velocidad estarías validando cada versión, encontrando errores más rápido que realizarlo manualmente. 
•	Usar contenedores nos ayudaría a tener una base compatible con la mayoría de los sistemas operativos, pudiendo adaptarlos a las necesidades de cada persona que trabaje en el código y permitiendo que cualquier persona puede desplegar el servicio en cualquier dispositivo, permitiendo así la colaboración entre desarrolladores.
•	También para fomentar la colaboración y para tener un mejor control de versiones una solución viable sería el uso de GitHub. Así el tema de mantener el código actualizado seria algo mas sencillo a que cada uno realice su propia versión. Ayudaría a verificar el código antes de mandarlo a los contenedores con su sistema GitHub Actions.
•	Con el tema de los servidores y el monitoreo la propuesta seria el uso de AWS EC2 combinado a los contenedores que ya mencione para servidores personalizados y el uso de sistemas de monitoreo centralizado como AWS CloudWatch, que permite automatizar temas como la ampliación del recursos en ciertas circunstancias, como cuando el uso del recurso supere una métrica ya definida, o alarmas para verificar picos de desempeño. 

# Explicación Docker:
En el dockerfile tengo lo que vendría siendo un Multi-stage build para una imagen ligera y con bastante seguridad. Construyo un contenedor temporal con un tipo imagen alpine y mete un código fuente desde una carpeta src que se proporciona, que es donde casi siempre se guardan los códigos frontend como HTML, CSS y JS. Después tomo los archivos de la etapa de construcción y los mando a producción. Se toma como base un servidor nginx y se expone por el puerto 80.
En el compose ahora si hago todo el despliegue de los contenedores por servicio, uno para el Frontend donde le digo que haga uso del dockerfile ya creado y que depende del backend. El backend es donde primero descargo una imagen tipo node/alpine directamente, y le digo que todo el despliegue viene de la carpeta /app y que se mantenga actualizado, tambien especifico la ruta a la base de datos. Después creo un servicio que conecta con la base de datos con una imagen mongo directa. Al final mis datos se mantienen en el disco duro que Docker reserva por si se llega a apagar el contenedor o a borrar.
El flujo seria así: 
1.	Entrada del usuario: llega al contenedor temporal Nginx y sirve lo que sea que se configure como frontend
2.	Petición de datos: el código frontend pide los datos al backend
3.	Consulta a base de datos: el backend procesa la lógica y pide los datos a la base de datos
4.	Respuesta: La base de datos envía la respuesta, node los formatea y nginx los muestra.
¿Porque serviría para el caso? Solucionaría el tema de la incompatibilidad pues cada contenedor podria configurarse con las herramientas que cada desarrollador necesite, tambien ayudaría mucho con las pruebas automatizadas y al despliegue pues cada contenedor tendría su propio servicio y así no seria necesario probar toda la aplicación cada vez que alguien hace un cambio en el código. Tambien es bueno en aislar los fallos por servicio, previniendo caídas completas y malas experiencias al usuario.

# Pipeline CI/CD:
Source: GitHub
El proceso inicia con un git push a la rama main.
•	Herramientas: GitHub Actions o GitLab CI.
•	Acción: El servidor de CI detecta el cambio y descarga el código. Se activan reglas de protección de rama (nadie sube código sin que pase el pipeline).
Build: Docker Build.
Aquí es donde entra el Dockerfile. Se crean las imágenes para el Frontend, el Backend y la base de Datos
•	Herramientas: Docker Engine, GitHub Packages o AWS ECR (para guardar las imágenes).
•	Acción: Se ejecutan los comandos docker build. Se generan "etiquetas" (tags) únicas para cada version, lo que permite hacer un rollback rápido si algo falla después.
Test: Pruebas.
Antes de subir la imagen a la nube, tenemos que verificar si funciona.
•	Herramientas: Jest (para Node.js), Mocha o Cypress (para el frontend).
•	Acción: Se levantan contenedores temporales. Se ejecutan pruebas unitarias (lógica del código) y de integración (¿el backend puede conectar con el storage?). Si una prueba falla, el pipeline se detiene.
Deploy: Producción.
Si todo está bien, la nueva imagen se envía al servidor real.
•	Herramientas: AWS ECS, Render o Kubernetes.
•	Acción: Se actualiza el servicio.
Monitoreo: 
Tenemos que tener extrema vigilancia
•	Herramientas: AWS CloudWatch.
•	Acción: Se vigilan métricas como el uso de CPU, RAM y errores 500. Si el contenedor de "Storage" se queda sin espacio, el sistema lanza una alerta automática a tu correo.

# Monitoreo:
Yo monitorearía tres cosas principales: uso del CPU de la instancia, espacio en los contenedores y errores 500 con la conexión de servidores.
Configuraría alertas para situación donde, por ejemplo, el CPU alcance una métrica de 75%, por lo cual desplegaría otra instancia a la cual redirigir el tráfico. Si llegan a ver errores con la aplicación mandaría alertas inmediatas para poder verificar en donde se esta presentando el problema y poder resolverlo a la brevedad. Y si el espacio en los contenedores llega a superarse empezaría a mandar datos a un bucket S3 u otro tipo de almacenamiento. También si el tiempo de respuesta empieza a crecer el equipo tendría que verificar la conexión frontend – backend, ósea la API, o si es mas profundo el asunto otros errores como el servidor o la base de datos.

# Conclusion
Creo que la propuesta podría ayudar, por lo menos, en dar una base solida en la cual apoyarse para poder empezar a cambiar de filosofía a la hora de desarrollar, mantener y monitorear la aplicación. La parte más difícil seria, principalmente, cambiar la mentalidad y los hábitos a la hora de realizar cambios en el código y poder también configurar las partes técnicas detrás de la automatización, contenedores y monitoreo. Pero al final, considero, que podría ser muy beneficioso para la empresa, pues con estos métodos, al final se estaría dando una mejor versión de la aplicación al cliente, manteniéndose a la vanguardia y estando al tanto de las nuevas tecnologías.
________________________________________

