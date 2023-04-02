import datetime

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")



from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def display_time():
    time = get_current_time()
    return render_template('home.html', time=time)


if __name__ == '__main__':
    application.run()
