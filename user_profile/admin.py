from django.contrib import admin


from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'course', 'mobile', 'gender']
    search_fields = ['name__username', 'faculty', 'course']
    show_full_result_count = True
    empty_value_display = '-empty-'


admin.site.register(Profile, ProfileAdmin)
