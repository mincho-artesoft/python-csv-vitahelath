// Auto-generated from foods_full_merged.csv
import Foundation

public enum FoodCategory: String, Codable, CaseIterable {
    case appleJuice = "Apple juice"
    case apples = "Apples"
    case babyFoodCereals = "Baby food: cereals"
    case babyFoodFruit = "Baby food: fruit"
    case babyFoodMeatAndDinners = "Baby food: meat and dinners"
    case babyFoodMixtures = "Baby food: mixtures"
    case babyFoodSnacksAndSweets = "Baby food: snacks and sweets"
    case babyFoodVegetables = "Baby food: vegetables"
    case babyFoodYogurt = "Baby food: yogurt"
    case babyJuice = "Baby juice"
    case babyWater = "Baby water"
    case bacon = "Bacon"
    case bagelsAndEnglishMuffins = "Bagels and English muffins"
    case bananas = "Bananas"
    case bean = "Bean"
    case beans = "Beans"
    case beef = "Beef"
    case beer = "Beer"
    case biscuits = "Biscuits"
    case blueberriesAndOtherBerries = "Blueberries and other berries"
    case bottledWater = "Bottled water"
    case broccoli = "Broccoli"
    case burgers = "Burgers"
    case burritosAndTacos = "Burritos and tacos"
    case butterAndAnimalFats = "Butter and animal fats"
    case cabbage = "Cabbage"
    case cakesAndPies = "Cakes and pies"
    case candyContainingChocolate = "Candy containing chocolate"
    case candyNotContainingChocolate = "Candy not containing chocolate"
    case carrots = "Carrots"
    case cerealBars = "Cereal bars"
    case cheese = "Cheese"
    case cheeseSandwiches = "Cheese sandwiches"
    case chicken = "Chicken"
    case chickenFilletSandwiches = "Chicken fillet sandwiches"
    case chickenPatties = "Chicken patties"
    case citrusFruits = "Citrus fruits"
    case citrusJuice = "Citrus juice"
    case coffee = "Coffee"
    case coldCutsAndCuredMeats = "Cold cuts and cured meats"
    case coleslaw = "Coleslaw"
    case cookiesAndBrownies = "Cookies and brownies"
    case corn = "Corn"
    case cottageRicottaCheese = "Cottage/ricotta cheese"
    case crackers = "Crackers"
    case creamAndCreamSubstitutes = "Cream and cream substitutes"
    case creamCheese = "Cream cheese"
    case deliAndCuredMeatSandwiches = "Deli and cured meat sandwiches"
    case dietSoftDrinks = "Diet soft drinks"
    case dietSportAndEnergyDrinks = "Diet sport and energy drinks"
    case dips = "Dips"
    case doughnuts = "Doughnuts"
    case driedFruits = "Dried fruits"
    case eggRolls = "Egg rolls"
    case eggBreakfastSandwiches = "Egg/breakfast sandwiches"
    case eggsAndOmelets = "Eggs and omelets"
    case enhancedWater = "Enhanced water"
    case fish = "Fish"
    case flavoredMilk = "Flavored milk"
    case flavoredOrCarbonatedWater = "Flavored or carbonated water"
    case formula = "Formula"
    case frankfurterSandwiches = "Frankfurter sandwiches"
    case frankfurters = "Frankfurters"
    case frenchFriesAndOtherFriedWhitePotatoes = "French fries and other fried white potatoes"
    case frenchToast = "French toast"
    case friedRiceAndLoChowMein = "Fried rice and lo/chow mein"
    case friedVegetables = "Fried vegetables"
    case fruitDrinks = "Fruit drinks"
    case gelatins = "Gelatins"
    case grapes = "Grapes"
    case greek = "Greek"
    case gritsAndOtherCookedCereals = "Grits and other cooked cereals"
    case groundBeef = "Ground beef"
    case iceCreamAndFrozenDairyDesserts = "Ice cream and frozen dairy desserts"
    case jams = "Jams"
    case lamb = "Lamb"
    case lettuceAndLettuceSalads = "Lettuce and lettuce salads"
    case liquorAndCocktails = "Liquor and cocktails"
    case liverAndOrganMeats = "Liver and organ meats"
    case macaroniAndCheese = "Macaroni and cheese"
    case mangoAndPapaya = "Mango and papaya"
    case margarine = "Margarine"
    case mashedPotatoesAndWhitePotatoMixtures = "Mashed potatoes and white potato mixtures"
    case mayonnaise = "Mayonnaise"
    case meatAndBbqSandwiches = "Meat and BBQ sandwiches"
    case meatMixedDishes = "Meat mixed dishes"
    case melons = "Melons"
    case milk = "Milk"
    case milkShakesAndOtherDairyDrinks = "Milk shakes and other dairy drinks"
    case mustardAndOtherCondiments = "Mustard and other condiments"
    case nachos = "Nachos"
    case notIncludedInAFoodCategory = "Not included in a food category"
    case nutritionBars = "Nutrition bars"
    case nutritionalBeverages = "Nutritional beverages"
    case nutsAndSeeds = "Nuts and seeds"
    case oatmeal = "Oatmeal"
    case olives = "Olives"
    case onions = "Onions"
    case otherMexicanMixedDishes = "Other Mexican mixed dishes"
    case otherDarkGreenVegetables = "Other dark green vegetables"
    case otherDietDrinks = "Other diet drinks"
    case otherFruitJuice = "Other fruit juice"
    case otherFruitsAndFruitSalads = "Other fruits and fruit salads"
    case otherRedAndOrangeVegetables = "Other red and orange vegetables"
    case otherStarchyVegetables = "Other starchy vegetables"
    case otherVegetablesAndCombinations = "Other vegetables and combinations"
    case pancakes = "Pancakes"
    case pasta = "Pasta"
    case pastaMixedDishes = "Pasta mixed dishes"
    case pastaSauces = "Pasta sauces"
    case peachesAndNectarines = "Peaches and nectarines"
    case peanutButterAndJellySandwiches = "Peanut butter and jelly sandwiches"
    case pears = "Pears"
    case pineapple = "Pineapple"
    case pizza = "Pizza"
    case plantBasedMilk = "Plant-based milk"
    case plantBasedYogurt = "Plant-based yogurt"
    case popcorn = "Popcorn"
    case pork = "Pork"
    case potatoChips = "Potato chips"
    case poultryMixedDishes = "Poultry mixed dishes"
    case pretzelsSnackMix = "Pretzels/snack mix"
    case proteinAndNutritionalPowders = "Protein and nutritional powders"
    case pudding = "Pudding"
    case ramenAndAsianBrothBasedSoups = "Ramen and Asian broth-based soups"
    case readyToEatCereal = "Ready-to-eat cereal"
    case rice = "Rice"
    case riceMixedDishes = "Rice mixed dishes"
    case rollsAndBuns = "Rolls and buns"
    case saladDressingsAndVegetableOils = "Salad dressings and vegetable oils"
    case saltineCrackers = "Saltine crackers"
    case sausages = "Sausages"
    case seafoodMixedDishes = "Seafood mixed dishes"
    case seafoodSandwiches = "Seafood sandwiches"
    case shellfish = "Shellfish"
    case smoothiesAndGrainDrinks = "Smoothies and grain drinks"
    case softDrinks = "Soft drinks"
    case soups = "Soups"
    case soyAndMeatAlternativeProducts = "Soy and meat-alternative products"
    case soyBasedCondiments = "Soy-based condiments"
    case spinach = "Spinach"
    case sportAndEnergyDrinks = "Sport and energy drinks"
    case stirFryAndSoyBasedSauceMixtures = "Stir-fry and soy-based sauce mixtures"
    case strawberries = "Strawberries"
    case stringBeans = "String beans"
    case sugarSubstitutes = "Sugar substitutes"
    case sugarsAndHoney = "Sugars and honey"
    case tapWater = "Tap water"
    case tea = "Tea"
    case tomatoBasedCondiments = "Tomato-based condiments"
    case tomatoes = "Tomatoes"
    case tortilla = "Tortilla"
    case tortillas = "Tortillas"
    case turkey = "Turkey"
    case turnoversAndOtherGrainBasedItems = "Turnovers and other grain-based items"
    case vegetableDishes = "Vegetable dishes"
    case vegetableJuice = "Vegetable juice"
    case vegetableSandwichesBurgers = "Vegetable sandwiches/burgers"
    case vegetablesOnASandwich = "Vegetables on a sandwich"
    case whitePotatoes = "White potatoes"
    case wine = "Wine"
    case yeastBreads = "Yeast breads"
    case yogurt = "Yogurt"
    case bakedOrBoiled = "baked or boiled"
    case brothBased = "broth-based"
    case cookedGrains = "cooked grains"
    case corn = "corn"
    case creamBased = "cream-based"
    case duck = "duck"
    case dumplings = "dumplings"
    case excludesGround = "excludes ground"
    case excludesMacaroniAndCheese = "excludes macaroni and cheese"
    case excludesSaltines = "excludes saltines"
    case game = "game"
    case goat = "goat"
    case gravies = "gravies"
    case higherSugar212G100G = "higher sugar (>21.2g/100g)"
    case ices = "ices"
    case legumeDishes = "legume dishes"
    case legumes = "legumes"
    case lowerSugar212G100G = "lower sugar (=<21.2g/100g)"
    case lowfat = "lowfat"
    case muffins = "muffins"
    case nonLettuceSalads = "non-lettuce salads"
    case nonfat = "nonfat"
    case noodles = "noodles"
    case nuggetsAndTenders = "nuggets and tenders"
    case otherChips = "other chips"
    case otherPoultry = "other poultry"
    case otherSauces = "other sauces"
    case pastries = "pastries"
    case pea = "pea"
    case peas = "peas"
    case pickledVegetables = "pickled vegetables"
    case pickles = "pickles"
    case preparedFromPowder = "prepared from powder"
    case quickBreads = "quick breads"
    case readyToFeed = "ready-to-feed"
    case reducedFat = "reduced fat"
    case regular = "regular"
    case sorbets = "sorbets"
    case sourCream = "sour cream"
    case sushi = "sushi"
    case sweetRolls = "sweet rolls"
    case syrups = "syrups"
    case tomatoBased = "tomato-based"
    case toppings = "toppings"
    case waffles = "waffles"
    case whippedCream = "whipped cream"
    case whole = "whole"
    case wholePieces = "whole pieces"
}

public enum FoodGroup: String, Codable, CaseIterable {
    case algae = "Algae"
    case beverages = "Beverages"
    case celery = "Celery"
    case chocolate = "Chocolate"
    case coconutMilk = "Coconut Milk"
    case compositeMeal = "Composite Meal"
    case condiments = "Condiments"
    case connectiveTissue = "Connective Tissue"
    case dairy = "Dairy"
    case energyDrink = "Energy Drink"
    case fillings = "Fillings"
    case fruits = "Fruits"
    case fungi = "Fungi"
    case grains = "Grains"
    case herbs = "Herbs"
    case legumes = "Legumes"
    case medicinal = "Medicinal"
    case nuts = "Nuts"
    case oilsAndFats = "Oils and fats"
    case olives = "Olives"
    case plantDairy = "Plant-Dairy"
    case plants = "Plants"
    case probiotic = "Probiotic"
    case proteins = "Proteins"
    case raisins = "Raisins"
    case root = "Root"
    case roots = "Roots"
    case salad = "Salad"
    case seaweed = "Seaweed"
    case seeds = "Seeds"
    case soy = "Soy"
    case specializedNutrition = "Specialized Nutrition"
    case spices = "Spices"
    case stimulant = "Stimulant"
    case sweetsAndSnacks = "Sweets and snacks"
    case vegetables = "Vegetables"
    case water = "Water"
}

public enum MacronutrientFocus: String, Codable, CaseIterable {
    case alcohol = "Alcohol"
    case bVitamins = "B-Vitamins"
    case balanced = "Balanced"
    case calciumFortified = "Calcium-fortified"
    case carbohydrateRich = "Carbohydrate-rich"
    case fatRich = "Fat-rich"
    case flavorRich = "Flavor-rich"
    case lowCalorie = "Low Calorie"
    case mineralRich = "Mineral-rich"
    case nA = "N/A"
    case probiotic = "Probiotic"
    case proteinRich = "Protein-rich"
    case stimulant = "Stimulant"
    case umamiRich = "Umami-rich"
    case variable = "Variable"
    case vitaminRich = "Vitamin-rich"
}

public enum ProcessingLevel: String, Codable, CaseIterable {
    case highlyProcessed = "Highly Processed"
    case minimallyProcessed = "Minimally Processed"
    case processed = "Processed"
    case unprocessed = "Unprocessed"
}

public enum CulinaryUsage: String, Codable, CaseIterable {
    case afterDinnerDrink = "After-Dinner Drink"
    case alcoholicBeverage = "Alcoholic Beverage"
    case alcoholicNovelty = "Alcoholic Novelty"
    case antipasto = "Antipasto"
    case appetizer = "Appetizer"
    case appetizerBase = "Appetizer Base"
    case appetizerPlatter = "Appetizer Platter"
    case babyDessert = "Baby Dessert"
    case babyFood = "Baby Food"
    case babyToddlerCookie = "Baby/Toddler Cookie"
    case babyToddlerMeal = "Baby/Toddler Meal"
    case babyToddlerSnack = "Baby/Toddler Snack"
    case babyToddlerSnackBar = "Baby/Toddler Snack Bar"
    case babyToddlerTeethingBiscuit = "Baby/Toddler Teething Biscuit"
    case bakedGood = "Baked Good"
    case baking = "Baking"
    case bakingIngredient = "Baking Ingredient"
    case baseForDishes = "Base for Dishes"
    case baseForSoups = "Base for Soups"
    case baseForSweetSavoryDishes = "Base for Sweet/Savory Dishes"
    case beans = "Beans"
    case beverage = "Beverage"
    case beverageAdditive = "Beverage Additive"
    case beverageMixPowder = "Beverage Mix Powder"
    case beverageMixIn = "Beverage Mix-in"
    case bread = "Bread"
    case breadProduct = "Bread Product"
    case breadSubstitute = "Bread Substitute"
    case breakfast = "Breakfast"
    case breakfastAccompaniment = "Breakfast Accompaniment"
    case breakfastBar = "Breakfast Bar"
    case breakfastBread = "Breakfast Bread"
    case breakfastCereal = "Breakfast Cereal"
    case breakfastCracker = "Breakfast Cracker"
    case breakfastItem = "Breakfast Item"
    case breakfastMeat = "Breakfast Meat"
    case breakfastPastry = "Breakfast Pastry"
    case breakfastReplacement = "Breakfast Replacement"
    case breakfastSandwichBase = "Breakfast Sandwich Base"
    case breakfastSideDish = "Breakfast Side Dish"
    case breakfastSupplementMix = "Breakfast Supplement Mix"
    case breakfastTaquito = "Breakfast Taquito"
    case breathFreshener = "Breath Freshener"
    case brownie = "Brownie"
    case brunch = "Brunch"
    case bun = "Bun"
    case bunForHamburger = "Bun for Hamburger"
    case bunForHotDog = "Bun for Hot Dog"
    case burritoShell = "Burrito Shell"
    case cake = "Cake"
    case cakeBase = "Cake Base"
    case cakeCupcakeTopping = "Cake/Cupcake Topping"
    case campfireTreat = "Campfire Treat"
    case candy = "Candy"
    case candyBar = "Candy Bar"
    case candyBarComponent = "Candy Bar Component"
    case casserole = "Casserole"
    case casseroleComponent = "Casserole Component"
    case celebrationCake = "Celebration Cake"
    case chewingGum = "Chewing Gum"
    case coatingForFriedBakedFoods = "Coating for Fried/Baked Foods"
    case cocktail = "Cocktail"
    case cocktailIngredient = "Cocktail Ingredient"
    case cocktailMixer = "Cocktail Mixer"
    case coffeeDrink = "Coffee Drink"
    case coldCut = "Cold Cut"
    case componentOfChowMeinDish = "Component of Chow Mein dish"
    case condiment = "Condiment"
    case convenienceFood = "Convenience Food"
    case cookedToAPaste = "Cooked to a paste"
    case cookie = "Cookie"
    case cookieBar = "Cookie Bar"
    case cookingAromatic = "Cooking Aromatic"
    case cookingBase = "Cooking Base"
    case cookingFat = "Cooking Fat"
    case cookingGreen = "Cooking Green"
    case cookingMedium = "Cooking Medium"
    case cookingOil = "Cooking Oil"
    case cookingSauce = "Cooking Sauce"
    case cornCake = "Corn Cake"
    case cornmealFlatbreadPancake = "Cornmeal Flatbread/Pancake"
    case cracker = "Cracker"
    case crepe = "Crepe"
    case curryComponent = "Curry Component"
    case custardLikeCornbread = "Custard-like Cornbread"
    case decoration = "Decoration"
    case dessert = "Dessert"
    case dessertBar = "Dessert Bar"
    case dessertComponent = "Dessert Component"
    case dessertIngredient = "Dessert Ingredient"
    case dessertTamale = "Dessert Tamale"
    case dessertTopping = "Dessert Topping"
    case dietarySupplement = "Dietary Supplement"
    case dimSum = "Dim Sum"
    case dip = "Dip"
    case dipVehicle = "Dip Vehicle"
    case dipping = "Dipping"
    case dippingSauce = "Dipping Sauce"
    case dippingSauceForSeafood = "Dipping Sauce for Seafood"
    case doughnut = "Doughnut"
    case dressing = "Dressing"
    case dressingBase = "Dressing Base"
    case electrolyteBeverage = "Electrolyte Beverage"
    case electrolyteBeverageMixPowder = "Electrolyte Beverage Mix Powder"
    case energyBar = "Energy Bar"
    case energyDrink = "Energy Drink"
    case essentialBeverage = "Essential Beverage"
    case fairFood = "Fair Food"
    case filling = "Filling"
    case finishingOil = "Finishing Oil"
    case flatbread = "Flatbread"
    case flavorBase = "Flavor Base"
    case flavorEnhancer = "Flavor Enhancer"
    case flavoring = "Flavoring"
    case flavoringOil = "Flavoring Oil"
    case forInfantFormulaDrinking = "For Infant Formula/Drinking"
    case friedCookiePastry = "Fried Cookie/Pastry"
    case friedDough = "Fried Dough"
    case friedDoughWithFruit = "Fried Dough with Fruit"
    case friedFlatbread = "Fried Flatbread"
    case friedPastry = "Fried Pastry"
    case friedStripsForSoupSalad = "Fried Strips for Soup/Salad"
    case frozenDessert = "Frozen Dessert"
    case frozenTreat = "Frozen Treat"
    case fruit = "Fruit"
    case frying = "Frying"
    case fryingFat = "Frying Fat"
    case fryingMedium = "Frying Medium"
    case garnish = "Garnish"
    case glaze = "Glaze"
    case gravy = "Gravy"
    case grilling = "Grilling"
    case hamburgerToppingSpread = "Hamburger Topping/Spread"
    case handPie = "Hand Pie"
    case healthy = "Healthy"
    case holidayMeal = "Holiday Meal"
    case iceCreamCone = "Ice Cream Cone"
    case infantMeal = "Infant Meal"
    case ingredient = "Ingredient"
    case juice = "Juice"
    case juicing = "Juicing"
    case kidsBeverage = "Kids Beverage"
    case kidsSnackBar = "Kids Snack Bar"
    case kidsSnackCracker = "Kids Snack Cracker"
    case kimchiBase = "Kimchi Base"
    case laminatedDoughForPastries = "Laminated Dough for Pastries"
    case layeredFlatbread = "Layered Flatbread"
    case leaveningAgent = "Leavening Agent"
    case lightCocktail = "Light Cocktail"
    case lightMeal = "Light Meal"
    case mainDish = "Main Dish"
    case margarineProduction = "Margarine Production"
    case marinade = "Marinade"
    case meal = "Meal"
    case mealBase = "Meal Base"
    case mealComponent = "Meal Component"
    case mealReplacement = "Meal Replacement"
    case mealReplacementBar = "Meal Replacement Bar"
    case mealReplacementPowder = "Meal Replacement Powder"
    case meatSubstitute = "Meat Substitute"
    case meatSubstituteMeal = "Meat Substitute Meal"
    case medicalBeverage = "Medical Beverage"
    case medicalFluid = "Medical Fluid"
    case milkFlavoring = "Milk Flavoring"
    case mixer = "Mixer"
    case moderate = "Moderate"
    case muffin = "Muffin"
    case neutral = "Neutral"
    case neutralDebated = "Neutral/Debated"
    case noBakeCookie = "No-Bake Cookie"
    case nonAlcoholicCocktail = "Non-alcoholic Cocktail"
    case nonAlcoholicDrink = "Non-alcoholic Drink"
    case noodles = "Noodles"
    case nutritionBar = "Nutrition Bar"
    case oil = "Oil"
    case omeletFilling = "Omelet Filling"
    case pairedWithCheese = "Paired with Cheese"
    case partyBeverage = "Party Beverage"
    case pasta = "Pasta"
    case pastaAlternative = "Pasta Alternative"
    case pastaDish = "Pasta Dish"
    case pastaDishComponent = "Pasta Dish Component"
    case pastaSauce = "Pasta Sauce"
    case paste = "Paste"
    case pastry = "Pastry"
    case pastryShell = "Pastry Shell"
    case performanceSnack = "Performance Snack"
    case pickling = "Pickling"
    case pizzaComponent = "Pizza Component"
    case pizzaTopping = "Pizza Topping"
    case plainCracker = "Plain Cracker"
    case pocketBread = "Pocket Bread"
    case porridge = "Porridge"
    case potluckDish = "Potluck Dish"
    case preservative = "Preservative"
    case processedFoodIngredient = "Processed Food Ingredient"
    case proteinBar = "Protein Bar"
    case proteinSupplement = "Protein Supplement"
    case proteinSupplementPowder = "Protein Supplement Powder"
    case pudding = "Pudding"
    case quickBread = "Quick Bread"
    case recipe = "Recipe"
    case recipeComponent = "Recipe Component"
    case richBread = "Rich Bread"
    case richLayerCake = "Rich Layer Cake"
    case roll = "Roll"
    case salad = "Salad"
    case saladBase = "Salad Base"
    case saladComponent = "Salad Component"
    case saladDressing = "Salad Dressing"
    case saladIngredient = "Salad Ingredient"
    case saladTopping = "Salad Topping"
    case saladOrHotDish = "Salad or Hot Dish"
    case sandwich = "Sandwich"
    case sandwichBase = "Sandwich Base"
    case sandwichComponent = "Sandwich Component"
    case sandwichFilling = "Sandwich Filling"
    case sandwichLayer = "Sandwich Layer"
    case sandwichMeat = "Sandwich Meat"
    case sandwichSpreadLayer = "Sandwich Spread/Layer"
    case sandwichTopping = "Sandwich Topping"
    case sandwichBase = "Sandwich base"
    case sauce = "Sauce"
    case sauceBase = "Sauce Base"
    case sauceTopping = "Sauce Topping"
    case sauceForWings = "Sauce for Wings"
    case savoryPancake = "Savory Pancake"
    case savoryPastry = "Savory Pastry"
    case seasoning = "Seasoning"
    case shellForMexicanDish = "Shell for Mexican Dish"
    case shot = "Shot"
    case sideDish = "Side Dish"
    case sideDishComponent = "Side Dish Component"
    case slaw = "Slaw"
    case smallCracker = "Small Cracker"
    case smoothieIngredient = "Smoothie Ingredient"
    case snack = "Snack"
    case snackBar = "Snack Bar"
    case snackCake = "Snack Cake"
    case snackChip = "Snack Chip"
    case snackPuffCrunchy = "Snack Puff/Crunchy"
    case snackPuffRing = "Snack Puff/Ring"
    case sodaCracker = "Soda Cracker"
    case soup = "Soup"
    case soupBase = "Soup Base"
    case soupComponent = "Soup Component"
    case soupGarnish = "Soup Garnish"
    case soupIngredient = "Soup Ingredient"
    case sourdoughFlatbread = "Sourdough Flatbread"
    case spice = "Spice"
    case spread = "Spread"
    case staple = "Staple"
    case stapleMealComponent = "Staple Meal Component"
    case steamedBread = "Steamed Bread"
    case stew = "Stew"
    case stewComponent = "Stew Component"
    case stirFry = "Stir-fry"
    case stirFryIngredient = "Stir-fry Ingredient"
    case streetFood = "Street Food"
    case stuffing = "Stuffing"
    case submarineSandwichRoll = "Submarine Sandwich Roll"
    case sugar = "Sugar"
    case summerSausage = "Summer Sausage"
    case supplement = "Supplement"
    case supplementPowder = "Supplement Powder"
    case sushi = "Sushi"
    case sushiComponent = "Sushi Component"
    case sushiRoll = "Sushi Roll"
    case sweet = "Sweet"
    case sweetBread = "Sweet Bread"
    case sweetCracker = "Sweet Cracker"
    case sweetRoll = "Sweet Roll"
    case sweetTurnover = "Sweet Turnover"
    case sweetener = "Sweetener"
    case tacoBase = "Taco Base"
    case tacoFilling = "Taco Filling"
    case tacoShell = "Taco Shell"
    case tamales = "Tamales"
    case teaBiscuit = "Tea Biscuit"
    case teaTime = "Tea Time"
    case teethingBiscuit = "Teething Biscuit"
    case throatLozenge = "Throat Lozenge"
    case toddlerMeal = "Toddler Meal"
    case toddlerMealSupplement = "Toddler Meal/Supplement"
    case topping = "Topping"
    case treat = "Treat"
    case unleavenedCracker = "Unleavened Cracker"
    case veryUnhealthy = "Very Unhealthy"
    case warmBeverage = "Warm Beverage"
    case warmCocktail = "Warm Cocktail"
    case warmHolidayCocktail = "Warm Holiday Cocktail"
    case warmSalad = "Warm Salad"
    case warmColdCocktail = "Warm/Cold Cocktail"
    case wrap = "Wrap"
    case wrapper = "Wrapper"
}

public enum HealthImpact: String, Codable, CaseIterable {
    case essential = "Essential"
    case healthy = "Healthy"
    case moderate = "Moderate"
    case neutral = "Neutral"
    case unhealthy = "Unhealthy"
    case variable = "Variable"
    case veryUnhealthy = "Very Unhealthy"
}

public enum Diet: String, Codable, CaseIterable {
    case dairyFree = "Dairy-Free"
    case eggFree = "Egg-Free"
    case glutenFree = "Gluten-Free"
    case halal = "Halal"
    case highProtein = "High-Protein"
    case keto = "Keto"
    case kosher = "Kosher"
    case lactoseFree = "Lactose-Free"
    case lowSodium = "Low Sodium"
    case lowCarb = "Low-Carb"
    case lowFat = "Low-Fat"
    case mineralRich = "Mineral-Rich"
    case noAddedSugar = "No Added Sugar"
    case nutFree = "Nut-Free"
    case paleo = "Paleo"
    case pescatarian = "Pescatarian"
    case soyFree = "Soy-Free"
    case vegan = "Vegan"
    case vegetarian = "Vegetarian"
    case vitaminRich = "Vitamin-Rich"
}

public enum Allergen: String, Codable, CaseIterable {
    case celery = "Celery"
    case cerealsContainingGluten = "Cereals containing gluten"
    case cerealsContainingGlutenBarley = "Cereals containing gluten (barley)"
    case cerealsContainingGlutenOats = "Cereals containing gluten (oats)"
    case crustaceans = "Crustaceans"
    case eggs = "Eggs"
    case fish = "Fish"
    case milk = "Milk"
    case molluscs = "Molluscs"
    case mustard = "Mustard"
    case nuts = "Nuts"
    case nutsBrazilNuts = "Nuts (Brazil nuts)"
    case nutsAlmonds = "Nuts (almonds)"
    case nutsCashews = "Nuts (cashews)"
    case nutsChestnuts = "Nuts (chestnuts)"
    case nutsCoconut = "Nuts (coconut)"
    case nutsHazelnuts = "Nuts (hazelnuts)"
    case nutsMacadamiaNuts = "Nuts (macadamia nuts)"
    case nutsPecans = "Nuts (pecans)"
    case nutsPineNuts = "Nuts (pine nuts)"
    case nutsPistachioNuts = "Nuts (pistachio nuts)"
    case nutsWalnuts = "Nuts (walnuts)"
    case peanuts = "Peanuts"
    case sesameSeeds = "Sesame seeds"
    case soybeans = "Soybeans"
    case sulphurDioxideSulphites = "Sulphur dioxide/sulphites"
}
