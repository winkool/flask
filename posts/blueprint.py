from flask import Blueprint
from flask import render_template
from models import Post,Tag
import json

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    posts = Post.query.all()
    # reqTemp = {}
    # for post in posts:
    #     reqTemp[post.id]={'title': post.title, 'content': post.body, 'datetime': str(post.created)}
    # return json.dumps(reqTemp, ensure_ascii=False)
    return render_template('posts/index.html', posts=posts)


@posts.route('<slug>')
def postBySlug(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/index.html', posts=posts, tag=tag)