from django.shortcuts import render
from django.views import View
from profile_app.models import Profile


class Profile_User(View):
    """Класс профайла"""

    def get(self, request):
        """Представление профайла пользователя"""

        user = Profile.objects.get(user=request.user)
        contex = {
            'title': 'Profile',
            'avatar': user,
        }
        return render(request, "profile.html", contex)