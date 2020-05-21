from django.shortcuts import render
from django.http import HttpResponse
from .models import Post # admin.pyにも入っている
# Postクラスの変数をviewで利用する宣言

def index(request):
    takeblogs = Post.objects.order_by('-published')
    return render(request, 'takeblogs/index.html',{'takeblogs': takeblogs})
    # order_by＝並び替え　published＝公開・代入
    # htmlに変数を渡すために、render()内に{'posts': posts}と追記
    # レンダリングとは「ある情報を形を変えて表現すること」
    # renderメソッドは、request、template_name、contextという3つの引数を取る

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'takeblogs/post_detail.html', {'post_id': post_id})
# get(pk=post_id)というのは、primary_keyが
# post_idに一致する投稿を取ってくる役割
# Create your views here.
