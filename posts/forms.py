from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    title = StringField('Заголовок')
    body = TextAreaField('Текст')
    tags = StringField('Теги')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if self.tags.data:
            data = []
            for i in self.tags.data:
                data.append(str(i))
            self.tags.data = ', '.join(data)