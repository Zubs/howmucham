from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
	return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/<my_name>')
def greetings(my_name):
	return "Welcome " + my_name + ",<br>I'm Zubair The Great 👑"

@app.route('/square/<int:number>')
def show_square(number):
    return "Square of " + str(number) + " is: " + str(number * number) 

if __name__== '__main__':
	app.run(debug=True)
