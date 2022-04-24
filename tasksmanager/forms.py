from django import forms
from tasksmanager.models import Task, Comment




class ChangeTaskForm(forms.ModelForm):
    # class Meta:
    #     model = Task
    #     fields = ['status', 'title', 'author', 'executor', 'description']
    #     widgets = {
    #         'status': forms.Select(choices = Task.CHOICES),
    #    }
    pass

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'required': 'true'})
        }

    def save(self, commit=True):
        self.instance.creator = self.initial['author']
        self.instance.task = self.initial['task']

        return super().save(commit)