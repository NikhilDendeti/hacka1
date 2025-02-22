"""
URL configuration for final_one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import signup, login, test_token
from dyslexia_assessment.views import dyslexia_test, get_questions
from game.views import get_gamified_questions, update_score,user_levels_status


# signout,deleteaccount
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('login/', login),
    path('test/', test_token),
    path('dyslexia_test/', dyslexia_test),
    path('get_questions/', get_questions),
    path('start_game/', get_gamified_questions),
    path('update_score/', update_score),
    path('user_levels_status/', user_levels_status)
    

]
