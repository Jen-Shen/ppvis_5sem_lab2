from model.entity.recipe import Recipe


class Account:
    def __init__(self, name_of_profile: str, email: str, password: str, recipe: Recipe, secret_key: str):
        self.name_of_profile = name_of_profile
        self.email = email
        self.password = password
        self.secret_key = secret_key
        self.list_of_recipe = list()
        self.list_of_recipe.append(recipe)

