from flask import Flask
import time
import os
# http://localhost:6738

CURRENT_TIME = int(time.time())
app = Flask(__name__)

@app.route('/')
def get_unix_time():
    """get unix time"""

    #unix_time = CURRENT_TIME
    #return str(unix_time)
    return('Hello World')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
