from flask import Flask, render_template, request, jsonify
from agent import BrowserAgent
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
browser_agent = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_prompt():
    prompt = request.json.get('prompt')
    try:
        global browser_agent
        if browser_agent is None:
            browser_agent = BrowserAgent()
        
        result = browser_agent.execute_prompt(prompt)
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        logging.error(f"Error executing prompt: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)