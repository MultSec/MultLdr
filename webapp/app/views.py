from flask import render_template, send_file
from app import app, Log

# favicon.ico route
@app.route('/favicon.ico')
def favicon():
    # Return the favicon
    return send_file('./static/MultLdr.ico', mimetype='image/vnd.microsoft.icon')

# Get enabled plugins
@app.route('/api/v1/plugins', methods=['GET'])
def plugins():
    return app.config['plugins']

# Upload raw payload for a given id
@app.route('/api/v1/payload/upload/<id>', methods=['POST'])
def upload(id):
    print(id)
    Log.info( "Saving payload from client: " + id)
    
    # Get the file from the request
    file = request.files['payload']

    # Save the file to the uploads folder as payload
    file.save('./uploads/payload')

    # Return the success message
    return jsonify({"message": "File uploaded successfully"})

# Generate loader with payload for a given id
@app.route('/api/v1/payload/generate/<id>', methods=['POST'])
def generate(id):

    return id

# Route for errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404