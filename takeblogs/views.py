from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post # admin.pyにも入っている
# Postクラスの変数をviewで利用する宣言

def index(request):
    takeblogs = Post.objects.order_by('-published')
    print('print log：',takeblogs)
    return render(request, 'takeblogs/index.html',{'takeblogs': takeblogs})
    # order_by＝並び替え　published＝公開・代入
    # htmlに変数を渡すために、render()内に{'posts': posts}と追記
    # レンダリングとは「ある情報を形を変えて表現すること」
    # renderメソッドは、request、template_name、contextという3つの引数を取る

def post_detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id)
    print('print log：',detail)
    return render(request, 'takeblogs/post_detail.html', {'detail': detail})
# get(pk=post_id)というのは、primary_keyが
# post_idに一致する投稿を取ってくる役割
# Create your views here.
