# Stories URL file

from django.urls import path

from . import views

app_name = 'stories'
urlpatterns = [
    path('', views.start, name='start'),
    path('create_story/', views.create_story, name='create_story'),
    path('join_story/', views.join_story, name='join_story'),
    path('roadmap/<int:story_id>/', views.roadmap, name='roadmap'),
    path('add_segment/<int:story_id>/<int:segment_id>/', views.add_segment, name='add_segment'),
    path('wait/<int:story_id>/<int:segment_id>', views.wait, name='wait'),
    path('finish/<int:story_id>/', views.finish, name='finish'),
]

#note: wait has a segment id because we need to know what the last segment was to get to the next one