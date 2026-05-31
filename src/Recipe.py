class Recipe:
    def __init__(self, title: str, ingredients: Ingredient) -> None:
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient) -> None:
        if ingredient in self.ingredients:
            for i in range(len(self.ingredients)):
                if self.ingredients[i] == ingredient: self.ingredients[i].quantity += ingredient.quantity
        else:
            self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if isinstance(ratio, (int,float,complex)):
            if ratio > 0: return True
        return False
    def scale(self, ratio: float) -> Recipe:
        new_recipe = Recipe(self.title, [])
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit)
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe
    def  __len__(self): return len(self.ingredients)
    def __str__(self):
        return self.title + " Ингридиенты:" +  ", ".join(str(ingridient) for ingridient in self.ingredients)