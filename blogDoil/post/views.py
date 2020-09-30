from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator


def read_blog_list(request):
    blogs = Blog.objects.all()
    #몇개씩 볼건지
    paginator = Paginator(blogs, 2)
    #지금 보려는 페이지는 무엇?
    page = request.GET.get('page')
    #새로 담아서 보내주기
    posts = paginator.get_page(page)
    return render(request, 'post/blog_list.html', {'posts': posts})

def read_blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'post/blog_detail.html', {'blog': blog})
# blog라는 이름의 blog(get_object_or_404...)를 post/blog_detail.html에 뿌려주겠다는 뜻...

def blog_new(request):
    return render(request, 'post/blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    #BLOG element 채우기
    blog.save() #DB에 저장되는 함수
    return redirect('read_blog_list') # 어느 페이지로 갈지

def update_blog(request, blog_id):  #url, html 에서도 처리해주기
    #객체 탐색
    blog = get_object_or_404(Blog, pk = blog_id)
    #데이터 입력
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        #데이터 저장
        blog.save()

        return redirect('read_blog_detail', blog.id)

    return render(request, 'post/blog_update.html', {'blog': blog})

def delete_blog(request, blog_id):  #url, html 에서도 처리해주기
    #객체 탐색
    blog = get_object_or_404(Blog, pk = blog_id)
    #삭제
    blog.delete()
    #리스트 페이지로 가기
    return redirect('read_blog_list')
