from django.contrib import admin
from django.utils.safestring import mark_safe
from review_app.models import Review, MediaReview


# Register your models here.


class MediaReviewAdmin(admin.StackedInline):
    """Вывод изображений постов в админке"""
    model = MediaReview
    list_display = ('image_review','preview')
    readonly_fields = ('image_review','preview')
    extra = 1


    def preview(self, obj):
        """Превью при нажатии на картинку"""
        if obj.image_review:
            return mark_safe(
                f'<a target=_blank href={obj.image_review.url}>'
                f'<img src={obj.image_review.url} width="100" height="100">'
                f'</a>'
            )
        else:
            return 'No Image'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    inlines = (
        MediaReviewAdmin,
    )
    list_display = ('text', 'user', 'post', 'created_at',)
    list_display_links = ('text', 'user',)
    list_filter = ('user', 'post', 'created_at',)
    search_fields = ('user', 'text', 'post')
    list_editable = ('post',)
    save_on_top = True