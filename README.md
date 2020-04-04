# README

## Configuracion inicial

### Clonar repo-create

`git clone https://github.com/Apolofx/github-wrapper.git`

### GitHub personal token

1. Ir a la seccion Settings en tu sesion de GitHub.
2. Ir a la pestaña Developer settings en la columna de la izquierda.
3. Seleccionar Personal acces tokens
4. Elegir Generate new toker
5. Seleciconar el scope de permisos que vas a tener mediante la API.
6. Generar el token
7. Ir al directorio del script, y en el archivo `keys.py` reemplazar el valor del campo GITHUB_API_KEYS por el token obtenido previamente.

### Agregar repositorio al PATH

#### Linux

1. Abrir el archivo `.bashrc` que esta en tu `/home` (por ejemplo, `/home/tu-nombre-de-usuario/.bashrc`) en un editor de texto.
2. Agregar `export PATH="tu-dir:$PATH"` al final del archivo, donde tu dir es el directorio donde esta guardado `repo-create.py`.
3. Guardar el archivo `.bashrc`.
4. Reiniciar el terminal.

#### Mac OS X

1. Abrir el archivo `.bash_profile`que esta file en tu `/home` (por ejemplo, `Users/tu-nombre-de-usuario/.bash_profile`) en un editor de texto.
2. Agregar `export PATH="tu-dir:$PATH"` al final del archivo, donde tu dir es el directorio donde esta guardado `repo-create.py`.
3. Guardar el archivo `.bash_profile`.
4. Reiniciar el terminal.

### Agregar permisos y Alias

1. Dentro de la carpeta del script, corremos `chmod +x repo-create.py`
2. (Opcional) Agregamos el alias para no tener que escribir `'.py'`. Abrimos nuestro `.bash_alias` y le agregamos la linea `alias repo-create='repo-create.py'`

## Features

El script crea un repositorio remoto en GitHub consumiendo la GitHub API con peticiones https.

## Modo de uso

1. cd ~/dir-del-proyecto/
2. git init
3. git add .
4. git commit -m 'initial commit'
5. repo-create

## TODO

Agregar delete repo permission y metodo.
