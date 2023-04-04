from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    for video in videos:
     print(video.video_file.url)
    context = {
        'videos': videos
    }
    return render(request, 'video_list.html', context)


from django.shortcuts import render, redirect
from .forms import VideoForm

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})
