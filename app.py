from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1, story2

app = Flask(__name__)
app.config['SECRET_KEY'] = "shh it's a secret"
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return render_template("home.html")
    
    

@app.route('/prompts')
def prompts():
    selected_story=request.args.get("story_selection")

    if selected_story == "story1":
        prompts = story1.prompts

    elif selected_story == "story2":
        prompts = story2.prompts

    else:
        return "Please select a story"
    

    return render_template("prompts.html", prompts=prompts, story=selected_story)
        


@app.route('/story')
def show_story():
    selected_story=request.args.get("story_selection")
    if selected_story == "story1":
        selected_story = story1

    elif selected_story == "story2":
        selected_story = story2

        
    answers={prompt:request.args.get(prompt) for prompt in selected_story.prompts} 
    story_text = selected_story.generate(answers)
    return render_template("story.html", template=story_text)