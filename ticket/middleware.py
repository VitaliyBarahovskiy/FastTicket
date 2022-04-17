from .models import Customer
from django.utils.deprecation import MiddlewareMixin

class ProfileMiddlware(MiddlewareMixin):
    def __int__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not hasattr(request.user, 'customer'):
            Customer.objects.create(user=request.user)

        response = self.get_response(request)

        return response
