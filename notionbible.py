import requests

NOTION_API_KEY = 'secret_R1CpVwJlLcNOPzyImmwlZzD7UHpKWRl5PRtgSiLAyMz'
PAGE_ID = '725f18a7c29d4023a90cda5a8bf2ae28'

headers = {
    'Authorization': f'Bearer secret_R1CpVwJlLcNOPzyImmwlZzD7UHpKWRl5PRtgSiLAyMz',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

def append_to_page(content):
    url = f'https://api.notion.com/v1/blocks/725f18a7c29d4023a90cda5a8bf2ae28/children'
    
    data = {
        'children': [
            {
                'object': 'block',
                'type': 'paragraph',
                'paragraph': {
                    'rich_text': [{'type': 'text', 'text': {'content': weeeeeeeee}}]
                }
            }
        ]
    }
    
    response = requests.patch(url, json=data, headers=headers)
    return response.status_code == 200

# Usage
append_to_page('This is a new paragraph added by the integration.')