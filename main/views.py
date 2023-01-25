from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts=Post.objects.all()
    
    ctx={
        'posts':posts,
    }
    return render(request,'main/post_list.html',ctx)
    
def post_create(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx={
                'form':form,
            }
            return render(request,'main/post_create.html',ctx)
    
    elif request.method=='GET':
        form=PostForm()
        ctx={
            'form':form,
        }
        
        return render(request,'main/post_create.html',ctx)
    
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def like_ajax(request):
    req=json.loads(request.body)
    post_id=req['id']
    
    post=Post.objects.get(id=post_id)
    
    post.like+=1
    
    post.save()
    
    
    return JsonResponse({'id':post_id})

@csrf_exempt
def comment_create(request):
    req=json.loads(request.body)
    post_id=req['id']
    post_comment=req['comment']
    
    post=Post.objects.get(id=post_id)
    
    post.comment=post_comment
    
    post.save()
    
    return JsonResponse({'id':post_id, "comment":post_comment})
    