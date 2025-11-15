from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/topics')
def topics():
    project_topics = [
    {"title": "Solar Energy", "desc": "Learn how solar panels convert sunlight into electricity."},
{"title": "Water Purification", "desc": "Understand simple methods to purify water for science projects."},
{"title": "Artificial Intelligence", "desc": "Explore how AI is transforming the modern world."},
{"title": "Environmental Pollution", "desc": "Study the effects of pollution and how to reduce it."},
{"title": "Computer Networks", "desc": "Basics of how computers communicate over networks."}
]
    return render_template('topics.html', topics=project_topics)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)
