from flask import Flask, render_template, request, json
app = Flask(__name__)
 

@app.route('/')
def index():
    return render_template('index.html')
 
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()