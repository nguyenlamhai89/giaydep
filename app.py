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

if __name__ == '__main__':
  app.run(debug=True)
