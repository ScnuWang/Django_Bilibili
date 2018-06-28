```html
 <!--如果使用get_list_or_404（Blog）查询，则会报错 -->
    {% empty %}
        <p>-- 小主，催更人带着杀猪刀来了 --</p>
    {% endfor %}
```

```html
{# 长文本截取:建议大家这里truncatechars改用truncatechars_html，因为truncatechars可能会有因html截取不全导致html错乱问题       #}
        <p>{{ blog.content|truncatechars_html:50 }}</p>
```

```css
/* 去掉最后一行的线*/
div.blog:not(:last-child){
    margin-bottom: 2em;
    padding-bottom: 1em;
    border-bottom: 1px solid #eeeeee;
}
```

Blog.objects.filter():是函数，后面的过滤条件不能直接给不等号类似条件--->使用条件修饰符:created_time__gt，created_time__lt等

```python
# 给类新增属性：blog_count;for循环里面新增的属性是临时属性
blog_count_with_type=[]
for blog_type in BlogType.objects.all():
    blog_type.blog_count = Blog.objects.filter(blogtype=blog_type).count()
    blog_count_with_type.append(blog_type)
    
    
blog_count_with_type = BlogType.objects.annotate(blog_count=Count('blog')) # 与上述代码等效；blog为BlogType关联的对象小写
```

```python
# 获取最近7天的阅读量数据
def get_seven_read_data(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(7,0,-1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        readDetail = ReadDetail.objects.filter(content_type=content_type,date=date)
        result = readDetail.aggregate(read_num_sum = Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)

    return read_nums,dates
```

```python
# 校验用户是否登录，通过这种方式传递user
    def __init__(self,*args,**kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm,self).__init__(*args,**kwargs)
```

django.contrib.auth.context_processors.auth默认配置在settings文件中，这个方法会返回user,故可以通过request.user获取

action的值如果不写或者写成#号，表示是提交到当前方法

阅读次数统计方案：
1. 根据request来统计，每次请求，阅读次数加1,统计数字不准确，例如F5刷新也算一次
2. 根据Cookie来统计，数据相对比较准确，统计数据单一，不能统计某一个时间段的访问量,后台编辑文章的时候，如果有人访问，数据不会被记录
3. 根据Cookie来统计，将统计次数新建一个模型ReadNum，与博客建立一对一的关系，这样在修改Blog的时候,不会影响ReadNum,反之亦然；如果有多个模块（公告，个人简介，教程等）需要引用到计数的话，那么管理起来会比较乱
4. 使用[ContentType](https://docs.djangoproject.com/en/2.0/ref/contrib/contenttypes/)(项目里面所有注册的应用所包含的模型的相关信息都能通过使用ContentType查询出来)


list(filter(lambda x:  'Input' in x,dir(forms)))
过滤器(filter),取出每一个（lambda x）, 从集合里面取（dir(forms)）,对每一个做出操作（判断是否包含'Input'）

如果不确定是否包含这个键值对，就不要直接用['key']来取值，用get('key'),这样的话如果为空呢，会返回None

在blog_detail.html总添加代码块，需要先在base.html上面添加，不然不会被渲染