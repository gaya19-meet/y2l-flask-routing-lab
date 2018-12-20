from flask import *
app = Flask(__name__)

@app.route('/')
def home_page():
	pets_list = ["cat" , "dog" , "unicorn" , "panda" , "bear"]
	return render_template("home.html" , pets=pets_list)


@app.route('/shop')
def shop_page():
    return render_template("shop.html")

if __name__ == '__main__':
   app.run(debug = True)

