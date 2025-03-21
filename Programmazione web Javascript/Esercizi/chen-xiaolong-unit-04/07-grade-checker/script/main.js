/**
 * Description placeholder
 *
 * @param {number} score 
 * @returns {("A" | "B" | "C" | "D" | "F")} 
 */
function assignGrade(score) {
     if (score >= 90)
          return 'A';
     else if (score >= 80)
          return 'B';
     else if (score >= 70)
          return 'C';
     else if (score >= 60)
          return 'D';
     else return 'F';
 }
for(let i=60;i<=100;i++){
     console.log('For '+i+' you got: '+assignGrade(i))
}