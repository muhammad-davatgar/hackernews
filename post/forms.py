from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(label="title", max_length=20, required=True,
                            widget=forms.TextInput())
    text = forms.CharField(label="text", max_length=300, required=True,
                           widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'title'
        self.fields['title'].label = 'title'
        self.fields['title'].help_text = 'Required. 300 characters or fewer.'

        self.fields['text'].widget.attrs['placeholder'] = 'text'
        self.fields['text'].label = 'text'
        self.fields['text'].help_text = 'body of the Post.'


# Create Add Record Form
# class AddRecordForm(forms.ModelForm):
# 	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
# 	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
# 	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
# 	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
# 	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
# 	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
# 	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
# 	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

# 	class Meta:
# 		model = Post
# 		exclude = ("user",)


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        required=True, widget=forms.widgets.Textarea, max_length=300)
    reply = forms.IntegerField(required=False, min_value=0)

    class Meta:
        model = Comment
        fields = ['text', 'reply']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'text'
        self.fields['text'].label = 'text'
        self.fields['text'].help_text = 'body of Comment'

        self.fields['reply'].widget.attrs['placeholder'] = 'reply'
        self.fields['reply'].label = 'reply'
        self.fields['reply'].help_text = 'replying to'
