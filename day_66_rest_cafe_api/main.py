from flask import Flask, jsonify, render_template, request, Request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.get("/random")
def random():
    with app.app_context():
        cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()
        return jsonify(cafe.to_dict())

@app.get("/all")
def get_all():
    with app.app_context():
        all_cafes = db.session.execute(db.select(Cafe)).scalars()
        return [cafe.to_dict() for cafe in all_cafes]

@app.get("/search")
def search():
    location = request.args.get("location")
    if not location:
        return jsonify({"error": {"missing parameter": "Missing parameter 'location' "}}), 422
    with app.app_context():
        all_cafes = db.session.execute(db.select(Cafe).where(Cafe.location.like(f"%{location}%"))).scalars().all()
        print(all_cafes)
        if not all_cafes:
            return jsonify({"error": {"Not found": "No cafes found in your area"}}), 404
        return [cafe.to_dict() for cafe in all_cafes]

@app.post("/add")
def add_cafe():
    with app.app_context():
        req_json:dict = request.json
        cafe = Cafe()
        for key in req_json.keys():
            cafe.__setattr__(key, req_json[key])
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={"success": "New cafe added"})

@app.patch("/update-price")
def update_price():
    cafe_id = request.args.get("id")
    req_json = request.json
    print(cafe_id)
    if not cafe_id:
        return jsonify(error={"Missing parameter": "Missing 'id'"}), 422
    if not req_json:
        return jsonify(error={"Missing body": "No 'new_price' provided"}), 422
    with app.app_context():
        cafe = db.get_or_404(entity=Cafe, ident=cafe_id, description="No cafe found")
        cafe.coffee_price = req_json["new_price"]
        db.session.commit()
        return jsonify(response={"success": "Price edited"})

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
