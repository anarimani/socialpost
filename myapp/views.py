from django.shortcuts import render, redirect
from .forms import PostForm
from .social_media import post_to_telegram
from .utils import save_image
import asyncio

def home(request):
    return render(request, 'home.html')

async def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            text = form.cleaned_data['text']
            image_path = save_image(image)
            await post_to_telegram(image_path, text)
            return redirect('success')
            send_whatsapp_message(image_path, text)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

def success(request):
    return render(request, 'success.html')
