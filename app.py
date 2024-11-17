import json
from flask import Flask, jsonify, request

app = Flask(__name__)

def index():
    return '''
    <!DOCTYPE html>
    <h1>endpoint</h1>
    <p>endpoint for the thanks-giving-recipe-api by webbrowser11</p>
    '''

def recipe_is_valid(recipe):
    return (
        "name" in recipe and isinstance(recipe["name"], str) and
        "ingredients" in recipe and isinstance(recipe["ingredients"], list) and
        "steps" in recipe and isinstance(recipe["steps"], list)
    )


thanksgivingrecipes = {
    "best-turkey-gravy": {
        "ingredients": ["pan drippings", "chicken or turkey stock", "unsalted butter", "flour", "thyme", "salt and pepper"],
        "steps": [
            '''strain pan drippings trough a fine mesh sieve; discard soils and reserve 2 1/2 cups pan drippings; set aside.
            melt butter in a medium saucepan over medium heat. whisk in flour and thyme until lightly browned, about 1 minute.
            gradually whisk in reserved pan drippings. bring to a boil; reduce heat and simmer, whisking constantly until thickened about 5-10 minutes stir in parsley season with salt and pepper to taste
            serve warm.'''
        ]
    }
}

@app.route('/thanksgivingrecipes', methods=['GET'])
def get_thanksgivingrecipies():
    return jsonify(thanksgivingrecipes)

@app.route("/thanksgivingrecipes", methods=['POST'])
def create_recipie():
    recipe = json.loads(request.data)

    if not recipe_is_valid(recipe):
        return jsonify({'error': 'invalid recipe properties.'}), 400
    
    recipe_name = recipe["name"].lower()
    if recipe_name in thanksgivingrecipes:
        return jsonify({'error': f'Recipe "{recipe_name}" already exists.'}), 409
    
    thanksgivingrecipes[recipe_name] = {
        "ingredients": recipe["ingredients"],
        "steps": recipe["steps"]
    }

    return jsonify({'message': f'recipe "{recipe_name}" created sucsesfully!'}), 201

@app.route('/thanksgivingrecipes/<string:recipe_name>', methods=['DELETE'])
def delete_recipe(recipe_name: str):
    global thanksgivingrecipes
    recipe_name = recipe_name.lower()

    if recipe_name not in thanksgivingrecipes:
        return jsonify({'error': 'recipe does not exist'}), 404
    
    deleted_recipe = thanksgivingrecipes.pop(recipe_name)
    return jsonify(deleted_recipe), 200

if __name__ == '__main__':
    app.run(port=5000)
