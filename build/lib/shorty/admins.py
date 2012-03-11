from shorty.utils import url_encode
from django.contrib import admin

__author__ = 'ogonbat'

#admin section
class UrlAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('url_field','show_slug','user','status','is_protected','created')
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
    actions = ['ban_this_link','active_this_link','refuse_this_link','pending_this_link']

    #actions
    def ban_this_link(self,request,queryset):
        queryset.update(status='Banned')
    ban_this_link.short_description = 'Ban selected links'
    
    #actions
    def active_this_link(self,request,queryset):
        queryset.update(status='Active')
    active_this_link.short_description = 'Active selected links'
    
    #actions
    def refuse_this_link(self,request,queryset):
        queryset.update(status='Refused')
    refuse_this_link.short_description = 'Refuse selected links'

    #actions
    def pending_this_link(self,request,queryset):
        queryset.update(status='Pending')
    pending_this_link.short_description = 'Move selected links to Pending'
    
    #property
    def show_slug(self,obj):
        if obj.personal:
            #the link have a personal slug
            return obj.personal_slug
        else:
            return url_encode(obj.id)
    show_slug.short_description = "Slug"
    
    #property
    def is_protected(self,obj):
        if obj.private:
            #the link have a personal slug
            return "yes"
        else:
            return "no"
    is_protected.short_description = "Is Protected"