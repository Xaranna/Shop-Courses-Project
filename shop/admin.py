from django.contrib import admin
from .models import Course, Category, Cart

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcome to the Courses admin area"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    search_fields = ('title',)
    ordering = ('title',)


class CoursesInline(admin.TabularInline):
    model = Course
    extra = 1
    exclude = ['created_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]
    search_fields = ('title',)


class CartAdmin(admin.TabularInline):
    model = Cart
    fields = ('course', 'quantity', 'created_at')
    extra = 0
    readonly_fields = ('created_at',)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)