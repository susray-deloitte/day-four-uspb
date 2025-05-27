from flask import Blueprint, request, jsonify, render_template
from .openai_api import get_chatbot_response

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/', methods=['GET'])
def index():
    print("Index route called")
    return render_template('index.html')

@chatbot_bp.route('/chatbot', methods=['POST'])
def chatbot_api():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'No question provided'}), 400
    response = get_chatbot_response(data['question'])
    return jsonify({'response': response})