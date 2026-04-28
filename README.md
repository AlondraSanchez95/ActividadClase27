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

