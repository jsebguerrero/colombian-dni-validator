# import zxing
import pytesseract
import os, cv2
from run import PATH
from app.models.functions.image_functions import *


class ImageAnalyser:

    @staticmethod
    def verify_id(img, scope):
        result = {
            'error': False,
            'message': '',
            'img': False
        }

        keywords_front = ['REPUBLICA', 'COLOMBIA', 'IDENTIFICACION', 'PERSONAL', 'CEDULA', 'CIUDADANIA', 'TARJETA',
                    'IDENTIDAD', 'EXTRANJERIA', 'TEMPORAL']
        keywords_back = ['NACIMIENTO', 'SEXO', 'REGISTRADOR',
                    'NACIONAL', 'FECHA', 'LUGAR', 'EXPEDICION',
                    'RH', 'VENCIMIENTO']
        keywords_passport = ['REPUBLICA', 'COLOMBIA', 'PASAPORTE', 'PASSPORT', ]
        counterword = 0
        #image processing
        img = preprocess_img(img, scope)
        pre_text = thresholding(get_grayscale(img))
        faces, img = verify_faces(img, scope)
        ocr = pytesseract.image_to_string(pre_text)
        #OCR CHECKS
        if scope == 'id_frontal' or scope == 'pasaporte':
            if scope == 'id_frontal':
                for keyword in keywords_front:
                    if keyword in ocr.upper():
                        counterword += 1
            else:
                for keyword in keywords_passport:
                    if keyword in ocr.upper():
                        counterword += 1
            if counterword >= 3:
                if faces == 1:
                    success, encoded_image = cv2.imencode('.jpg', img)
                    result.update({'img': encoded_image.tobytes()})
                else:
                    result.update({'img': False, 'error': True,
                                   'message': 'La app no corresponde a cara frontal de un DNI colombiano'})
            elif ocr != '\n\f' and faces == 1:
                result.update({'img': False, 'error': True,
                               'message': 'Por favor tomar mejor la foto, no es posible distinguir el documento'})
            else:
                result.update({'img': False, 'error': True,
                               'message': 'Imagen invalida'})
        elif scope == 'id_anverso':
            for keyword in keywords_back:
                if keyword in ocr.upper():
                    counterword += 1
            if counterword and not faces:
                    success, encoded_image = cv2.imencode('.jpg', img)
                    result.update({'img': encoded_image.tobytes()})
            elif ocr != '\n\f' :
                result.update({'img': False, 'error': True,
                               'message': 'Por favor tomar mejor la foto, no es posible distinguir el documento'})
            else:
                result.update({'img': False, 'error': True,
                               'message': 'La imagen no corresponde a cara trasera de un DNI colombiano'})
        else:
            result.update({'img': False, 'error': True, 'message': 'imagen invalida'})

        return result

    """
    @staticmethod
    def verify_back_id(img, id, scope):
        result = {
            'error': False,
            'message': [],
            'barcode': None
        }

        img = preprocess_img(img, scope)
        reader = zxing.BarCodeReader()
        data = None
        for i in range(2):
            try:
                mpath = os.path.join(PATH, str(id) + '.jpg')
                cv2.imwrite(mpath, img)
                barcode = reader.decode(mpath, True)
                data = list(filter(None, barcode.raw.split('\x00')))
                os.remove(mpath)
                break
            except AttributeError:
                os.remove(mpath)
                img = cv2.rotate(img, cv2.ROTATE_180)
        if data:
            success, encoded_image = cv2.imencode('.jpg', img)
            result.update({'barcode': [data[i] for i in range(2, 8)],
                           'img': encoded_image.tobytes()})
        else:
            result.update({'barcode': False,
                           'error': True,
                           'message': 'no se recibio parte trasera de cedula',
                           'img': False})
        return result"""

    @staticmethod
    def parse_img(img):
        result = {
            'error': False,
            'message': '',
            'img': None
        }
        img = transform_image(img)
        img = equalize_histogram(img)
        success, encoded_image = cv2.imencode('.jpg', img)
        result.update({'img': encoded_image.tobytes()})
        return result
