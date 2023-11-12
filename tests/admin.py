from django.contrib import admin
from django import forms

from .models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

    answers = forms.CharField(widget=forms.Textarea, help_text="Enter answers as a comma-separated list.")


class TestAdmin(admin.ModelAdmin):
    form = TestForm
    list_display = ('question', 'correct_answer')
    search_fields = ['question', 'correct_answer']


admin.site.register(Test, TestAdmin)
