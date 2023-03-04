from django.contrib import admin
from django.utils.safestring import mark_safe

from webapp.models import Company, Scope, Office, Profile, Position, Language


class OfficeInline(admin.StackedInline):
    model = Office

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(company_id=self.extra)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    filter_horizontal = ('partner',)
    inlines = [OfficeInline]
    fields = ('name', 'logo', 'preview', 'scope', 'country', 'is_active', 'partner',)
    readonly_fields = ('preview',)
    list_display = ('id', 'name', 'logo_tag', 'is_active',)
    list_display_links = ('name',)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-height: 150px;">')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('user', 'is_active')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('address', 'birthdate'),
        }),
    )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'is_remote', 'name', 'salary', 'company', 'employee')
    list_editable = ('is_remote', 'salary',)
    actions = ['make_published']

    @admin.action(description='Сделать выбранные позиции удаленными')
    def make_published(modeladmin, request, queryset):
        queryset.update(is_remote=True)


admin.site.register(Language)
admin.site.register(Scope)
admin.site.register(Office)