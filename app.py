from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

from openai_script_generator import generate_script

# Load environment variables from .env file
app = Flask(__name__)
load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Process the form data here and generate the script
        persona = request.form.get('persona', '')
        episode_theme = request.form.get('episode_theme', '')
        intro_clip = request.form.get('intro_clip', '')
        episode_num = request.form.get('episode_num', '')
        guest_name = request.form.get('guest_name', '')
        guest_intro = request.form.get('guest_intro', '')
        commercial_break = request.form.get('commercial_break', '')
        
        # Generate the script
        script = generate_script(persona, episode_theme, intro_clip, episode_num, guest_name, guest_intro, commercial_break)

        # Render the template with the generated script
        return render_template('home.html', script=script)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run()

@app.route('/result', methods=['POST'])
def result():
    data = request.get_json()

    persona = data['persona']
    episode_theme = data['episode_theme']
    intro_clip = data['intro_clip']
    episode_num = data['episode_num']
    guest_name = data['guest_name']
    guest_intro = data['guest_intro']
    commercial_break = data['commercial_break']
    
    # Generate the script
    script = generate_script( persona, episode_theme, intro_clip, episode_num, guest_name, guest_intro, commercial_break)

    return jsonify({'script': script})

if __name__ == '__main__':
    app.run(debug=True)
