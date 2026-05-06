/* =============================================
   PORTFOLIO — script.js
   - Cursor glow that follows the mouse
   - Active nav link updates on scroll
   ============================================= */

// ---- Cursor glow ----
const glow = document.getElementById('glow');

document.addEventListener('mousemove', (e) => {
  glow.style.left = e.clientX + 'px';
  glow.style.top  = e.clientY + 'px';
});

// Hide glow when mouse leaves the window
document.addEventListener('mouseleave', () => {
  glow.style.opacity = '0';
});
document.addEventListener('mouseenter', () => {
  glow.style.opacity = '1';
});


// ---- Active nav link on scroll ----
const sections  = document.querySelectorAll('main section[id]');
const navLinks  = document.querySelectorAll('.nav-link');

const observerOptions = {
  root: null,
  rootMargin: '-30% 0px -60% 0px',  // trigger when section is roughly in view
  threshold: 0,
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const id = entry.target.getAttribute('id');

      navLinks.forEach((link) => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${id}`) {
          link.classList.add('active');
        }
      });
    }
  });
}, observerOptions);

sections.forEach((section) => observer.observe(section));


// ---- Smooth scroll for nav links ----
navLinks.forEach((link) => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const targetId = link.getAttribute('href').slice(1);
    const target   = document.getElementById(targetId);
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
