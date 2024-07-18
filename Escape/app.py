from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    name = ''
    if request.method == 'POST':
        name = escape(request.form.get('name', ''))
    
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Template Engine</title>
    </head>
    <body>
        <form method="POST">
            <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
        {% if name %}
        <h1>Merhaba, {{ name }}!</h1>
        {% endif %}
    </body>
    </html>
    '''
    
    return render_template_string(html_content, name=name)

if __name__ == '__main__':
    app.run(debug=True)
