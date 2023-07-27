from django.shortcuts import redirect, render
from .models import Post
from .forms import CommentForm
from .models import Post

# Create your views here.
#The front page html view
def frontpage(request):
    posts = Post.objects.all()
    return render(request,'blog/frontpage.html',{'posts':posts})

#The post_detail html view
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    #check if form was submitted
    if request.method =='POST':
        form = CommentForm(request.POST)

        if form.is_valid(request.POST):
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail',slug=post.slug)
    else:
        form= CommentForm()
        
    return render(request, 'blog/post_detail.html', {'post':post,'form':form})