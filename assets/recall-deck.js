/* ============================================================
   AI-Forward course — recall-deck component
   Phone-friendly retrieval practice. Each .card starts showing
   only its prompt; tap to reveal the answer. Retrieval BEFORE
   reveal is the whole point — think the answer out loud first.
   Behavior only; styling lives in assets/style.css (.card).
   ============================================================ */
(function () {
  function wire() {
    var cards = document.querySelectorAll('.card');
    cards.forEach(function (card) {
      var back = card.querySelector('.card-back');
      if (!back) return;
      card.setAttribute('role', 'button');
      card.setAttribute('tabindex', '0');
      function toggle() {
        var open = card.classList.toggle('revealed');
        card.setAttribute('aria-expanded', open ? 'true' : 'false');
      }
      card.addEventListener('click', toggle);
      card.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
      });
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wire);
  } else {
    wire();
  }
})();
