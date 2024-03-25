# planet_world/views.py

from django.views.generic import View
from django.shortcuts import render

class ProfileView(View):
    def get(self, request):
        """ A view to display the user's profile """
        return render(request, 'planet_world/profile.html')
