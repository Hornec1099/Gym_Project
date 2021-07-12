from flask import Flask , render_template

from controllers.member_controller import member_blueprint
from controllers.activity_controller import activity_blueprint
from controllers.booking_controller import booking_blueprint

app = Flask( __name__)

app.register_blueprint(member_blueprint)
app.register_blueprint(activity_blueprint)
app.register_blueprint(booking_blueprint)

@app.route('/')
def home ():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug = True)
