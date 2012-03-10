from shorty.utils import url_encode

__author__ = 'ogonbat'

#admin section
class UrlAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('url_field','show_slug','user','status','created')
    list_display_links = ('url_field',)
    #list_editable = ('url_field',)
    list_filter = ('status',)
    search_fields = ('url_field','status')
    fieldsets = (
        ('General',{
            'fields':('url_field','user','status')
        }),
        ('Advanced options',{
            'classes': ('collapse',),
            'fields':('private','private_password')
        })
        )
    actions = ['ban_this_link']

    #actions
    def ban_this_link(self,request,queryset):
        queryset.update(status='b')
    ban_this_link.short_description = 'Ban selected links'


    #property
    def show_slug(self,obj):
        return url_encode(obj.id)
    show_slug.short_description = "Slug"

class PrivateSlugAdmin(admin.ModelAdmin):
    pass