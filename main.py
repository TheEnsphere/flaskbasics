

from flask import Flask, request, render_template
#Explaining Imports: Flask - Html support | requests - used to take text area | render_template - opening html files |

app = Flask(__name__)
#===Dummy Data===#
output = ''




@app.route('/') #creates a new webpage
@app.route('/home') #stacked so multiurl links to same place
def home():
  return render_template('home.html') #render_templates renders html file in /templates

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}'.format(request.form['text'])





if __name__ == '__main__':
  app.run(host='0.0.0.0', port = 8080)

#debug mode does not work with repl.it
  
