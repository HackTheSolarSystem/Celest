from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sun')
def sun():
    start_datetime = datetime.datetime(*request.args.get('start_date'), *request.args.get('start_time'))
    end_datetime = datetime.datetime(*request.args.get('end_date'), *request.args.get('end_time'))
    resolution = request.args.get('resolution')
    wavelength = request.args.get('wavelength')

    return 'Something was done here.'

if __name__ == '__main__':
    app.run()