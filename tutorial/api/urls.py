from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import users.views
from users import views
from django.urls import include, path
import snippets.views
import users.views
from api import views


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.test.api_root),
    path('snippets/',
        snippets.views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        snippets.views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        snippets.views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        users.views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        users.views.UserDetail.as_view(),
        name='user-detail'),
    # path('rest-auth/',
    #      include('rest_auth.urls'),
    #      name='authauth',
    #      ),

])