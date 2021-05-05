from app import app
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.models.mainservice import service as svc
from app.version import VERSION


@app.post('/imagen/webapi/{dnitype}')
async def verify_dni(request: Request, dnitype):
    valid_types = ['id_frontal', 'id_anverso', 'pasaporte', 'selfie']
    if dnitype in valid_types:
        # objeto service
        service = svc.Service()
        # verificar y sacar info de la request
        await service.validate_request(request)
        # procesar
        if 'id_frontal' in dnitype or 'id_anverso' in dnitype or 'pasaporte' in dnitype:
            service.verify_id(dnitype)
        elif 'selfie' in dnitype:
            service.parse_img()
        # subir foto
        await service.upload_image()
        if service.error or not service.upload_status:
            return JSONResponse(content={'error': service.error_message},
                                status_code=400)
        else:
            return JSONResponse(content={'status': 'success',
                                         'url': service.url},
                                status_code=200)
    else:
        return JSONResponse(content={'status': 'NOT ALLOWED'},
                            status_code=500)


@app.get("/imagen/webapi")
async def home():
    # respuesta para verificar si esta en linea
    return JSONResponse({'message': 'online'})


@app.get('/imagen/webapi/health')
def health():
    return JSONResponse(content={'health': 'healthy', 'version': VERSION},
                        status_code=200)
