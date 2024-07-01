from app import app
from utils.probe_plugins import get_plugins
import json

if __name__ == "__main__":
    app.config['plugins'] = json.loads(get_plugins())
    app.run(host='0.0.0.0', port=5000)