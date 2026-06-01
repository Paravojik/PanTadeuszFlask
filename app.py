from flask import Flask, render_template,abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/k1')
# def k1():
#     return render_template('k1.html')



# @app.route('/k1')
# def k1():
#     return render_template('k1.html')
# @app.route('/k2')
# def k2():
#     return render_template('k2.html')
# @app.route('/k3')
# def k3():
#     return render_template('k3.html')


@app.route('/k<int:book_id>')
def show_book(book_id):
    if book_id < 1 or book_id > 12:
        abort(404) 
        
    return render_template(f'k{book_id}.html',book_id=book_id)

if __name__=="__main__":
    app.run()