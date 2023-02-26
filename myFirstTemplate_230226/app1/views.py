# from django.shortcuts import render

# Create your views here.

# -----(其他)---------
# 時間需要
from datetime               import datetime

from django.forms.widgets   import datetime_safe
# 用 model
from app1.models            import Post
from django.shortcuts       import render
# ----------------------------------------
##   當你這個 view 有很多 templete 時候 get_template 可以幫你選版 通常是中間的 base.html
##   再用 HttpResponse(html) 去把你要的畫面拼出來
from django.template.loader import get_template
from django.http            import HttpResponse

def homepage(request):
    link_admin = True
    if link_admin:
        template      = get_template('index.html')
        content_posts = Post.objects.all()
        now           = datetime.now()
        html          = template.render(locals())
        return HttpResponse(html)
    else:
        return HttpResponse('<h1>Tryyyyyyyyyyyyyyyyy</h1>')

