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