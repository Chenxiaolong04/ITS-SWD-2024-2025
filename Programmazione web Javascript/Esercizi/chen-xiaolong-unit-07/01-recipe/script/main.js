/**
 * @file Main game file for Hangman game
 * @author Chen Xiaolong
 */
let recipe = [
    {
        title : "pasta al pomodoro",
        servings : 2,
        ingredients : ["pasta", "pomodori", "olio d'oliva", "aglio", "basilico"]
    },
    {
        title : "insalata greca",
        servings : 2,
        ingredients : ["pomodori", "cetrioli", "cipolla rossa", "feta", "olive nere", "olio d'oliva", "origano"]
    }
];

for(x in recipe) {
    for(k in recipe[x]) {
        switch(k) {
    
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
