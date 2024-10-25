import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/sap_notas', methods=['POST'])
def receive_json():
    # Get the JSON data from the request
    data = request.get_json()

    # You can process or validate the data here if needed
    if not data:
        return jsonify({"message": "No JSON received"}), 400

    row_now = data['rowNow']
    # Return a success message
    return jsonify({"message": f"Nota {row_now} cadastrada com sucesso"}), 200

if __name__ == '__main__':
   app.run()
