/**
 * @file main.js
 * @author Chen Xiaolong
 */

/**
 * Array containing different recipes, each with a title, number of servings, and ingredients.
 * @type {Array<{title: string, servings: number, ingredients: string[]}>}
 */
let recipe = [
    {
        title: "pasta al pomodoro",
        servings: 2,
        ingredients: ["pasta", "pomodori", "olio d'oliva", "aglio", "basilico"]
    },
    {
        title: "insalata greca",
        servings: 2,
        ingredients: ["pomodori", "cetrioli", "cipolla rossa", "feta", "olive nere", "olio d'oliva", "origano"]
    }
];

/**
 * Loops through the recipe array and logs the details of each recipe, including its title, servings, and ingredients.
 * @param {Array<{title: string, servings: number, ingredients: string[]}>} recipe - Array of recipe objects containing the title, number of servings, and ingredients.
 */
for (let x in recipe) {
    for (let k in recipe[x]) {
        switch (k) {
            case "title":
                console.log("Title: " + recipe[x][k]);
                continue;

            case "servings":
                console.log("Serving: " + recipe[x][k]);
                continue;

            case "ingredients":
                console.log("Ingredients: " + recipe[x][k]);
                continue;
        }
    }
}
