import app.models.functions.s3Storage as s3


class Uploader:
    @staticmethod
    async def upload(_id, binary_data, dir_name):
        return s3.upload(_id, binary_data, dir_name)
