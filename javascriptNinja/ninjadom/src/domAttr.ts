/**
 * Accessing DOM attributes
 * With JS, we can access information in the DOM through 2 ways.
 * 1. the traditional getAttribute/setAttribute --> returns an 'attribute'
 * 2. the dot operator --> returns a 'property'
 * Javascript objects have properties, HTML has attributes. Generally they will
 * return the same value, but they can differ
 */

const incrementBtn = document.querySelector<HTMLButtonElement>('#incrementProgress');
const resetBtn = document.querySelector<HTMLButtonElement>('#resetProgress');
const progressBar = document.querySelector<HTMLProgressElement>('#myProgress');
// If defining custom attributes/properties, it is best practice to prefix with 'data-'
progressBar?.setAttribute('data-foo', String(42));

function increment() {
  if (progressBar) {
    // We can access values via the traditional getAttribute and setAttribute methods
    const maxString = progressBar.getAttribute('max');
    const max = maxString ? parseFloat(maxString) : 0;
    // Or just access them through a property
    const value = progressBar.value;
    if (value + 10 > max) {
      progressBar.value = max;
    } else {
      progressBar.value = value + 10;
    }
  }
}

function resetProgress() {
  if (progressBar) {
    progressBar.value = 0;
  }
}

incrementBtn?.addEventListener('click', increment);
resetBtn?.addEventListener('click', resetProgress);
