from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm

# Create your views here.
def add_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        comment.delete()
        return redirect('comment_list')
    return render(request, 'blog/delete_comment.html', {'comment': comment})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'blog/comment_list.html', {'comments': comments})
