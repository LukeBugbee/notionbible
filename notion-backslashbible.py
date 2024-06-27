from flask import Flask, request, jsonify
from your_notion_script import add_item_to_database, get_database_items

app = Flask(__name__)

@app.route('/slash-command', methods=['POST'])
def handle_slash_command():
    command = request.form.get('command')
    text = request.form.get('text')

    if command == '/add-task':
        task_id = add_item_to_database(text)
        return jsonify({'response_type': 'in_channel', 'text': f'Task added with ID: {task_id}'})
    elif command == '/search-tasks':
        items = get_database_items(text)
        response = 'Found tasks:\n' + '\n'.join([item['properties']['Name']['title'][0]['text']['content'] for item in items])
        return jsonify({'response_type': 'in_channel', 'text': response})
    else:
        return jsonify({'response_type': 'ephemeral', 'text': 'Unknown command'})

if __name__ == '__main__':
    app.run(port=3000)