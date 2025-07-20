/**
 * macrotasks vs microtasks:
 * JS engines include multiple event loop queues,
 * 1 macrotask is processed on each pass through the event loop, and all the microtasks.
 * Microtasks are prioritized, over macrotasks.
 *
 */
const launchBtn = document.getElementById('launchTasks');

function manyTasks() {
  console.log('👆 Click event (macrotask)');

  // Microtask: queued in the microtask queue
  Promise.resolve().then(() => {
    console.log('🔬 Microtask: Promise.then #1');
  });

  // Macrotask: setTimeout
  setTimeout(() => {
    console.log('⏰ Macrotask: setTimeout');
  }, 0);

  // Another Microtask
  queueMicrotask(() => {
    console.log('🔬 Microtask: queueMicrotask');
  });

  // Another Promise
  Promise.resolve().then(() => {
    console.log('🔬 Microtask: Promise.then #2');
  });

  console.log('📦 End of click handler');
}

launchBtn?.addEventListener('click', manyTasks);
