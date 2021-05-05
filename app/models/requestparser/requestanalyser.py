class RequestAnalyser:
    @staticmethod
    async def validate_request(request):
        response = {'message': []}
        _id = request.query_params.get('id') if request.query_params.get('id') else False
        scope = request.scope['path'] if request.scope['path'] else False
        data = await request.form()
        try:
            img1 = data.getlist('images[]')[0].file.read()
        except IndexError:
            img1 = False
        if not img1:
            response['message'].append('app invalida')
        if not _id:
            response['message'].append('no hay numero de identificacion, no se puede proceder')
        response.update({'id': _id,
                         'img': img1,
                         'scope': scope,
                         'error': True if response['message'] else False})
        return response
