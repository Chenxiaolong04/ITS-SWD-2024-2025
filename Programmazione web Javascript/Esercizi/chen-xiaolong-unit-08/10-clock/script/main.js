/**
 * @file: main.js
 * @author: Chen Xiaolong
 */
setInterval(() => {
    let now = new Date();
    let hours = now.getHours().toString().padStart(2, '0');
    let minutes = now.getMinutes().toString().padStart(2, '0');
    let seconds = now.getSeconds().toString().padStart(2, '0');

    let timeString = `${hours}:${minutes}:${seconds}`;
    console.log(timeString);
}, 1000);



