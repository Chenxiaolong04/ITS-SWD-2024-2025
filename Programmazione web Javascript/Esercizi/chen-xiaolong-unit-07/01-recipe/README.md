# 01-recipe
Autor: Chen Xiaolong  
Contact: xiao.chen@edu-its.it
## Exercise requirements
Create an object to hold information on your favorite recipe. It should have
properties for title (a string), servings (a number), and ingredients (an
array of strings).
● On separate lines (one console.log statement for each), log the recipe
information
Bonus: Create an array that holds several recipes and log them all

## Problem Description
The goal of this project is to iterate through a list of recipes and print their details in a user-friendly format. Each recipe contains the following properties:
- **title**: The name of the dish.
- **servings**: The number of servings the dish provides.
- **ingredients**: A list of ingredients used in the recipe.

## Approach to Solution
1. **Data Representation**:
   - The recipes are represented as an array of objects, where each object has three properties: `title`, `servings`, and `ingredients`.
   - The `ingredients` property is an array of strings, representing individual ingredients required for the recipe.

2. **Iterating Through Recipes**:
   - A `for...in` loop is used to iterate over each recipe in the `recipe` array.
   - For each recipe, another loop iterates over its properties (`title`, `servings`, `ingredients`), and depending on the property, the relevant information is printed out to the console.

3. **Switch Statement**:
   - A `switch` statement is used to identify which property is being accessed (`title`, `servings`, or `ingredients`), and prints the corresponding information in a human-readable format.

4. **JSDoc Comments**:
   - The code is documented using JSDoc comments, which explain the purpose and type of each variable and function. This ensures that the code is easy to understand and maintain by other developers.


