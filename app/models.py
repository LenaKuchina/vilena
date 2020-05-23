from app import db
from datetime import datetime
import re


def slugify(s):
    pattern = r'[^\w+]' # выделит ненужные нам знаки
    return re.sub(pattern, '-', s)#заменяем все на -

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(140), unique = True)
    body = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self): # осмысленный вид
        return '<Post id: {}, title: {}>', format(self.id, self.title)