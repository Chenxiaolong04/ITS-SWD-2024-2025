// Create 3 dirty stacks with random plates (10-15 each)
const dirtyStacks = [[], [], []];
const cleanStack = [];

for (let i = 0; i < 3; i++) {
  const count = Math.floor(Math.random() * 6) + 10; // 10-15 plates
  for (let j = 0; j < count; j++) {
    dirtyStacks[i].push({ id: `P${i + 1}-${j + 1}` });
  }
}

// Draw current state of all stacks
function drawStacks() {
  for (let i = 0; i < 3; i++) {
    const container = document.getElementById(`dirty${i + 1}`);
    container.innerHTML = `<h3>Dirty Stack ${i + 1}</h3>`;
    dirtyStacks[i].forEach(() => {
      const plate = document.createElement('div');
      plate.className = 'dish';
      container.appendChild(plate);
    });
  }

  const clean = document.getElementById('clean');
  clean.innerHTML = `<h3>Clean Stack</h3>`;
  cleanStack.forEach(() => {
    const plate = document.createElement('div');
    plate.className = 'dish';
    clean.appendChild(plate);
  });
}

// Wash one dish: move one dish from a random non-empty dirty stack to clean stack
// Returns true if a dish was washed, false if none available
function washDish() {
  const availableStacks = dirtyStacks.filter(stack => stack.length > 0);
  if (availableStacks.length === 0) return false;

  const stack = availableStacks[Math.floor(Math.random() * availableStacks.length)];
  const dish = stack.pop();
  cleanStack.push(dish);
  return true;
}

// Wash two dishes at once (bonus)
// Returns number of dishes actually washed (0,1 or 2)
function washTwoDishes() {
  let washed = 0;
  if (washDish()) washed++;
  if (washDish()) washed++;
  drawStacks();
  return washed;
}

// Utility delay function
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Run simulation: wash all dirty dishes two at a time, random delay between washes
async function runSimulation() {
  let remaining = dirtyStacks.reduce((acc, stack) => acc + stack.length, 0);

  while (remaining > 0) {
    const washedNow = washTwoDishes();
    remaining -= washedNow;
    await delay(Math.random() * 1000 + 500); // 500ms to 1500ms delay
  }
}

// Initial render
drawStacks();
