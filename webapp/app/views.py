from flask import render_template, request, redirect
from app import app
import importlib
from utils.ldr_generation import generate_loader

# favicon.ico route
@app.route('/favicon.ico')
def favicon():
    # Return the favicon
    return send_file('./static/MultLdr.ico', mimetype='image/vnd.microsoft.icon')

# Define the route that will serve the loader configuration
@app.route('/', methods=['GET'])
def serve_conf():
    return render_template('index.html', importlib = importlib, plugins = app.config['plugins'])

# Define the route that will generate the loader
@app.route('/', methods=['POST'])
def gen_ldr():
    # Check if the payload file was uploaded
    if 'payload' not in request.files:
        return redirect(request.url)
    payload = request.files['payload']
    
    # Get the chosen configurations from the form
    conf = request.form
    
    # Generate a json with the chosen configurations
    config = {
        "placement": conf['placement'],
        "encryption": conf['encryption'],
        "compression": conf['compression'],
        "obfuscation": conf['obfuscation'],
        "metadata" : {
            "binaryName": conf['binaryName'],
            "companyName": conf['companyName'],
            "fileDescription": conf['fileDescription'],
            "internalName": conf['internalName'],
            "legalCopy": conf['legalCopy'],
            "originalFilename": conf['originalFilename'],
            "productName": conf['productName'],
            "productVersion": conf['productVersion']
        }
    }

    # Get icon if it was uploaded
    if 'icon' in request.files:
        icon = request.files['icon']
        config['icon'] = icon
    else:
        config['icon'] = None

    # Generate the loader
    generate_loader(config, icon, payload)

    # redirect to index
    return redirect(request.url)

    

# Route for errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404