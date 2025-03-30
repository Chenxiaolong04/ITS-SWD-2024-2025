/**
 * @param {string} name 
 * @param {string} group 
 */
function checkGroup(name, group) {
    if (group.includes(name)) {
        console.log(`${name} IS part of the group`);
    } else {
        console.log(`${name} is NOT part of the group`);
    }
}

let groupNames = "Mary, James, and John";
let oldGuy = "James"; 
let newGuy = "Philip"; 

checkGroup(oldGuy, groupNames);
checkGroup(newGuy, groupNames);