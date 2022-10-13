# FastApi-JYVD

from fastapi.responses import JSONResponse
easyWSL

class MiError(Exception):
    pass
def funcion (n1:int=0,n2:int=0)->int:
    if n1<0:
        raise MiError("N1 no puede ser negativo")
    else:
        return n1+n2

## Instalar fastapi 
```bash
pip install fastapi uvicorn
```

## Instalar python3 y PIP
```bash
sudo apt install python3 python3-pip
```

## Indexar archivos nuevos al repositorio
```bash
$ git add .
```

## Crear un commit con los cambios
```bash
git commit -m "UPDATED estructura del proyecto"
```

## Actualizar los cambios uniendo ambas partes
```bash
$ git merge
```

## Actualizar el repositorio en GitHub
```bash
$ git push -u origin main
```

## Actualizar todo los cambios de la maquina a GitHub de forma forzada

```bash
$ git push -f origin main
```
## Sincronizar todo el trabajo de github

```bash
$ git pull
```



## Verificar el SO

```bash
uname -a
```

## Verificar el kernel

```bash
sudo apt install neofetch
neofech
```
## Instalar librerias desde un archivo de texto

```bash
pip3 install -r *nombre del archivo*
```

## Ver las librerias de las versiones instaladas de las librerias y dependencias

```bash
pip3 freeze
```

## Mandar la salida del comando hacia otro archivo

```bash
pip3 freeze>*nombre del archivo*
```

## Crear una base de datos y mandar el scrip

```bash
sqlite3 base.db<base.sql
```
## Ver procesos

```bash
ps -a
```

## Terminar un proceso

```bash
kill *PID*
```
## Terminar procesos forzandolo

```bash
kill -9 *PID*
```