from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route('/')
def hello_ssti():
    person = {'name':"Tester", 'secret':"UGhldmJoZj8gYWl2ZnZoei5wYnovcG5lcnJlZg=="}
    if request.args.get('name'):
        person['name'] = request.args.get('name')
    template = '''
<h1> Hey there! </h1>
<h2> Nice to meet you %s!</h2>

''' % person['name']
    return render_template_string(template, person=person)

def get_user_file(f_name):
    with open(f_name) as f:
        return f.readlines()

app.jinja_env.globals['get_user_file'] = get_user_file 

if __name__ == "__main__":
    app.run(threaded=True)
