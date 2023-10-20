document.addEventListener('DOMContentLoaded', function() {
  let remainingSeconds = 20;

  const timer = document.getElementById('timer');
  updateTimer();

  setInterval(function() {
    remainingSeconds--;
    updateTimer();
  }, 10);

  function updateTimer() {
    const minutes = Math.floor(remainingSeconds / 60);
    const seconds = remainingSeconds % 60;

    timer.innerText = `${padLeft(minutes)}:${padLeft(seconds)}`;
  }

  function padLeft(value) {
    return String(value).padStart(2, '0');
    
    
  }
});

document.addEventListener('DOMContentLoaded', function() {
  const modal = document.getElementById('modal');
  const modalClose = document.getElementById('modal-close');

  modalClose.addEventListener('click', function() {
    modal.style.display = 'none';
  });

  // Trigger the modal pop-up
  showModal();
});

function showModal() {
    const modal = document.getElementById('modal');
    modal.style.display = 'block';
}
