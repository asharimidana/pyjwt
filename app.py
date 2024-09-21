#Project Flask MVC

__author__ = "asharimidana"
__version__ = "1"
__email__ = "ashari@gmail.com"

from app import app

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
