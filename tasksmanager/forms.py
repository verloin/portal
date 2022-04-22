from django import forms
from tasksmanager.models import Task, Comment



class ChangeTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']
        widgets = {
            # 'deadline': forms.DateTimeInput(attrs={'disabled': True}),
            'status': forms.Select(attrs={'onchange': 'enableDeadlineField(this.selectedIndex);'})
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2})
        }

    def save(self, commit=True):
        self.instance.creator = self.initial['creator']
        self.instance.task = self.initial['task']
        return super().save(commit)