

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    path('api/register/', RegisterView.as_view(), name='register'),
    
    path('api/token/', obtain_auth_token, name='token'),
    
    
]
from django.contrib import admin
from django.urls import path, include
from accounts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # To handle login and logout views
    path('register/', register, name='register'),
]
from django.urls import path


urlpatterns = [
    # ... (previously defined URLs)
    path('users/<int:user_id>/', views.get_user_info, name='get_user_info'),
    path('users/<int:user_id>/tasks/', views.get_tasks_for_user, name='get_tasks_for_user'),
]
from django.urls import path


urlpatterns = [
    # ... (previously defined URLs)
    path('tasks/<int:task_id>/comments/', views.add_comment, name='add_comment'),
    path('tasks/<int:task_id>/comments/<int:comment_id>/', views.update_delete_comment, name='update_delete_comment'),
    path('tasks/<int:task_id>/comments/', views.get_comments, name='get_comments'),
]
