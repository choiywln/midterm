from flask import Flask, render_template, redirect, request
from forms import SignUpForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'web programming is hard'


@app.route('/')
def board():
    form = SignUpForm()
    return render_template('board_page.html', form=form)


@app.route('/post')
def post_page():
    form = SignUpForm()
    return render_template('post_page.html', form=form)


@app.route('/author')
def author_page():
    form = SignUpForm()
    return render_template('author_page.html', form=form)


@app.route('/writing', methods=['GET', 'POST'])
def writing_page():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('board_page.html', result=result)
    return render_template('writing_page.html', form=form)


@app.errorhandler(404)
def page_not_found():
    return render_template('404_error_page.html'), 404


if __name__ == '__main__':
    app.run()
