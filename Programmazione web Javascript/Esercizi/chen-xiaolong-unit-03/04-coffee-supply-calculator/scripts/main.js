/**
 * Description placeholder
 *
 * @param {number} currentAge 
 * @param {number} maximumAge 
 * @param {number} quantity 
 */
function calculateSupply(currentAge, maximumAge, quantity) {
    console.log("You will need", (maximumAge - currentAge) * quantity * 365,"cups of coffee to last you until the age of", maximumAge);
}

calculateSupply(20, 21, 0.5);
calculateSupply(18, 74, 0.3);
calculateSupply(33, 75, 0.7);
