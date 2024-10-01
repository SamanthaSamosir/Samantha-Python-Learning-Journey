veggies = ["spinach","kale","collard greens","bell peppers",
           "hot peppers","celery","tomatoes","cucumbers","lettuce","potatoes","green beans","peas","zucchini","summer squash"]
fruits = ["rawberries", "apples", "grapes", "pears", "cherries", "peaches", "nectarines", "blueberries", "raspberries", "plums", "citrus fruits", "apricots", "kiwis"]
#Let's create nested List
dirtyDozen=[veggies, fruits] #[0][1]
print(dirtyDozen)
print(dirtyDozen[0])
print(dirtyDozen[1])
print(dirtyDozen[1][2]) #[list][items inside the list]
print(dirtyDozen[0][3])