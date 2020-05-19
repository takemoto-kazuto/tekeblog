from django.shortcuts import render
from django.http import HttpResponse
from .models import Post # admin.pyにも入っている
# Postクラスの変数をviewで利用する宣言

def index(request):
    posts = Post.objects.order_by('-published')
    return render(request, 'takeblogs/index.html',{'posts': posts})
    # order_by＝並び替え　published＝公開・代入
    # htmlに変数を渡すために、render()内に{'posts': posts}と追記
    # レンダリングとは「ある情報を形を変えて表現すること」
    # renderメソッドは、request、template_name、contextという3つの引数を取る

# Create your views here.
