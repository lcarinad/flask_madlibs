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
        return render_template("prompts.html", prompts=prompts)

    elif selected_story == "story2":
        prompts = story2.prompts
        return render_template("prompts.html", prompts=prompts)

    else:
        return "Please select a story"
    


@app.route('/story',methods=["POST"])
def show_story():

    selected_story = request.form.get("story_selection")
    print("Selected Story:", selected_story)
    if selected_story == "story1":
        story = story1

    elif selected_story == "story2":
        story = story2

    else:
        return "Invalid story selection"
        
    answers={prompt:request.form[prompt] for prompt in story.prompts} 
    story.template = story.generate(answers)
    return render_template("story.html", template=story.template)