from django.contrib import admin

# Register your models here.


class ThemeAdmin(admin.ModelAdmin):
    list_display = 'Theme'
    search_fields = 'Theme'
    list_editable = 'Theme'


class NewsAdmin(admin.ModelAdmin):
    list_display = ("name",
                    'description',
                    'date_of_creation',
                    'date_of_update',
                    'status',
                    ' theme',
                    'image',
                    )
    search_fields = ("name",
                     'description',
                     'date_of_creation',
                     'date_of_update',
                     'status',
                     ' theme',
                     'image',
                     )
    list_editable = ("name",
                     'description',
                     'date_of_creation',
                     'date_of_update',
                     'status',
                     ' theme',
                     'image',
                     )
    list_filter = ('name', 'theme', 'status')