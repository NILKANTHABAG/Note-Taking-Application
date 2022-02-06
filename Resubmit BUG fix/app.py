from flask import Flask, render_template, redirect, request, url_for
  
# Initiate flask app
app = Flask(__name__)
  
# Declare routes and methods
@app.route('/', methods =['GET', 'POST'])
def home():
    # If it is POST request the redirect
    if request.method =='POST':
        return redirect(url_for('home'))
  
    return render_template('home.html', title ='Home')
  
if __name__=='__main__':
    app.run()