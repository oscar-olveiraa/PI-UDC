#!/bin/bash
# Script para crear los contenedores y crear el usuario con datos precargados

dir_base=`dirname $(readlink -f $0)`;
dir_origen=`pwd`

green="\e[0;32m\033[1m"
end="\033[0m\e[0m"
red="\e[0;31m\033[1m"
blue="\e[0;34m\033[1m"
yellow="\e[0;33m\033[1m"
purple="\e[0;35m\033[1m"
turquoise="\e[0;36m\033[1m"
gray="\e[0;37m\033[1m"
white="\e[0;97m\033[1m"

if [[ $1 == "clean" ]];then
	containers=`docker ps -a | tail -n+2 | grep 'nutrifit' | cut -d ' ' -f 1`
	imagenes=`docker images | tail -n +2 | sed -E 's/ +/ /g'| grep -E 'nutrifit|postgres' | cut -d ' ' -f 3`
	volumenes=`docker volume ls | tail -n +2 | sed -E 's/ +/ /g' | grep 'postgres' | cut -d ' ' -f 2`

	for contenedor in $containers;
	do
        	docker rm -f $contenedor;
	done;

	for imagen in $imagenes;
	do
        	docker rmi -f $imagen;
	done;

	for volumen in $volumenes;
	do
        	docker volume rm -f $volumen;
	done;
	exit;
fi

cd $dir_base/.devcontainer
echo -e "${red}[${green}+${red}]${end} docker-compose up --build -d"
docker-compose up --build -d 
echo -e "${red}[${green}+${red}]${end} python3 manage.py makemigrations"
docker exec devcontainer_nutrifit_1 python3 /workspace/nutrifit/manage.py makemigrations
echo -e "${red}[${green}+${red}]${end} python3 manage.py migrate"
docker exec devcontainer_nutrifit_1 python3 /workspace/nutrifit/manage.py migrate
echo -e "${red}[${green}+${red}]${end} python3 manage.py runserver 0.0.0.0:8000"
docker exec -d devcontainer_nutrifit_1 python3 /workspace/nutrifit/manage.py runserver 0.0.0.0:8000
echo -e "${red}[${green}+${red}]${end} Creando usuario con datos precargados"
# El sleep y el bucle es porque el servidor tarda un tiempo en arrancar
while ! $(curl -L localhost:8000/aux/createuser 1>/dev/null 2>&1);
do
	sleep 1;
done
echo -e "${red}[${green}+${red}]${end} Credenciales del usuario creado:    ${green}test@nutrifit.com${white}:${green}1234${end}"
