"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
# importは画像などの静的ファイルを読み込むために必要なパッケージを入れている。
from django.conf import settings
# settings.pyというファイルを読み込むためのコード
from takeblogs import views
# from django.conf.urls.static import static
# from django.conf import settings
# from django.urls import include, path

urlpatterns = [
    url('admin/', admin.site.urls),
    url('takeblogs/', include('takeblogs.urls')),
    url(r'^takeblogs/(?P<post_id>[0-9]+)/$', views.post_detail, name = "post_detail")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatternsの後ろにstatic()で表示するデータのurlの設定と、
# そのデータをどこに表示しているかを指定
# 正規表現（英：regular expression）とは
# 文字列を特定する際に、曖昧な感じで指定ができる表現方法のこと

    # path('admin/', admin.site.urls),
    # path('^posts/', include('posts.urls')),
