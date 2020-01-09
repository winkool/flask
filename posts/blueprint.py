from flask import Blueprint, render_template, request, redirect, url_for
from models import Post, Tag
from .forms import PostForm
from app import db


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q)
                                  | Post.body.contains(q)).order_by(Post.created.desc()).all()
    else:
        posts = Post.query.order_by(Post.created.desc()).all()

    return render_template('posts/index.html', posts=posts)
    # reqTemp = {}
    # for post in posts:
    #     reqTemp[post.id]={'title': post.title, 'content': post.body, 'datetime': str(post.created)}
    # return json.dumps(reqTemp, ensure_ascii=False)


@posts.route('/<slug>')
def postBySlug(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/index.html', posts=posts, tag=tag)
