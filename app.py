from flask import *
app = Flask(__name__)
import mlab
from mongoengine import *

mlab.connect()

class NLHStore(Document):
    name = StringField()
    image = StringField()
    masp = StringField()
    price = IntField()

for shoes  in NLHStore.objects():
    print(shoes.name)
    print(shoes.image)


@app.route('/')
def index():
    return render_template('index.html', shoeslist=NLHStore.objects())

@app.route("/admin")
def admin():
    return render_template("admin.html", shoeslist=NLHStore.objects())

@app.route("/deleteshoes/<shoes_id>")
def deleteshoes(shoes_id):
    shoes = NLHStore.objects().with_id(shoes_id)
    if shoes is not None:
        shoes.delete()
    return redirect("/admin")

if __name__ == '__main__':
  app.run(debug=True)
