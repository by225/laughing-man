from flask import Blueprint

# Create a Blueprint instead of using a direct app reference
main_blueprint = Blueprint('main', __name__)

mbp = main_blueprint

from datetime import datetime
from flask import make_response

current_time = datetime.now()
mysql_formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

def create_response(data, status=200, mimetype='text/html'):
    data += '<br>\n'
    data += mysql_formatted_time
    response = make_response(data, status)
    response.mimetype = mimetype
    return response

@mbp.route('/')
def home():
    return create_response('Hello world!')

@mbp.route('/hello')
def hello_world():
    return create_response('Hello, World!')
