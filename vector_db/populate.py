# Script to populate vector DB with initial project context
import os
from vector_db import add_item

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

files_to_index = [
    ('docs', 'global_rules', os.path.join(PROJECT_ROOT, '.codeium', 'windsurf', 'memories', 'global_rules.md')),
    ('docs', 'mcp_config', os.path.join(PROJECT_ROOT, '.codeium', 'windsurf', 'mcp_config.json')),
]

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def populate():
    for collection, item_id, path in files_to_index:
        if os.path.exists(path):
            content = read_file(path)
            add_item(collection, item_id, content)
            print(f'Indexed {item_id} into {collection}')
        else:
            print(f'File not found: {path}')

if __name__ == '__main__':
    populate()
