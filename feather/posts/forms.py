from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('headliner', 'text', 'group', 'image')
        labels = {
            'headliner': 'Заголовок',
            'text': 'Текст',
            'group': 'Группа',
        }
        exclude = ('date', 'author')

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('Вы должны что-то написать, и не забудьте про заголовок')
        if len(data) > 1150:
            raise forms.ValidationError('Максимальная длина текста - 1150 символов')
        return data

    def clean_headliner(self):
        data = self.cleaned_data['headliner']
        if data == '':
            raise forms.ValidationError('Необходимо дать посту заголовок')
        if len(data) > 70:
            raise forms.ValidationError('Максимальная длина заголовка - 70 символов')
        return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Текст',
        }
        exclude = ('date', 'author', 'post', 'answer_to',)

    def clean_subject(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('Вы должны что-то написать')
        return data
