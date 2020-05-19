from django.conf.urls import url
#django.httpという便利箱から、
# HttpResponseという便利グッズを使いますと宣言している
from . import views
#これは、同じディレクトリ階層（"."は同じ階層を表す）の中の
# views.pyというファイルを読み込みますという宣言である。
urlpatterns = [url(r'^$',views.index, name = 'index')]
#ユーザーが渡してきたurlがアプリ内でどのファイルを読み込むべきかを記します
#コードの意味としては、r''の部分に記述したurlが渡された時に、
# viewsファイルの中の、indexというクラスを実行してください


