# Flask OpenAI Chatbot

This project is a simple Flask application that integrates with the OpenAI API to create a chatbot. Users can input their questions through a web interface, and the chatbot will respond based on the provided prompts.

## Project Structure

```
day-four-uspb
├── chatbot
│   ├── __init__.py
│   ├── routes.py
│   ├── openai_api.py
│   └── templates
│       └── index.html
├── requirements.txt
├── run.py
├── .env
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd day-four-uspb
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up your OpenAI API key:**
   - Create a `.env` file in the project root with the following content:
     ```
     OPENAI_API_KEY=your-openai-api-key-here
     ```
   - Replace `your-openai-api-key-here` with your actual OpenAI API key.

## Usage

1. **Run the application:**
   ```
   python run.py
   ```

2. **Access the chatbot:**
   Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to interact with the chatbot.

## Features

- User-friendly web interface for inputting questions.
- Integration with the OpenAI API for generating responses.
- Simple and clean layout styled with CSS.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.