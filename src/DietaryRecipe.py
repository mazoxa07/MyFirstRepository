class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: Ingredient) -> None:
        super(title, self.ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float) -> DietaryRecipe:
        ingredients = super().scale(ratio)
        diet = DietaryRecipe(self.title, self.diet_type, ingredients)
        return diet
    def __str__(self): return f"[{self.diet_type}] {self.title}"