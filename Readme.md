# __Diploma__ 
___

## __Project *Bee*__
___


### 
__Тема диплома:__<br/>

__"Интернет-магазин на Django", который должен соответствовать следующим требованиям:__

- *Реализация авторизации/регистрации пользователя.*<br/>
- *Реализация профиля пользователя.*<br/>
  - *должна быть возможность загрузки картинок;*<br/>
- *Реализация товаров.*<br/>
  - *должна быть возможность загрузки картинок;*<br/>
  - *максимальное количество картинок в одной записи: 5 ;*<br/>
- *Реализация избранных товаров.*<br/>
- *Реализация отзывов к товару.*<br/>
  - *должна быть возможность загрузки картинок;*<br/>
  - *максимальное количество картинок в одной записи: 5 ;*<br/>
- *Реализация рейтинга к товару.*<br/>
- *Реализация истории просмотра товаров.*<br/>


***Важное замечание:***
- *Функционал должен быть продублирован как в формах, так и через API с использованием DRF !*<br/>
- *Развернуть свой дипломный проект на Heroku !*<br/>
<br/>

~~~python
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from catalog_app.models import Media
from catalog_app.models import Post
from category_app.models import Tag


class CatalogPageView(View):
    """Каталог товаров"""

    def get(self, request):
        """Представление каталога товаров"""

        posts = Post.objects.filter(is_public=True).order_by('-created_at')

        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if posts:

            tag = Tag.objects.annotate(count=Count("post")).order_by("-count")[:5]
            image_post = []
            for post in posts:
                image_post.append(Media.objects.filter(post=post).first)
            contex = {
                      "posts": posts,
                      "image_post": image_post,
                      "tag": tag,
                      "page_obj": page_obj,
                      }
        else:
            contex = {
                      "error": "Oops, this item may have been removed =/",
                      }
        return render(request, 'all_catalog.html', contex)
~~~
**Полный код Интернет-магазина на Django** (*Python* + *HTML* + *CSS* + *JavaScript*) **находится по ссылке** [**сlick me.**](https://github.com/DarthVaderOn/Diploma)

## **Скриншоты Интернет-магазина на Django**
___
### 
- *Реализация регистрации пользователя.*<br/>
<a href="https://ibb.co/sHwXsm2"><img src="https://i.ibb.co/jRMj36T/6.png" alt="6" border="0" /></a>

- *Реализация авторизации пользователя.*<br/>
<a href="https://ibb.co/gtHCVqH"><img src="https://i.ibb.co/QYzGdSz/5.png" alt="5" border="0" /></a>

- *Реализация товаров.*<br/>
<a href="https://ibb.co/Sy4NxRy"><img src="https://i.ibb.co/3d91sBd/3.png" alt="3" border="0" /></a>
<a href="https://ibb.co/CncX5xF"><img src="https://i.ibb.co/vJFrx28/9.png" alt="9" border="0" /></a> 
<a href="https://ibb.co/nMrVQgR"><img src="https://i.ibb.co/B2L7Tzw/11.png" alt="11" border="0" /></a> 

- *Реализация профиля пользователя.*<br/>
<a href="https://ibb.co/tXzzHJB"><img src="https://i.ibb.co/bJFF6K1/2.png" alt="2" border="0" /></a> 
<a href="https://ibb.co/pZWXVPd"><img src="https://i.ibb.co/CvJ0CtQ/4.png" alt="4" border="0" /></a> 

- *Реализация отзывов и рейтинга к товару.*<br/>
<a href="https://ibb.co/pX7BN64"><img src="https://i.ibb.co/3h39V5S/10.png" alt="10" border="0" /></a> 

- *Реализация Django Admin.*<br/>
<a href="https://ibb.co/4Td6Lgg"><img src="https://i.ibb.co/tsX76PP/7.png" alt="7" border="0" /></a>

- *Реализация API с использованием DRF.*<br/>
<a href="https://ibb.co/JzPkYLZ"><img src="https://i.ibb.co/D7nKBXd/8.png" alt="8" border="0" /></a>