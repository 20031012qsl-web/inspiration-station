const root = document.documentElement;
root.classList.remove('no-js');
root.classList.add('js');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const canHover = window.matchMedia('(hover: hover)').matches;
const isMobile = window.matchMedia('(max-width: 760px)').matches;
let pointerFrame = 0;
let pointer = { x: window.innerWidth / 2, y: window.innerHeight / 2 };

function updatePointerVars() {
  pointerFrame = 0;
  root.style.setProperty('--mx', `${pointer.x}px`);
  root.style.setProperty('--my', `${pointer.y}px`);
}

if (canHover && !prefersReducedMotion) {
  window.addEventListener('pointermove', (event) => {
    pointer.x = event.clientX;
    pointer.y = event.clientY;
    if (!pointerFrame) pointerFrame = requestAnimationFrame(updatePointerVars);
  }, { passive: true });
}

const nav = document.querySelector('[data-nav]');
const updateNav = () => nav?.classList.toggle('is-scrolled', window.scrollY > 24);
updateNav();
window.addEventListener('scroll', updateNav, { passive: true });

const revealItems = document.querySelectorAll('.reveal');
if (prefersReducedMotion || !('IntersectionObserver' in window)) {
  revealItems.forEach((item) => item.classList.add('is-visible'));
} else {
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.16, rootMargin: '0px 0px -8% 0px' });
  revealItems.forEach((item) => revealObserver.observe(item));
}

if (window.gsap && window.ScrollTrigger && !prefersReducedMotion) {
  window.gsap.registerPlugin(window.ScrollTrigger);
  window.gsap.timeline({
    scrollTrigger: {
      trigger: '.hero-constellation',
      start: 'top top',
      end: 'bottom top',
      scrub: 0.8
    }
  })
    .to('.star-card', {
      x: 0,
      y: 0,
      rotateX: 0,
      rotateY: 0,
      rotateZ: 0,
      scale: 0.82,
      opacity: 0,
      stagger: { amount: 0.45, from: 'random' },
      ease: 'power2.inOut'
    })
    .from('.ai-method-panel', {
      scale: 0.86,
      opacity: 0,
      y: 70,
      ease: 'power3.out'
    }, '-=0.24');

  window.gsap.utils.toArray('.section-head h2, .section-copy h2, .stage__copy h2').forEach((title) => {
    window.gsap.from(title, {
      scrollTrigger: { trigger: title, start: 'top 82%' },
      y: 42,
      opacity: 0,
      duration: 0.9,
      ease: 'power3.out'
    });
  });

  window.gsap.utils.toArray('.magazine-row').forEach((row, index) => {
    const direction = index % 2 === 0 ? -60 : 60;
    window.gsap.from(row.querySelectorAll('.magazine-card'), {
      scrollTrigger: { trigger: row, start: 'top 85%' },
      x: direction,
      y: 30,
      opacity: 0,
      scale: 0.92,
      stagger: 0.12,
      duration: 0.8,
      ease: 'power3.out'
    });
  });

  window.gsap.from('.magazine-carousel', {
    scrollTrigger: { trigger: '.magazine-carousel', start: 'top 88%' },
    y: 50,
    opacity: 0,
    duration: 1,
    ease: 'power3.out'
  });
}

const spotlightCards = document.querySelectorAll('.card');
spotlightCards.forEach((card) => {
  let cardFrame = 0;
  let localX = 50;
  let localY = 50;
  card.addEventListener('pointermove', (event) => {
    if (!canHover) return;
    const rect = card.getBoundingClientRect();
    localX = ((event.clientX - rect.left) / rect.width) * 100;
    localY = ((event.clientY - rect.top) / rect.height) * 100;
    if (!cardFrame) {
      cardFrame = requestAnimationFrame(() => {
        card.style.setProperty('--mx', `${localX}%`);
        card.style.setProperty('--my', `${localY}%`);
        cardFrame = 0;
      });
    }
  }, { passive: true });
});

async function initStage() {
  const canvas = document.querySelector('#stage-canvas');
  const wrapper = document.querySelector('[data-stage]');
  if (!canvas || !wrapper || prefersReducedMotion || isMobile) {
    wrapper?.classList.add('is-static');
    return;
  }

  let THREE;
  try {
    THREE = await import('https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js');
  } catch (error) {
    wrapper.classList.add('is-static');
    return;
  }

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(42, 1, 0.1, 100);
  camera.position.set(0, 0.2, 5.2);

  const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.8));

  const geometry = new THREE.IcosahedronGeometry(1.35, 2);
  const material = new THREE.MeshStandardMaterial({
    color: new THREE.Color(0xff9500),
    metalness: 0.62,
    roughness: 0.28,
    emissive: new THREE.Color(0x3a1d00),
    emissiveIntensity: 0.28,
    wireframe: false
  });
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  const wire = new THREE.Mesh(
    new THREE.IcosahedronGeometry(1.72, 1),
    new THREE.MeshBasicMaterial({ color: 0x5db7d6, wireframe: true, transparent: true, opacity: 0.22 })
  );
  scene.add(wire);

  scene.add(new THREE.AmbientLight(0xffffff, 0.75));
  const key = new THREE.PointLight(0xff9500, 2.4, 10);
  key.position.set(2.4, 2.2, 3);
  scene.add(key);
  const fill = new THREE.PointLight(0x5db7d6, 1.6, 10);
  fill.position.set(-2.6, -1.2, 2.4);
  scene.add(fill);

  let running = false;
  let raf = 0;

  function resize() {
    const rect = wrapper.getBoundingClientRect();
    const width = Math.max(1, rect.width);
    const height = Math.max(1, rect.height);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  }

  function render() {
    if (!running) return;
    mesh.rotation.x += 0.004;
    mesh.rotation.y += 0.007;
    wire.rotation.x -= 0.002;
    wire.rotation.y += 0.003;
    renderer.render(scene, camera);
    raf = requestAnimationFrame(render);
  }

  const observer = new IntersectionObserver((entries) => {
    const visible = entries.some((entry) => entry.isIntersecting);
    if (visible && !running) {
      running = true;
      resize();
      render();
    } else if (!visible && running) {
      running = false;
      cancelAnimationFrame(raf);
    }
  }, { threshold: 0.12 });

  observer.observe(wrapper);
  window.addEventListener('resize', resize, { passive: true });
}

initStage();

(function initOrbitCarousel() {
  const track = document.querySelector('[data-orbit-track]');
  if (!track) return;
  const cards = Array.from(track.querySelectorAll('.orbit-card'));

  const tabs = document.querySelectorAll('.orbit-tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('is-active'));
      tab.classList.add('is-active');
      const filter = tab.dataset.filter;
      cards.forEach(card => {
        if (filter === 'all' || card.dataset.cat === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
})();
