/* Reusable self-grading quiz widget for AI-Forward lessons.
   Markup contract:
     <div class="quiz">
       <div class="q" data-answer="1">
         <p class="stem">Question?</p>
         <div class="opts">
           <button class="opt">Option A</button>
           <button class="opt">Option B</button>   // index 1 = correct
         </div>
         <div class="fb" data-ok="Nice — why it's right."
                         data-no="Not quite — the reason.">
         </div>
       </div>
       <p class="progress">Answered 0 of N</p>   // optional, scoped per-quiz
     </div>
   Immediate feedback; retrieval practice; no formatting tells (answers are
   equal-length by construction in the lesson, not enforced here).            */

function initQuizzes() {
  document.querySelectorAll('.quiz').forEach(quiz => {
    const cards = [...quiz.querySelectorAll('.q')];
    const prog = quiz.querySelector('.progress');   // scoped to THIS quiz
    let answered = 0;

    cards.forEach(card => {
      const correct = Number(card.dataset.answer);
      const opts = [...card.querySelectorAll('button.opt')];
      const fb = card.querySelector('.fb');

      opts.forEach((btn, i) => {
        btn.addEventListener('click', () => {
          if (card.dataset.done) return;
          card.dataset.done = '1';
          answered++;
          opts.forEach(b => b.disabled = true);
          opts[correct].classList.add('correct');
          if (i !== correct) btn.classList.add('wrong');
          if (fb) {
            const ok = i === correct;
            fb.textContent = (ok ? '✓  ' : '✗  ') +
              (ok ? (fb.dataset.ok || 'Correct.') : (fb.dataset.no || 'Not quite.'));
            fb.classList.add('show');
            fb.classList.toggle('ok', ok);
          }
          if (prog) prog.textContent =
            `Answered ${answered} of ${cards.length}` +
            (answered === cards.length
              ? ' — done. Come back in a day and try again from memory.' : '');
        });
      });
    });
  });
}

/* Run whether or not DOMContentLoaded has already fired. */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initQuizzes);
} else {
  initQuizzes();
}
