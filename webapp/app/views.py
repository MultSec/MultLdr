from flask import render_template, send_file, request, jsonify
from app import app, Log
import os
import shutil
from threading import Thread
from utils.ldr_generation import generateLdr

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
    Log.info(f"[{id}] Saving payload")

    # Check if 'payload' file is in the request
    if 'payload' not in request.files:
        Log.error("No payload file part in the request")
        return jsonify({"error": "No payload file part"}), 400

    # Get the file from the request
    file = request.files['payload']

    # Make directory
    Log.info(f"[{id}] Generating temp dir")
    os.makedirs(f'./uploads/{id}')
    
    # Save the file to the uploads folder as payload
    file.save(f'./uploads/{id}/payload')

    # Return the success message
    return jsonify({"message": "File uploaded successfully"})

# Generate loader with payload for a given id
@app.route('/api/v1/payload/generate/<id>', methods=['POST'])
def generate(id):
    Log.info(f"[{id}] Generating loader")

    # Get JSON data from the request
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    
    # Read and print all key-value pairs
    plugins = data.items()

    # Check if every plugin is present
    Log.info(f"[{id}] Checking Loader Config")
    for key, elements in plugins:
        for element in elements:
            if not os.path.exists("./plugins" + element + "/run.py"):
                Log.error(f"[{id}] Plugin not found: {element}")

                # Remove directory
                Log.info(f"[{id}] Removing temp dir")
                shutil.rmtree(f'./uploads/{id}')

                return jsonify({"error": f"Plugin not found: {element}"}), 500

    # Start worker thread
    thread = Thread(target=generateLdr, args=(id, plugins, ))
    thread.daemon = True
    thread.start()

    return jsonify({"message": "Loader generation started successfully"})

# Generate loader with payload for a given id
@app.route('/api/v1/payload/status/<id>', methods=['GET'])
def getStatus(id):
    filename = f'./uploads/{id}/status'

    try:
        with open(filename, 'r') as file:
            # Check if its contents is the word "Finished"
            contents = file.read().strip()
            if contents == "Finished":
                return jsonify({"status": "Finished"}), 200
            else:
                return jsonify({"status": "Not Finished"}), 200

    except FileNotFoundError:
        return jsonify({"error": "Error wrong client id"}), 500

# Generate loader with payload for a given id
@app.route('/api/v1/payload/result/<id>', methods=['GET'])
def getResult(id):
    file_path = os.path.abspath(f'./uploads/{id}/result')

    # Check if the file exists
    if os.path.exists(file_path):
        # Send the file to the client
        result = send_file(file_path, as_attachment=True)
    else:
        result = jsonify({"error": "File not found"}), 404

    # Remove directory
    Log.info(f"[{id}] Removing temp dir")
    shutil.rmtree(f'./uploads/{id}')

    return result

# Route for errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
