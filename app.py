from flask import *
app = Flask(__name__)
import mlab
from mongoengine import *

mlab.connect()

class NLHStore(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    masp = StringField()
    sizes = StringField()
    price = IntField()


# shoes = NLHStore(name="TUBULAR DOOM SOCK PRIMEKNIT SHOES", image="http://demandware.edgesuite.net/sits_pod20-adidas/dw/image/v2/aaqx_prd/on/demandware.static/-/Sites-adidas-products/en_US/dwc1ccf83c/zoom/BY3564_01_standard.jpg?sw=500&sfrm=jpg",
#                                                            description="Color Grey / Core Black / Running White",
#                                                            masp="Mã sản phẩm: BY3564",
#                                                            price=120,
#                                                            sizes="Sizes: 39/40/41/42/43")
# shoes.save()
#
#
#
#
# sh = [
#     {
#         "name": "TUBULAR DOOM SOCK PRIMEKNIT SHOES",
#         "masp": "Mã sản phẩm: BY3564",
#         "description": "Color Grey / Core Black / Running White",
#         "sizes": "Sizes: 39/40/41/42/43",
#         "price": 120,
#         "image": "http://demandware.edgesuite.net/sits_pod20-adidas/dw/image/v2/aaqx_prd/on/demandware.static/-/Sites-adidas-products/en_US/dwc1ccf83c/zoom/BY3564_01_standard.jpg?sw=500&sfrm=jpg"
#     },
#     {
#         "name": "TUBULAR SHADOW OXIDIZED SHOES",
#         "masp": "Mã sản phẩm: BY3539",
#         "description": "Color Collegiate Navy / Collegiate Navy / Collegiate Navy",
#         "sizes": "Sizes: 39/40/41",
#         "price": 70,
#         "image": "http://demandware.edgesuite.net/sits_pod20-adidas/dw/image/v2/aaqx_prd/on/demandware.static/-/Sites-adidas-products/en_US/dw5d37f82d/zoom/BY3539_01_standard.jpg?sw=500&sfrm=jpg"
#     },
#     {
#         "name": "TUBULAR INSTINCT BOOST SHOES",
#         "masp": "Mã sản phẩm: BY3611",
#         "description": "Color Core Black / Running White / Antique Silver",
#         "sizes": "Sizes: 40/41/42/43/44",
#         "price": 150,
#         "image": "http://demandware.edgesuite.net/sits_pod20-adidas/dw/image/v2/aaqx_prd/on/demandware.static/-/Sites-adidas-products/en_US/dw6553dc35/zoom/BY3611_01_standard.jpg?sw=500&sfrm=jpg"
#     }
#
#
# ]

@app.route('/')
def index():
    return render_template('index.html', listshoes=NLHStore.objects())

if __name__ == '__main__':
  app.run(debug=True)
