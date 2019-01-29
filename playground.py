from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def typeplay():
    return "Type 'play' in the address line for a surprise"

@app.route('/play')
def play():
    return render_template("pindex.html", num = 3)


@app.route('/play/<n>')
def play2(n):
    return render_template("pindex.html", num = int(n))


@app.route('/play/<n>/<c>')
def play3(n, c):
    return render_template("pindex.html", num = int(n), color = c)


if __name__=="__main__":
    app.run(debug = True)