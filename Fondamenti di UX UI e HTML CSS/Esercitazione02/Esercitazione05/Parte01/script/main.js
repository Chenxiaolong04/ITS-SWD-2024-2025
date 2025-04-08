let bool = true;
setInterval(() => {
    if (bool) {
        document.documentElement.style.setProperty('--primary-color', '#FFFF00');
    } else {
        document.documentElement.style.setProperty('--primary-color', '#ffaadd');
    }
    bool = !bool;
}, 100);
