from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/',methods=["GET"])
def hello():
    return render_template('index.html')

@app.route('/myMethod/',methods=["POST"])
def myMethod():
    num1=int(request.form['nm1'])
    num2=int(request.form['nm2'])

    return render_template('index3.html',Sumvalue=str(num1+num2))


@app.route('/Params/',methods=["GET","POST"])
def Params():
    if request.method=="GET":
        return render_template('index1.html')
    else:
        username = request.form.get('username')
        print(username)
        password= request.form.get('password')
        print(password)
        return render_template('index3.html',Sumvalue=username)

if __name__ == '__main__':
    app.run()