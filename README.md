## **Nombre Proyecto: Nutrifit**

El proyecto consiste en una aplicación web relacionada con la salud y el fitness. Partiendo de
los datos iniciales del usuario (altura, peso...) se hará un análisis para saber qué tipo de dieta
se le recomienda para poder obtener una buena salud. Al mismo tiempo, se irán guardando
los datos de progresión del mismo con el fin de mostrarle un seguimiento del progreso. A parte
de todo esto, el usuario va a poder crear unas rutinas semanales basadas en su condición
física. 

### Funcionalidades:

- **Soporte para usuarios:**
El usuario va poder registrarse rellenando una serie de campos (fecha de nacimiento,
peso, sexo...) e iniciar sesión introduciendo un nombre de usuario y su contraseña en
los campos que corresponden y pulsar el botón ‘Iniciar Sesión’.

- **Histórico de progreso:**
Se llevará un histórico de cómo progresa la condición del usuario a lo largo del tiempo.
Este histórico tendrá datos como el peso, las calorías que necesita consumir y demás datos
relacionados con la salud de la persona.

- **Mostrar datos estadísticos del histórico:**
El usuario podrá ver una serie de datos (valores máximos y mínimos de parámetros
en un intervalo de tiempo, la media de peso en un periodo...). Estos datos se calculan
a partir del histórico guardado.

- **Gráficas que muestren el progreso:**
El usuario podrá ver la progresión del histórico con una serie de gráficas.

- **Recomendación de recetas:**
Se le recomendarán recetas al usuario, basadas en el tipo de comida que quiera comer,
sus intolerancias y el tipo de dieta (vegetariana, vegana...), entre otros, o en base a sus
necesidades de micronutrientes (proteínas,  calcio, sodio...) extraídas del histórico del
usuario. Además, pueden verse los detalles de cada receta, incluyendo un gráfico con su
información nutricional.

- **Creación de rutinas semanales:**
Se creará una rutina semanal de ejercicios variados, teniendo en cuenta la condición física
del usuario.


### Cumplimiento de requisitos:

- En cuanto a los requisitos obligatorios, el proyecto cumple con todo lo pedido: Se trata de una **aplicación
  web**, desarrollada en el **framework _Django_** y escrita en **Python siguieno el patrón _Model-View-Template_**, en la
  que se realizan constantes **consultas a APIs** y se hace algún **análisis de datos con Pandas**. Además, ha sido
  desarrollada usando **git como control de versiones** y está **plenamente _dockerizada_**. Por último, también se han
  realizado **tests** para cada una de las tres aplicaciones (Funcionalidades) principales y se han realizado
  **reuniones de control** de progreso habituales (Periodo de ~3 días) en las que también **se ha ido anotando las
  horas de trabajo** realizadas por los miembros de este proyecto.

- Por otra parte, se han abarcado una gran cantidad de objetivos deseables. En primer lugar, 


## **Integrantes Grupo:**

  * Alejandro Fernández Otero  <alejandro.fernandezo@udc.es>
  * Alejandro Javier Herrero Arango  <a.j.herrero@udc.es>
  * Óscar Olveira Miniño  <oscar.olveira@udc.es>
  

## **Inicio automatizado**
1) Clonar el repositorio:
 ```git clone https://github.com/GEI-PI-614G010492324/aplicacion-django-olveira_fernandez_herrero.git```
2) ```cd aplicacion-django-olveira_fernandez_herrero```
3) Ejecutar el script: ```./setup.sh```

Tras esto la aplicación es completamente funcional. Para acceder a ella ir a http://localhost:8000

**Importante**: Una vez ejecutado el script, si se quisiese iniciar los contenedores de docker desde Visual Studio Code sería necesario ejecutar ```./setup.sh clean``` para eliminar los contenedores creados previamente y evitar conflictos.

## **Una vez terminado**
Se puede eliminar la aplicación haciendo ```./setup.sh clean```. Esto eliminará los contenedores, imagenes y volumenes que estuviese usando la aplicación.



### Ejecución de los tests:


## **Problemas conocidos:**

- En la parte de generar rutinas, hay algunos musculos que no tienen ejercicios específicos para una intensidad por lo que no se muestran en el calendario. Una posible solucion seria
  comprobar si para la intensidad que especifica el usuario, aparezcan solamente los musculos que tienen ejercicios con esa intensidad 


## **Posibles mejoras:**

- La API de spoonacular contiene no solo recetas, sino también ingredientes y operaciones para manejarlos,
  permitiendo la posibilidad de que los usuarios creen sus propios platos añadiendo o eliminando ingredientes
  mientras ven como va cambiando la informacion nutricional y la cantidad de calorías. Esto podría permitir que
  los usuarios crearan sus propios calendarios semanales de comida, bien con recetas ya existentes en spoonacular
  o con las suyas propias.

- Debido a carencias en el funcionamiento en la API de salud, usada principalmente en homepage, guardamos un
  histórico de micronutrientes. Creemos que sería bastante más útil que se guardaran más bien nutrientes más grandes,
  como hidratos de carbono, proteínas o grasas y no sodio, calcio o hierro, entre otros, que la gente no suele
  fijarse tanto en ellos.


---------------------------------------------------------------------------------------

#             TUTORIAL INSTALACION ENTORNO PRACTICAS 


# Visual Studio Code Tutorial

En este tutorial vamos a ver cómo configurar Visual Studio Code así como sus principales funcionalidades. Para un mayor aprovechamiento en la asignatura enfocaremos este tutorial a entorno de programación Python. Más específicamente, al finalizar el mismo tendréis configurado un entorno de desarrollo preparado para un proyecto Django con vistas a la práctica a realizar.

## Tabla de contenidos
1. [Comencemos](#desc)
2. [Aspectos generales](#tips)
3. [Extensiones](#ext)
4. [Debugging](#debug)
5. [Sistema control de versiones](#git)
6. [Remote-Containers](#container)
7. [Django](#django)

<a name="desc"></a>
# 1. Comencemos
## Setting up Visual Studio Code
VS Code es un editor de código fuente gratuito y [*open-source*](https://github.com/microsoft/vscode) disponible para Linux, macOS y Windows. A continuación se enlazan las guías de instalación específicas para cada plataforma:
* [macOS](https://code.visualstudio.com/docs/setup/mac)
* [Linux](https://code.visualstudio.com/docs/setup/linux)
* [Windows](https://code.visualstudio.com/docs/setup/windows)
## Interfaz de usuario

La siguiente figura muestra la disposición básica de componentes en VS Code.

<p align="center">
  <img src="https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png" alt="Figure 1"/>
</p>


Entre los componentes básicos encontraremos:
* **Activity Bar**. Situada en el borde vertical izquierdo, contiene el explorador de archivos, el administrador de extensiones, un buscador, el administrador de código fuente (e.g. Git), acceso a la herramienta de ejecución y depuración, entre otros. Los elementos de la activity bar podrán aumentar dependiendo de las extensiones que tengamos instaladas.
* **Side Bar**. Situada a la derecha de la activity bar, muestra información de distinta naturaleza dependiendo de la herramienta seleccionada, como podría ser la estructura de directorios de nuestro proyecto.
* **Editor Groups**. Región principal de la herramienta y desde donde editaremos nuestros ficheros fuente. Visual Studio Code permite dividir en celdas verticales y horizontales esta región, de manera que podemos tener distintos ficheros visibles simultáneamente. Para ello bastaría con seleccionar y arrastrar una pestaña por dicha región y el editor ya nos irá marcando las distintas formas en las que podemos ir dividiendo esta vista. Para más información acerca de esta funcionalidad, consultar [side-by-side-editing](https://code.visualstudio.com/docs/getstarted/userinterface#_side-by-side-editing) y [grid-layout](https://code.visualstudio.com/docs/getstarted/userinterface#_grid-editor-layout).
* **Panel**. Situado por defecto debajo del editor, muestra información de salida y de debugging, problemas o warnings de nuestra ejecución y también integra una terminal.
* **Status Bar**. Situada en el borde inferior, resume la información general de nuestro proyecto: rama del repositorio en la que nos encontramos, errores, warnings, etc.

<a name="tips"></a>
# 2. Aspectos generales
La paleta de comandos es el punto de encuentro a todas las funcionalidades de VS Code. Para acceder a la Paleta de Comandos podemos ir a ```Ver > Paleta de comandos``` o usando los atajos de teclado: ⌘P en macOS o Ctrl+P en Linux/Windows. 

Podemos utilizar esta herramienta para buscar por nombre los ficheros que hemos utilizado recientemente, por ejemplo.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157474152-ec25afba-d3f5-4fa9-b284-8711e4607eef.png" alt="Figure 2"/>
</p>

Una funcionalidad interesante si estamos intercambiando continuamente entre dos ficheros es la combinación Ctrl+P+P (⌘PP).

Sin embargo, la paleta de comandos no es meramente un buscador de archivos, sino que nos ofrece funcionalidades mucho más potentes e interesantes. Si escribimos ```?``` en la ventana emergente podremos ver la lista de "comodines" empleados en VS Code para representar las funcionalidades ofrecidas. Algunas de las opciones más interesantes están representadas por los caracteres: ```@```, ```#```, ```>``` ó ```:```. Vamos a ver cada uno por separado.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157477862-621181ce-3450-4c94-9fc1-42504cf6d965.png" alt="Figure 2"/>
</p>

* ```@``` : Nos permite buscar un símbolo por nombre en el fichero actual. Lo que VS Code llama símbolo puede ser una variable, una clase, un método, ...

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157477933-f7ad4e80-2e55-4c09-908d-13ba205ea39e.png" alt="Figure 2"/>
</p>

Si añadimos ```:``` después de ```@```, las coincidencias serán agrupadas según su categoría (variables, métodos, clases, etc).

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157479335-6e6b7c61-4598-4b3e-8770-e40bfa79ae3b.png" alt="Figure 2"/>
</p>

* ```#``` : Permite extender la búsqueda de símbolos a otros ficheros del proyecto, no necesariamente el actual (⌘T)

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157479560-d962d349-b002-4524-8398-b76ca3e7637c.png" alt="Figure 2"/>

</p>

* ```:``` : permite ir a una línea concreta del fichero actual (e.g. ```:50``` nos llevaría a la línea número 50)
* ```>``` : Representa la parte central de la Paleta de Comandos y permite mostrar y ejecutar múltiples comandos del editor. Podemos desde ejecutar nuestro proyecto, depurarlo, ejecutar órdenes de nuestro sistema control de versiones (e.g. pull, push, clone, etc), abrir una nueva terminal, hasta cambiar el tema/apariencia de nuestro editor, entre muchísimas otras.

Para mayor información acerca de la paleta de comandos, consultar [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette).

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157478066-bcf9a22e-261b-4942-97db-8d97bf0700ea.png" alt="Figure 2"/>
</p>

Un atajo fuera de la paleta de comandos, pero muy útil sobre todo cuando estamos familiarizándonos con un proyecto nuevo y/o ajeno, es el de 'Ir a definición/Go to definition'. Para ello situamos el cursor encima de una definición (puede ser una llamada a método, llamada a clase, llamada a función, etc) y pulsamos ```F12```. En ese momento VS Code nos llevará al lugar donde se ha hecho la declaración del objeto en cuestión.

Para quién quiera profundizar/investigar sobre otros atajos, *edit hacks* o "trucos" que pueden mejorar vuestra productividad, se recomienda consultar: [VS Code tips and tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks).

<a name="ext"></a>
# 3. Extensiones

Las funcionalidades que ofrece VS Code out-of-the-box pueden ser extendidas por medio de extensiones o plugins. Esto nos permitirá configurar nuestro editor de código *ad libitum*, incorporando nuevas capas de funcionamiento extra y consiguiendo un comportamiento cercano al de un IDE pero de una forma mucho más ligera, flexible, personalizada y sobre todo, gratuita.

Instalar nuevas extensiones es muy sencillo. Bastaría con seleccionar la pestaña de "Extensiones" en la Activity Bar, que nos llevará al MarketPlace donde podremos buscar por nombre la extensión deseada e instalarla.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157483945-773ac0b5-193b-40b6-8851-0465cf2f690a.png" alt="Figure 2"/>


Algunas de las extensiones recomendadas para esta asignatura son:
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (versión oficial de Microsoft)
* [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) (versión oficial de Microsoft)
* [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) (versión oficial de Microsoft)
* [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) (para usuarios de Windows. Versión oficial de Microsoft)
* [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) (versión oficial de Microsoft)
* [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (versión oficial de Microsoft)
* [HTML snippets](https://marketplace.visualstudio.com/items?itemName=abusaidm.html-snippets)
* [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django).

En relación con la extensión de Python, en caso de tener múltiples intérpretes instalados, deberemos seleccionar en la parte inferior del editor la versión del mismo que deseamos utilizar.

  
<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159157560-78dc441c-9e66-4ce9-ade6-7f298bfe4729.png" alt="Figure 2"/>


Otras extensiones de propósito general que pueden ser interesantes:
* [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
* [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)
* [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments)
* [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
* [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
* [Rewrap](https://marketplace.visualstudio.com/items?itemName=stkb.rewrap)

Se recomienda que, antes de instalar una extensión, se lea la descripción asociada y las funcionalidades que ofrece, se valore su necesidad y, en caso de instalarla, se configure tal y como se indica, si procede. En general, la mayoría de extensiones nos proporcionan un comportamiento por defecto sin necesidad de realizar una configuración específica. Sin embargo, casi todas ellas pueden configurarse para obtener un comportamiento más adaptado a nuestras necesidades.

<a name="debug"></a>
# 4. Debugging

Como hemos mencionado anteriormente, podemos encontrar un acceso directo al depurador de VS Code en la Activity Bar lateral.
El primer paso para poder debuggear nuestro código es crear un archivo ```launch.json``` que configure nuestro entorno de depuración.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157497614-94858087-5516-4f02-b83c-eb8ee6d66762.png" alt="Figure 2"/>
</p>

En caso de no tener un fichero ```launch.json``` creado, VS Code ofrece una serie de plantillas de configuración básicas para distintos lenguajes/librerías/herramientas. En este caso, vamos a seleccionar una plantilla básica para Python. No obstante, como podemos ver en la siguiente figura, también tenemos la posibilidad de generar una plantilla para una aplicación Django. Veremos esta opción más adelante.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157497690-1cd2ec65-df46-448b-b5fc-e03fd3df6a56.png" alt="Figure 2"/>
</p>

Existen diversos parámetros de configuración adicionales que pueden resultar de especial utilidad en nuestro entorno de trabajo dependiendo de nuestras necesidades. Podéis encontrar un listado de estos parámetros en: [additional configurations](https://code.visualstudio.com/docs/python/debugging#_additional-configurations).

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157497773-d061e403-563b-437a-9fff-e1b19e3e862a.png" alt="Figure 2"/>
</p>

Para comenzar el proceso de depuración, el primer paso sería definir los puntos de ruptura, pinchando en la parte izquierda de la línea en cuestión, de manera que aparezca un punto rojo que corrobore la selección hecha. A continuación, pinchamos en el símbolo "Play" situado en la parte superior de la Side Bar (```F5```). Nótese que debemos de tener seleccionada la plantilla de configuración que hemos creado previamente en el desplegable que está a la derecha del símbolo "Play" mencionado.

En este instante, aparecerá una pequeña barra de herramientas sobre el *Editor Group* que nos permitirá, de izquierda a derecha: continuar nuestra ejecución hasta el siguiente punto de ruptura (Continue), depurar paso a paso por procedimientos (step over), depurar paso a paso por instrucciones (step into), salir de la depuración (step Out), reiniciar la depuración (restart) y pausar la depuración (stop). Este funcionamiento es común a cualquier otra herramienta de depuración en IDE/editor de código que hayáis utilizado.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159155302-d61b045d-7c34-4ddb-b70c-1a955fa5a676.png" alt="Figure 2"/>
</p>

Cuando la ejecución del código llegue a uno de los puntos de ruptura establecidos previamente, la Side Bar mostrará el estado de las variables definidas hasta ese momento en nuestro programa.

Existe la posibilidad de ver la evolución de una variable específica escribiendo su nombre en el bloque "Inspección" que podemos encontrar en la Side Bar (```Inspección > Agregar expresion```).

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159155322-86ab5b9b-62f2-4453-b4e8-94bbf07e9fbf.png" alt="Figure 2"/>
</p>



También podremos configurar un punto de ruptura para que tenga un comportamiento distinto al por defecto. Esto puede ser interesante, por ejemplo, si queremos que el punto de ruptura definido no pare la ejecución del programa y simplemente escriba un log. Podremos ver dicho log en la "Consola de depuración", dentro del Panel de VS Code. Para ello hacemos click con el botón derecho sobre el punto de ruptura y seleccionamos ```Editar punto de interrupción > Mensaje de registro```. En el input text que nos aparece escribiríamos el mensaje que queremos imprimir, pudiendo imprimir el contenido de variables mediante la notación ```{variable}```.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157497911-4275eacc-320d-40d4-b0d4-8ff529b71ded.png" alt="Figure 2"/>
</p>

También podremos configurar un punto de ruptura para que solo se pare la ejecución de nuestro programa cuando se cumpla una determinada condición ```Editar punto de interrupción > Expresión```. Por ejemplo, cuando una variable tenga asignado un valor concreto.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/157497967-a29a8859-0107-4e4f-b4f6-9c6f88041173.png" alt="Figure 2"/>
</p>

También existe la posibilidad de configurar el depurador para que detecte y muestre las partes del código en las que se haya producido una excepción. Para ello tenemos que seleccionar el checkbox asociado ```Raised Exceptions``` dentro del grupo "Puntos de Interrupción" situado en la Side Bar (en la parte inferior).

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159155326-9af4b404-faf9-4d41-97fd-cd511605e664.png" alt="Figure 2"/>
</p>


<a name="GIT"></a>
# 5. Sistema control de versiones

VS Code integra por defecto el Source Control Management (SCM) e incluye soporte a Git out-of-the-box.

Así, podremos inicializar un repositorio nuevo dentro del proyecto en el que nos encontramos en caso de que aún no lo hayamos hecho.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159155479-d6b889d1-d237-4480-85b8-e5bc01a7de2e.png" alt="Figure 2"/>
</p>



Para hacer un commit, la dinámica es muy sencilla. Pinchamos sobre el símbolo ```+``` encima de aquellos ficheros que queramos incluir y damos un mensaje al commit. Una vez incluido un fichero podrá volver a ser eliminado del commit pinchando sobre el símbolo ```-```.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159155513-2d65cc44-f3ef-41a4-9d1b-ec1f6f69157b.png" alt="Figure 2"/>
</p>

Una vez añadidos todos los ficheros que queremos, pinchamos sobre "Confirmar" para realizar el commit.


![git4](https://user-images.githubusercontent.com/38211239/157498103-893f9a3c-ece0-43be-8d4a-51c4c4c75d78.png)

Veremos que nuestro commit aparece en el bloque "COMMITS" de la side bar.

<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159155659-aa80f7db-ff5a-4d81-b152-ed847171618b.png" alt="Figure 2"/>
</p>


Para hacer el commit público (hasta ahora sólo está en local), debemos hacer un push. Para ello pinchamos sobre el icono con una nube que aparece dentro del bloque COMMITS "Publish main to GitHub", o dentro del propio commit que acabamos de realizar. Recordad que si no existe el repositorio en GitHub, primero debéis crearlo y ejecutar ```git remote add origin git@github.com:LopezCastroRoberto/finalexample.git``` para asociar vuestra rama main/master con el origin. En commits posteriores el Push aparecerá representado simplemente mediante ↑.

**Cuidado**: puede que en algunos casos tengáis configurado el Push para que haga un Push force, con los riesgos que esto supone. Debéis ser conscientes de esto y cambiar la configuración en caso de que sea necesario.


<p align="center">
  <img src="https://user-images.githubusercontent.com/38211239/159155684-1b022256-bff8-4d9d-a0c1-e66f479eed91.png" alt="Figure 2"/>
</p>


En este punto, si hacéis un cambio en local y pincháis sobre el fichero modificado (letra "M" de "Modified" a la derecha del fichero) podréis ver resaltadas las diferencias con respecto al último commit en el Edit Group.

![git8](https://user-images.githubusercontent.com/38211239/157498191-fb6f0f92-fa50-4ba8-a08c-8893014c1053.png)


Cualquier otra funcionalidad de Git (pull, clone, etc) puede encontrarse escribiendo su nombre en la Paleta de Comandos (e.g. Git: pull) o en los tres puntos situados a la derecha del bloque "CONTROL DE CÓDIGO FUENTE".
![git9](https://user-images.githubusercontent.com/38211239/157498205-6863663b-ab2c-46b3-8bd0-d8d362fabde8.png)


<a name="container"></a>
# 6. Remote-Containers


Como requisito previo a este tutorial debéis tener instalado [Docker](https://www.docker.com/products/docker-desktop/) en vuestro equipo. Puede ser interesante, aunque no obligatorio, instalar también [PgAdmin](https://www.pgadmin.org/download/). Lo veremos más adelante.


Vamos a partir del ejemplo myciao de Django que habéis visto en clase de teoría. La configuración completa que haremos en este tutorial sobre ese proyecto se puede encontrar en ```https://github.com/GEI-PI-614G010492122/Tutoriales/tree/main/VSCode/myciao```.

El primer paso para configurar un entorno de desarrollo sobre Docker en VS Code será descargar la extensión asociada, previamente referenciada en este tutorial (Paso 3). 

![Captura de pantalla 2022-03-23 a las 11 56 52](https://user-images.githubusercontent.com/38211239/159684960-41b1b672-999e-46dc-bec4-9ffcebfdef1f.png)

Por otra parte, la extensión ```Remote-Containers``` nos permite crear un entorno de desarrollo empleando contenedores Docker de forma prácticamente transparente para el programador, pero con los beneficios que ofrece la virtualización de aplicaciones. También debemos instalarla.

![Captura de pantalla 2022-03-23 a las 11 57 11](https://user-images.githubusercontent.com/38211239/159684984-fc55e97e-bfe2-4dd0-929b-61b5304c89ca.png)

Tras instalar las dos extensiones previamente referenciadas, crear una configuración para soportar Docker en nuestro proyecto es tan fácil como seleccionar la opción ```Add Development Container Configuration Files``` en la Paleta de Comandos de VS Code

![Captura de pantalla 2022-03-23 a las 12 08 13](https://user-images.githubusercontent.com/38211239/159686853-7fa0f3c0-f529-40e4-a0a7-644b8bc176b4.png)

y posteriormente seleccionar la plantilla ```Python 3 & PostgreSQL```, que es la que más se aproxima a nuestro caso de uso.

![Captura de pantalla 2022-03-23 a las 12 08 31](https://user-images.githubusercontent.com/38211239/159686864-2dc86de0-cc6a-4351-bd9f-908239dce746.png)

Veremos que esto crea una carpeta ```.devcontainer``` con los ficheros de configuración/scripts: ```devcontainer.json```, ```docker-compose.yml``` y ```DockerFile```. 

A continuación se proporcionan algunas adaptaciones a dichas plantillas que serán necesarias en fases posteriores del tutorial:
## devcontainer.json
```
// For format details, see https://aka.ms/devcontainer.json. For config options, see the README at:
// https://github.com/microsoft/vscode-dev-containers/tree/v0.155.1/containers/python-3-postgres
// Update the VARIANT arg in docker-compose.yml to pick a Python version: 3, 3.8, 3.7, 3.6 
{
    "name": "Python 3 & PostgreSQL",
    "dockerComposeFile": "docker-compose.yml",
    "service": "app",
    "workspaceFolder": "/workspace",

    // Set *default* container specific settings.json values on container create.
    "settings": { 
        "terminal.integrated.shell.linux": "/bin/bash",
        "sqltools.connections": [{
            "name": "Container database",
            "driver": "PostgreSQL",
            "previewLimit": 50,
            "server": "localhost",
            "port": 5432,
            "database": "postgres",
            "username": "postgres",
            "password": "postgres"
        }],
        "python.pythonPath": "/usr/local/bin/python",
        "python.linting.enabled": true,
        "python.linting.pylintEnabled": true,
        "python.formatting.autopep8Path": "/usr/local/py-utils/bin/autopep8",
        "python.formatting.blackPath": "/usr/local/py-utils/bin/black",
        "python.formatting.yapfPath": "/usr/local/py-utils/bin/yapf",
        "python.linting.banditPath": "/usr/local/py-utils/bin/bandit",
        "python.linting.flake8Path": "/usr/local/py-utils/bin/flake8",
        "python.linting.mypyPath": "/usr/local/py-utils/bin/mypy",
        "python.linting.pycodestylePath": "/usr/local/py-utils/bin/pycodestyle",
        "python.linting.pydocstylePath": "/usr/local/py-utils/bin/pydocstyle",
        "python.linting.pylintPath": "/usr/local/py-utils/bin/pylint",
        "python.testing.pytestPath": "/usr/local/py-utils/bin/pytest", 

        // Analysing code using Django
        "python.linting.pylintArgs": [
            "--disable=C0111","--load-plugins", "pylint_django"
        ]
    },

    // Add the IDs of extensions you want installed when the container is created.
    "extensions": [
        "ms-python.python",
        "mtxr.sqltools",
        "mtxr.sqltools-driver-pg"
    ],

    // Use 'forwardPorts' to make a list of ports inside the container available locally.
    // "forwardPorts": [5000, 5432],

    // Use 'postCreateCommand' to run commands after the container is created.
    // "postCreateCommand": "pip install --user -r requirements.txt",

    // Comment out connect as root instead. More info: https://aka.ms/vscode-remote/containers/non-root.
    //"remoteUser": "vscode"
}
```
## docker-compose.yml

```
version: '3'

services:
  
  app:
    build:
      context: ..
      dockerfile: .devcontainer/Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ~/.gitconfig:/root/.gitconfig
      - ..:/workspace
    command: sleep infinity
    links:
      - 'db'

  db:
    image: postgres:latest
    restart: always
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: postgres
      POSTGRES_DB: postgres
      POSTGRES_PASSWORD: postgres

volumes:
  postgres-data:
```

## Dockerfile

```
FROM python:latest

ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace
WORKDIR /workspace

RUN pip install --upgrade pip

# Install Python dependencies from requirements.txt if it exists
COPY /requirements/requirements.txt requirements.txt* /workspace/
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt && rm requirements.txt; fi
COPY /requirements/development.txt development.txt* /workspace/
RUN if [ -f "development.txt" ]; then pip install --no-cache-dir -r development.txt && rm development.txt; fi

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
```

Una vez hemos aplicado los cambios pertinentes a dichos ficheros de configuración, el siguiente paso es construir los contenedores sobre los que correrá nuestra aplicación haciendo uso de las imágenes que acabamos de definir.

![Captura de pantalla 2022-03-23 a las 12 45 10](https://user-images.githubusercontent.com/38211239/159692213-e32b82d3-7045-4ac4-8a90-d7466b0146a2.png)

Si todo ha ido bien (debemos asegurarnos de que tenemos el servicio de docker corriendo en nuestro equipo), VS Code cambiará ligeramente la ventana que teníamos, de tal forma que en la esquina inferior izquierda veremos un rectángulo verde con el texto *Dev Container* que nos corroborará que estamos "conectados" a nuestro contenedor a través de la ventana actual del editor. Además, podremos ver que el prompt de la terminal integrada también ha cambiado, por lo que ahora los comandos que ejecutemos en dicha terminal serán invocados realmente dentro del contenedor Docker principal que hemos creado.

![Captura de pantalla 2022-03-23 a las 12 35 39](https://user-images.githubusercontent.com/38211239/159691105-0d2e0b49-5de7-4899-887d-7885bdf09958.png)

Podemos comprobar también fuera de VS Code, en una terminal, las imágenes de Docker que hemos generado con las definiciones aportadas (```docker images```). Como se puede apreciar se han creado dos imágenes: (1) una que contendrá nuestra aplicación y (2) otra que albergará la base de datos de la misma. Del mismo modo, también podemos comprobar los contenedores que tenemos ejecutándose a partir de dichas imágenes, es decir, instancias de las mismas que están corriendo en nuestra máquina actualmente (```docker container ls``` o ```docker ps```).

![Captura de pantalla 2022-03-23 a las 12 36 46](https://user-images.githubusercontent.com/38211239/159691141-91c0b4fa-ac01-4e31-b22c-db32d19ff68a.png)

Si tenemos Docker Desktop instalado, también podremos comprobar esta información desde la GUI o dashboard. 

![Captura de pantalla 2022-03-23 a las 12 37 20](https://user-images.githubusercontent.com/38211239/159691171-c1b5573f-7200-4299-b0f5-d7c063148030.png)

Algo interesante en este punto y que debemos diferenciar es el concepto de imagen y de volumen. Como podemos ver en el fichero ```docker-compose.yml``` se han generado dos imágenes, una para la aplicación y otra para la base de datos. Sin embargo, una diferencia fundamental entre ambas es que la imagen asociada a la base de datos define un volumen, que no es más que un directorio o fichero en el ```docker engine``` que se monta directamente en el contenedor y será el que nos proporcionará la persistencia de datos en nuestra aplicación. De hecho, podemos portar estos volúmenes entre equipos a través de un fichero comprimido, hacer backup de ellos o restaurarlos. Ver https://docs.docker.com/storage/volumes/#backup-restore-or-migrate-data-volumes

![Captura de pantalla 2022-03-23 a las 12 37 39](https://user-images.githubusercontent.com/38211239/159691183-b1ab086d-b450-4955-8a7f-57b61073ebf9.png)


<a name="django"></a>
# 7. Django

El siguiente paso es configurar nuestro proyecto Django para correr dentro del entorno Docker que hemos definido en la sección anterior. Para ello debemos de cambiar el siguiente trozo del fichero ```settings.py```


```
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

especificando ahora que la base de datos a utilizar será una postgreSQL indicando además el nombre, usuario y contraseña que habíamos definido en el fichero ```devcontainer.json```.

```
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

también podemos hacer uso de variables de entorno para no "cablear" la contraseña en nuestro fichero de configuración, ya que podrá hacerse público. 

```
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',                      
        'USER': 'postgres',
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': 'db',
        'PORT': '5432', 
    }
}
```

en este punto ya podemos ejecutar ```python manage.py runserver 0.0.0.0:8000``` para lanzar nuestra aplicación.

![Captura de pantalla 2022-03-23 a las 12 53 23](https://user-images.githubusercontent.com/38211239/159694063-676dc1fb-b89b-4e45-89c0-0217fe1d78fd.png)

aunque antes debéis de estructurar/inicializar el contenido de vuestra base de datos según proceda, por lo que debéis ejecutar un ```makemigrations``` seguido de un ```migrate```.

![Captura de pantalla 2022-03-23 a las 12 55 01](https://user-images.githubusercontent.com/38211239/159694092-93d21e73-a6a8-4187-9d49-99ec6edabc4e.png)
Así como crear un nuevo superusuario.
![Captura de pantalla 2022-03-23 a las 12 55 49](https://user-images.githubusercontent.com/38211239/159694122-af2539b2-944d-4ebc-9b2b-f0faf9e8e3d6.png)
La aplicación ya estaría operativa en este momento.
![Captura de pantalla 2022-03-23 a las 12 55 14](https://user-images.githubusercontent.com/38211239/159694170-f661fc2a-8cd9-4686-bfd6-89956c6c0930.png)

Como complemento, podéis instalar PgAdmin para interactuar con la base de datos de vuestra aplicación. Para ello debéis de establecer la conexión con la misma, que será accesible a través del puerto 5432, tal y como hemos definido.
![Captura de pantalla 2022-03-23 a las 13 00 39](https://user-images.githubusercontent.com/38211239/159695543-2d3fa6f4-3d9b-4652-8a25-a4906dc1df0b.png)
Aquí podréis realizar consultas, como comprobar que el superusuario ```root``` creado previamente ha sido añadido a la base de datos.
 
![Captura de pantalla 2022-03-23 a las 13 01 55](https://user-images.githubusercontent.com/38211239/159695173-53a2f46f-2460-4ff7-8d4c-07658c8d3b83.png)

Nótese que las extensiones que teníamos instaladas localmente en VS Code no serán instaladas por defecto en el contenedor destino, por lo que tendremos que hacerlo nosotros de forma explícita.

![Captura de pantalla 2022-03-23 a las 13 11 14](https://user-images.githubusercontent.com/38211239/159696261-1039f234-be10-4d5d-a081-663842efb406.png)
Para cerrar la conexión con el ```Dev Container``` bastará con pinchar sobre el rectángulo verde en la esquina inferior izquierda y pulsar ```Cerrar conexión remota``` en el Panel de Comandos.

![Captura de pantalla 2022-03-23 a las 13 11 29](https://user-images.githubusercontent.com/38211239/159696288-0fff5670-cb62-432b-a1c1-e60759f9b851.png)

Esto no solo cerrará la conexión en VS Code, sino que finalizará la ejecución de los contenedores asociados.
![Captura de pantalla 2022-03-23 a las 13 13 05](https://user-images.githubusercontent.com/38211239/159696463-f12cd92d-5a54-49fe-8f97-58b8c4daddbf.png)

<img width="1215" alt="Captura de pantalla 2022-03-23 a las 13 13 52" src="https://user-images.githubusercontent.com/38211239/159696675-bdee5f75-1cf7-4d3a-a252-774f32a03f8f.png">

Como parte final de este tutorial, recordar que también podéis crear una plantilla de depuración para una aplicación django cuando creáis vuestro fichero ```launch.json```.
<img width="1136" alt="Captura de pantalla 2022-03-27 a las 11 45 37" src="https://user-images.githubusercontent.com/38211239/160276194-2a0b3124-ca44-45c3-b17e-63043b67bacc.png">

