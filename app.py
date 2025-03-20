from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

openAIkey = os.getenv('OPENAI')

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Firebase!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
