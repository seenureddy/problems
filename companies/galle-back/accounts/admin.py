from django.contrib import admin

from accounts.models import Article, Category


class CategoryAdminInline(admin.TabularInline):
    model = Category
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ("title", "body", "author", )
    raw_id_fields = ("author", )
    inlines = [CategoryAdminInline, ]

    fieldsets = (
        ("Author Name", {
            'classes': ('wide', 'extrapretty',),
            'fields': ('author',)
        }),
        ("Article Title And Body", {
            'classes': ('wide', 'extrapretty',),
            'fields': (
                'title', 'body', 'posted_on'
            )
        }),
        ("Images", {
            'fields': (
                ("image", "optinal_image", ), 
            )

        }),
    )
