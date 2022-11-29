from flask import Flask
import routes

UPLOAD_FOLDER = '/tmp/'

app = Flask(__name__)
#app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.add_url_rule('/ocr/help',methods = ['GET'], view_func=routes.help)
app.add_url_rule('/ocr/aadhar', methods=['POST'], view_func=routes.aadhar)
app.add_url_rule('/ocr/pan', methods=['POST'], view_func=routes.pan)
app.add_url_rule('/ocr/dlic', methods=['POST'], view_func=routes.dlic)

if __name__ == '__main__':
	app.run(debug=True)