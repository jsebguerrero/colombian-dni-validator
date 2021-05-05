# About

Imagen is a web service designed to identify Colombian ID photos

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
queryparams : id -> id number

body  : images[] -> imagen

### Respuestas
```bash
200 -> OK
400 -> image did not pass requirements
```
