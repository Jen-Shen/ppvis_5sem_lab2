from model.entity.account import Account
from model.entity.recipe import Recipe


class Model:
    def __init__(self, recipe, user):
        self.list_of_recipe = recipe
        self.list_of_users = user
        self.user = None

    def registration(self):
        pass

    def entry(self):
        pass

    def lost_password(self, account: Account):
        pass


    def add_recipe(self, recipe: Recipe):
        pass

    def change_recipe(self, recipe: Recipe):
        pass

    def logout(self):
        pass

    def login_without_password(self):
        pass

