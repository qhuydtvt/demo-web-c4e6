from flask import *
from mongoengine import *


app = Flask(__name__)

class Movie(Document):
    title = StringField()
    desc = StringField()
    img_link = StringField()
    rate = FloatField()

TEST_IMG_LINK = "https://image.tmdb.org/t/p/w300_and_h450_bestv2/5JU9ytZJyR3zmClGmVm9q4Geqbd.jpg"
TEST_IMG_LINK2 = "https://image.tmdb.org/t/p/w300_and_h450_bestv2/dCgm7efXDmiABSdWDHBDBx2jwmn.jpg"

movie1 = Movie(title = "Terminator", desc = "Haha", img_link = TEST_IMG_LINK)
movie2 = Movie(title = "Fast & furious", desc = "Hihi", img_link = TEST_IMG_LINK2)

@app.route('/')
def index():
    return render_template("index.html", movies = [movie1, movie2])


if __name__ == '__main__':
    app.run()
