from django.shortcuts import render
from django.http import HttpResponse

from random import randint

from .models import Story, Player, Segment

# note: the story id, player id, etc. will just be the primary keys in the database

def start(request):
#    if create story:
#        create a story
#        return redirect to create_story
#    if join story:
#        return redirect to the join_story page
    return render(request, 'stories/start.html')

def create_story(request):
#    return the story id
#    option to proceed with the story
#    when that is chosen, create the necessary segments and allocate authors
#    then redirect to the wait page
    while True:
        story_id = randint(0,10000)
        try:
            story_id_existing = Story.objects.get(pk=story_id)
        except Story.DoesNotExist:
            break
    s = Story()
    s.save()
    context = {'story_id': story_id}
    return render(request, 'stories/create_story.html', context)

def join_story(request):
#    input story if
#    if story exists:
#        add player to the story
#        redirect to the wait page
#    else:
#        return an error: story does not exist
    story_id = request.POST['story_id']
    context = {'story_id': story_id}
    return render(request, 'stories/join_story.html', context)

def roadmap(request, story_id):
    return HttpResponse(f"Roadmap page, story id {story_id}")

def add_segment(request, story_id, segment_id):
#    display the previous segment
#    prompt input for the current segment
#    redirect to the wait page
    context = {'story_id': story_id, 'segment_id': segment_id}
    return render(request, 'stories/add_segment.html', context)

def wait(request, story_id, segment_id):
#    save the most recent segment
#    there is a button to ask to proceed
#    if not ready:
#        return an error
#    else:
#        redirect to the next segment or to finish
    try:
        segment_content = request.POST['segment_input']
    except KeyError:
        segment_content = "There are no segments yet"
    next_segment = segment_id + 1
    context = {'story_id': story_id, 'recent_segment': segment_content, 'segment_id': next_segment}
    return render(request, 'stories/wait.html', context)

def finish(request, story_id):
#    display all the segments and their authors
    context = {'story_id': story_id}
    return render(request, 'stories/finish.html', context)
