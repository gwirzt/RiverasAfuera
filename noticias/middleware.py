from django.http import JsonResponse


class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.TOKEN = '7939d2aefc22439bbf16da778c2c2628'  # Define tu token fijo aquí

    def __call__(self, request):
        token = request.headers.get('Authorization')
        print(f"Received token: {token}")  # Agrega esta línea para depurar

        if not token or not token.startswith('Token '):
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        token = token.split(' ')[1]
        if token != self.TOKEN:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response
