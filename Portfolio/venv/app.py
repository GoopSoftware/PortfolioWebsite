from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/adman')
def adman():
    return render_template(
    'macros.html',
    video_filename = 'videos/A-D man.mp4',
    title = 'A-D Man',
    description = ('A-D Man was my opportunity to challenge myself and put into practice '
                   'everything I had learned up until that point. The idea behind the game '
                   'is souls-like, two button controls, and pursuit. The game features a '
                   ' game speed mechanic that increases or decreases according to player '
                   'ability. The game was built using an object-oriented design structure.'),
    github_url = 'https://github.com/GoopSoftware/ADMan',
    skills = ["Object-Oriented Programming", "Pointers/References", "Vectors",
              "Adaptive Gameplay"]
    )



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)