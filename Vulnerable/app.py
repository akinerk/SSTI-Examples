from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
      name = request.form.get('name')
      template = f'''
      <h1>Merhaba, {name}!</h1>
      '''
      return render_template_string(template)
  return '''
  <form method="POST">
      <input type="text" name="name">
      <input type="submit" value="Submit">
  </form>
  '''

if __name__ == '__main__':
  app.run(debug=True)