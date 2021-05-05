# About

Imagen es el servicio destinado a revisar cédulas de ciudadanía y subir fotos a s3

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install requirements.txt
```

## Usage
```bash
python3 run.py // python run.py si tienes anaconda
```

## Endpoints
```bash
/imagen/webapi/id_frontal
/imagen/webapi/id_anverso
```
queryparams : id -> numero de cedula

body  : images[] -> imagen

### Respuestas
```bash
200 -> imagen está bien, se subió a s3
400 -> imagen no valida ya sea por mucho brillo o mal tomada, no se sube a s3
```
