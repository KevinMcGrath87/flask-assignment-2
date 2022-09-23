from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def checker1():
    return render_template('index.html', var1 = 8, var2 = 8)
@app.route("/<int:var1>")
def checker2(var1):
    return render_template('index.html',var1 = var1,var2= 8 )
@app.route("/<int:var1>/<int:var2>")
def checker3(var1, var2):
    return render_template('index.html',var1 = var1, var2=var2)

if __name__ == "__main__":
    app.run(debug = True)


