from flask import Flask
from api import api as api_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/aweme/v1/web')

CORS(app, origins='*', supports_credentials=True)  # 解决跨域问题


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3010)
