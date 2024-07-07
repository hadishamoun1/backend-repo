import yaml
import os

config_file = os.path.join(os.path.dirname(__file__), 'C:/Users/shamo/Desktop/projects/fullstack-repo/config.yaml')

with open(config_file, 'r') as f:
    config = yaml.safe_load(f)

server_ip = config.get('ip_address')

print(f"the server connected at IP address: {server_ip}")