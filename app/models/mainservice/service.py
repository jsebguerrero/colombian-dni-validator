from app.models.requestparser.requestanalyser import RequestAnalyser
from app.models.imageprocessing.imageanalyser import ImageAnalyser
from app.models.cloudservice.uploader import Uploader
from app.models.functions import utilities


class Service:
    def __init__(self):
        date, sqldate = utilities.getDate()
        self.request_analyser = RequestAnalyser()
        self.image_anaylser = ImageAnalyser()
        self.uploader = Uploader()
        self.date = date
        self.id = None
        self.img = ''
        self.upload_status = ''
        self.angle = 0
        self.scope = ''
        self.error = ''
        self.error_message = ''
        self.barcode_items = 0
        self.url = ''

    async def validate_request(self, request):
        info = await self.request_analyser.validate_request(request)
        self.img = info['img']
        self.id = info['id']
        self.scope = info['scope']
        self.error = info['error']
        self.error_message = info['message']

    def verify_id(self, dnitype):
        if not self.error:
            result = self.image_anaylser.verify_id(self.img, dnitype)
            self.error = result['error']
            self.error_message = result['message']
            self.img = result['img']
        else:
            pass

    def parse_img(self):
        if not self.error:
            result = self.image_anaylser.parse_img(self.img)
            self.error = result['error']
            self.error_message = result['message']
            self.img = result['img']
        else:
            pass

    """async def verify_back_id(self):
        if not self.error:
            result = self.image_anaylser.verify_id(self.img, self.scope.split('/')[-1])
            self.error = result['error']
            self.error_message = result['message']
            #self.barcode_items = result['barcode']
            self.img = result['img']
        else:
            pass"""

    async def upload_image(self):
        if not self.error:
            _dir = self.scope.split('/')[-1]
            if 'frontal' in self.scope.split('/')[-1] or 'pasaporte' in self.scope.split('/')[-1]:
                _dir = 'cedula'
            if 'selfie' in self.scope.split('/')[-1]:
                _dir = 'fotoRegistro'
            response = await self.uploader.upload(self.id,
                                                  self.img,
                                                  _dir)
            self.upload_status = response['status']
            self.error = response['error']
            self.error_message = response['message']
            self.url = response['url']
        else:
            pass
