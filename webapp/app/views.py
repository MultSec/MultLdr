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
    Log.info("Saving payload from client: " + id)

    # Check if 'payload' file is in the request
    if 'payload' not in request.files:
        Log.error("No payload file part in the request")
        return jsonify({"error": "No payload file part"}), 400

    # Get the file from the request
    file = request.files['payload']

    # Make directory
    Log.info("generating temp dir for client: " + id)
    os.makedirs(f'./uploads/{id}')
    
    # Save the file to the uploads folder as payload
    file.save(f'./uploads/{id}/payload')

    # Return the success message
    return jsonify({"message": "File uploaded successfully"})

# Generate loader with payload for a given id
@app.route('/api/v1/payload/generate/<id>', methods=['POST'])
def generate(id):
    Log.info("Generating loader for client: " + id)

    # Get JSON data from the request
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No JSON data received"}), 400
    
    # Process the JSON data
    try:        
        # Read and print all key-value pairs
        plugins = data.items()

        Log.success(f"Config used for id: {id}")
        for key, elements in plugins:
            Log.section(key)
            for element in elements:
                Log.subsection(element)

        thread = Thread(target=generateLdr, args=(id, plugins, ))
        thread.daemon = True
        thread.start()
    
    except Exception as e:
        # Remove directory
        Log.info("Removing temp dir for client: " + id)
        shutil.rmtree(f'./uploads/{id}')

        return jsonify({"error": f"Error processing JSON data: {str(e)}"}), 500

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
def getStatus(id):
    file_path = f'./uploads/{id}/result'

    # Send the file to the client
    response = send_file(file_path, as_attachment=True)

    # Remove directory
    Log.info("Removing temp dir for client: " + id)
    shutil.rmtree(f'./uploads/{id}')

    return response

# Route for errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404