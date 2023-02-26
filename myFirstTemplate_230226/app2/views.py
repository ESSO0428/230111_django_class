# from django.shortcuts     import render

# Create your views here.



# from django.shortcuts     import render

# Create your views here.

# -----(其他)---------
# 時間需要
from datetime               import datetime
from re import template
# 用 model
from app2.models            import Post, Product
# ---------------------------------------
##  寫法<2> 使用 render 直接簡短渲染寫法
from django.shortcuts       import render
## render 與底下的 HttpResponse 將會將
## templete 抓來用，再回傳給使用者
# ----------------------------------------
 ##  寫法<3> 使用到 get_template  & HttpResponse
 ##   當你這個 view 有很多 templete 時候 get_template 可以幫你選版 通常是中間的 base.html
 ##   再用 HttpResponse(html) 去把你要的畫面拼出來
from django.template.loader import get_template
from django.http            import HttpResponse
##################################
#     Create your views here.    #
##################################
##  寫法<1> 直接印 html
def pageApp2(request):
    html = '''
    <h1>This is a test page App2....</h1>
    <h2>~~~~~~~~~~~~~~~~~~~~~~~~</h2>
    <hr>
    <p>tryyyyyyyyyyyyyyyyyyy</p>
    
    
    <br>
    <br>
    <h3>TEST</h3>
    '''
    link_admin = True
    if link_admin:
        template      = get_template('index.html')
        content_posts = Post.objects.all()
        now           = datetime.now()
        html          = template.render(locals())
        return HttpResponse(html)
    else:
        return HttpResponse(html)

# """

class BaseHtmlTemplate:
    # step1
    def __init__(self, link_admin, html, SourceTemplat):
        self.link_admin    = True
        self.html          = ''
        self.SourceTemplat = 'index.html'

        self.link_admin    = link_admin
        self.html          = html
        if SourceTemplat != '':
            self.SourceTemplat = SourceTemplat
    # step3 (run it from outsite)
    # base template
    def exc_render(self):
        html = self.html
        if self.link_admin:
            # template      = get_template('index.html')
            SourceTemplat   = self.SourceTemplat
            template        = get_template(SourceTemplat)
            # content_posts = Product.objects.all()
            # now           = datetime.now()
            Dictlocals      = locals()
            self.GetContent()
            Dictlocals.update(self.dictUpdateValue)
            # html          = template.render(locals())
            html            = template.render(Dictlocals)
            # print(Dictlocals)
            # return HttpResponse(html)
        else:
            # return HttpResponse(html)
            pass
        self.html = html
    # step2 (don't use it from outsite)
    # DLC
    def GetContent(self):
        content_posts        = Product.objects.all()
        # content_posts      = Product.objects.all()[:2]
        now                  = datetime.now()
        dictUpdateValue      = {
            "content_posts" : content_posts,
            "now"           : now
        }
        self.dictUpdateValue = dictUpdateValue
    def get_render_result(self):
        return self.html
# 繼承上面的 class 並且可以覆蓋繼承的方法 (def 取相同名稱)
class NeoHtmlTemplate(BaseHtmlTemplate):
    # def GetContent(self):
    #     return super().GetContent()

    def GetContent(self):
        # content_posts      = Product.objects.all()
        content_posts        = Product.objects.all()[:2]
        now                  = datetime.now()
        dictUpdateValue      = {
            "content_posts" : content_posts,
            "now"           : now
        }
        self.dictUpdateValue = dictUpdateValue

class FormTemplate(BaseHtmlTemplate):
    def GetContent(self):
        if self.request.method == 'POST':
            message = ''
        else:
            message = f"感謝您的來信; 傳值方式為 : {self.request.method}"
        log = """
            原本要用 form 的範例簡單寫個 app 但沒寫完 (目前還只能在 view 內傳值，且 POST 未能傳值成功
            <br />
            這網頁渲染的有夠差，之後還要套模板。
        """
        dictUpdateValue = {
            "message"      : message,
            "Log"          : log,
            "user_name"    : "Andy6",
            "user_city"    : "user city",
            "user_school"  : "NCHU",
            "user_email"   : "XXX@gmail.com",
            "user_message" : "Talk ........",
        }
        self.dictUpdateValue = dictUpdateValue 

# 物件寫出來了底下的 def 可以刪除了
def repeat_code(link_admin=True, html='', SourceTemplat='index.html', List = []):
    
    if link_admin:
        # template      = get_template('index.html')

        template      = get_template(SourceTemplat)
        content_posts = Product.objects.all()
        now           = datetime.now()
        html          = template.render(locals())
        # return HttpResponse(html)
    else:
        # return HttpResponse(html)
        pass
    return html
# """
def ntab1(request):
    html = '''
    <h1>製作比先前測試頁再正式一點點點....的網頁 (維護中)</h1>
    '''
    link_admin      = True
    # SourceTemplat = 'try_bootstrap.html'
    SourceTemplat   = 'index.html'

    BaseTemplate = True
    if BaseTemplate: 
        MyObjTemplat = BaseHtmlTemplate(link_admin, html, SourceTemplat)
    else:
        MyObjTemplat = NeoHtmlTemplate(link_admin, html, SourceTemplat)
    MyObjTemplat.exc_render()
    html = MyObjTemplat.get_render_result()

    # html            = repeat_code(link_admin, html, SourceTemplat)

    ## template        = get_template(SourceTemplat)
    ## html            = template.render(locals())
    return HttpResponse(html)

# """
import random
def about(request):
    quotes = [
        '今日事，今日畢',
        '要怎麼收穫，先怎麼栽',
        '知識就是力量',
        '一個人的個性就是他的命運'
    ]
    quote = random.choice(quotes)
    return render(request, 'about.html', locals())


def LISTING(request, yr, mon, day):
    html = "<h2>List Date is {}/{}/{}</h2><hr>".format(yr, mon, day)
    return HttpResponse(html)

def listing(request):
    html = '''
    <h1>django 變數傳值 : 維護中 !!!!</h1>
    '''
    # print(html)

    link_admin = True
    SourceTemplat = ''
    SourceTemplat = 'contact.html'
    # html       = repeat_code(link_admin, html)

    BaseTemplate = False
    if BaseTemplate: 
        MyObjTemplat = BaseHtmlTemplate(link_admin, html, SourceTemplat)
    else:
        MyObjTemplat         = FormTemplate(link_admin, html, SourceTemplat)
        MyObjTemplat.request = request
    MyObjTemplat.exc_render()
    html = MyObjTemplat.get_render_result()
    print(html)


    return HttpResponse(html)

def bootstrap(request):
    html = '''
    <h1>bootstrap 模板套用 : 維護中 !!!!</h1>
    '''
    link_admin      = True
    # SourceTemplat = 'try_bootstrap.html'
    SourceTemplat   = 'Bbase.html'
    # MyObjTemplat = BaseHtmlTemplate(link_admin, html, SourceTemplat)
    # MyObjTemplat.exc_render()
    # html = MyObjTemplat.get_render_result()

    MyObjTemplat = NeoHtmlTemplate(link_admin, html, SourceTemplat)
    MyObjTemplat.exc_render()
    html = MyObjTemplat.get_render_result()

    # html            = repeat_code(link_admin, html, SourceTemplat)

    ## template        = get_template(SourceTemplat)
    ## html            = template.render(locals())
    return HttpResponse(html)


### 寫法<2> 使用 render 渲染
#def homepage(request):
#    content_posts = Post.objects.all()
             # content_posts = Post.objects.all()[0:3]  ##  選取 list 裡面幾個
#    now = datetime.now()
#    return render(request, 'index.html', locals())
# --------------------------------------------------------
##  寫法<3> 透過 html 去印出
