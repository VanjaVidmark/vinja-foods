from app import app, db
from flask import request, jsonify
from models import Recipe

@app.route("/api/recipies", methods=["GET"])
def get_recipies():
    recipies = Recipe.query.all()
    result = [recipe.to_json() for recipe in recipies]
    return jsonify(result)

@app.route("/api/recipies", methods=["POST"])
def create_recipe():
    try:
        data = request.json
        name = data.get("name")
        description = data.get("description")
        img_url = f"https://zaitoune.com.au/wp-content/uploads/2018/06/6-Lebanese-Food-Facts-You-Might-Not-Know.jpg"
        
        new_recipe = Recipe(name=name, description=description, img_url=img_url)
        db.session.add(new_recipe)

        db.session.commit()

        return jsonify({"msg": "Recipe created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": str(e)}), 500