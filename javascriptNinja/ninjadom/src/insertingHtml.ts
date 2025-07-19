/**
 * This is an overview of how to insert HTML with javascript
 * 1. createElement
 * 2. appendChild
 * 3. insertBefore
 * 4. insertAdjacentHTML
 * 5. third-party libraries like jQuery and React.js (not covered)
 * 6. innerHTML
 */
const node = document.querySelector<HTMLDivElement>('#insertingHTML');
const actionButton = document.querySelector<HTMLButtonElement>('#insertingHTML .btn');

// insertAdjacentHTML doesn't return a node, but allows us to easily use a string
node?.insertAdjacentHTML('beforeend', '<p>Hello world!</p>');

// Creating an element and appending it is a lot of work
const pChild = document.createElement('p');
if (pChild) {
  pChild.textContent = 'Hello appendChild';
  pChild?.classList.add('text-blue-500');
  node?.appendChild(pChild);
}

function addAlert(event: Event) {
  event.preventDefault();
  const pBefore = document.createElement('p');

  if (pBefore && pChild) {
    pBefore.textContent = 'Hello insertBefore';
    pBefore.classList.add('text-amber-500');
    // Note, we use the parent node, and pass the element we want to add, and the child
    // node to insert before (otherwise it will be added to the end
    node?.insertBefore(pBefore, pChild);
  }
}

actionButton?.addEventListener('click', addAlert);
