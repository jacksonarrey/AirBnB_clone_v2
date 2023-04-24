#!/usr/bin/python3
""""""
from Flask import Flask
app = Flask(__name__)
@app.router('/'. strict_slashes=False
def hello():
    """"""
         return 'Hello HBNB'
@app.router('/hbnb'. strict_slashes=False
    def hbnb():
    """"""
	return 'HBNB'
                 
@app.router('/c/<text>'. strict_slashes=False
    def c(text):
    """"""
        return 'c {}'.format(text.replace('_', ' ')) 
        @app.router('/python/(<text>)'. strict_slashes=False
@app.router('/python/(<text>)'. strict_slashes=False
    def python(text='is cool'):
    """"""
        return 'python {}'.format(text.replace('_', ' '))
if __name__ == "__main__:
app.run(host='0.0.0.0' port=5000

