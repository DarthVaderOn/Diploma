from django.views import View
from catalog_app.forms.catalog import AddImagePost
from django.shortcuts import render, redirect
from catalog_app.models import Media


class PostCreate(View):
    """Класс создания постов"""

    def get(self, request):
        """Представление формы"""

        form = AddImagePost()
        return render(request, 'create_ad.html', context={
            'title': 'Sell Goods',
            'form': form
        })


    def post(self,request):
        """Сохранение формы"""

        bound_form = AddImagePost(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        if len(files) > 5:
            return render(request, 'create_ad.html', context={
                'title': 'Sell Goods',
                'form': bound_form,
                'error': 'Image upload error: Allowed upload limit is no more than 5 files!'
            })

        if bound_form.is_valid():
            post_object = bound_form.save(commit=False)
            post_object.user = request.user
            post_object.save()
            for f in files:
                Media.objects.create(post=post_object,image_post=f)
            return redirect('catalog_page')
        return render(request, 'main_page.html', context={
            'title': 'Sell Goods',
            'form': bound_form
        })