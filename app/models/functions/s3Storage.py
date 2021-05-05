import boto3, os
from boto3.exceptions import S3UploadFailedError
from botocore.exceptions import ClientError
from settings_handler import settings


def s3_instance():
    return boto3.resource('s3')


def upload(_id, binary_data, dir_name):
    error = False
    message = False
    photo_path = str(_id) + '/' + dir_name + '/'
    photo = str(_id) + '.' + str(os.getenv('PHOTO_TYPE'))
    path = photo_path + photo
    try:
        s3 = s3_instance()
        request = s3.Object(str(os.getenv('BUCKET_NAME')),
                            path)
        request.put(Body=binary_data)
    except S3UploadFailedError:
        error = True
        message = 'error en subida a s3'

    except ClientError:
        error = True
        message = 'error de credenciales'

    return {'status': 'uploaded',
            'url': path,
            'error': error,
            'message': message}
