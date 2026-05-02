# DESIGN.md

> 电影级多维视觉宇宙：以深蓝黑、冷雾空间、暖橙能量点和滚动叙事，呈现“AI 训练师 + 业余设计师”的 AI 作品、平面视觉、建模作品、经历与个人介绍。

## 1. Visual Theme & Atmosphere

**Style**: Cinematic Multiverse Portfolio / Dark AI Visual Archive  
**Keywords**: 深蓝黑、电影感、雾面空间、橙色能量点、3D 展台、作品星群、细线网格、AI 训练档案  
**Tone**: 专业、神秘、锋利、克制、沉浸 — NOT 可爱、糖果色、卡通、拥挤、普通模板感  
**Feel**: 像走进一座夜间开放的个人视觉实验馆，远处是 AI 模型的微光，近处是一组组被精准归档的作品样本。

**Interaction Tier**: L3 沉浸体验  
**Dependencies**: GSAP + ScrollTrigger + Three.js；Lenis 仅在 pin-scrub 确有必要时启用。

**Reference Direction**: 继承 Skydda 参考中的深色安全感、雾面大图、细线边框、橙色高亮与冷静留白；转译为个人作品档案与多维视觉表达，不直接复刻文案和布局。

## 2. Color Palette & Roles

```css
:root {
  --bg: #090b10;
  --bg-deep: #040609;
  --surface: #111318;
  --surface-alt: #15171d;
  --surface-elevated: #1b1e25;
  --surface-hover: #20242c;
  --glass: rgba(17, 19, 24, 0.72);
  --border: #2a2f38;
  --border-soft: rgba(255, 255, 255, 0.08);
  --border-hover: #ff9f1a;
  --text: #f4f1ea;
  --text-secondary: #b8bbc4;
  --text-tertiary: #7d838f;
  --text-inverse: #07080b;
  --accent: #ff9500;
  --accent-hover: #ffb13b;
  --accent-deep: #c76600;
  --accent-glow: rgba(255, 149, 0, 0.34);
  --cyan: #5db7d6;
  --violet: #8b7cff;
  --bg-rgb: 9, 11, 16;
  --surface-rgb: 17, 19, 24;
  --text-rgb: 244, 241, 234;
  --accent-rgb: 255, 149, 0;
  --cyan-rgb: 93, 183, 214;
  --violet-rgb: 139, 124, 255;
  --success: #61d394;
  --error: #ff6b6b;
  --warning: #ffb13b;
  --shadow-soft: 0 24px 80px rgba(0, 0, 0, 0.42);
  --shadow-accent: 0 0 36px rgba(var(--accent-rgb), 0.26);
}
```

**Color Rules:** 所有颜色必须通过 CSS 变量引用；橙色只用于 CTA、活跃态、作品焦点和能量点；同一屏最多一个强强调色；背景必须有冷雾、颗粒、细线或径向光，不要纯黑死板。

## 3. Typography Rules

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Sans+SC:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
:root {
  --font-sans: 'Noto Sans SC', 'Inter', system-ui, sans-serif;
  --font-display: 'Inter', 'Noto Sans SC', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', Consolas, monospace;
}
```

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|---|---|---:|---:|---:|---:|
| Hero H1 | Inter + Noto Sans SC | clamp(48px, 8vw, 116px) | 700 | .92 | -0.06em |
| Section H2 | Inter + Noto Sans SC | clamp(36px, 5vw, 72px) | 650 | 1.02 | -0.045em |
| H3 | Noto Sans SC + Inter | clamp(22px, 2.2vw, 34px) | 650 | 1.18 | -0.025em |
| Body | Noto Sans SC + Inter | clamp(15px, 1.1vw, 18px) | 400 | 1.75 | 0.02em |
| Label | JetBrains Mono | 11px-13px | 500 | 1.4 | 0.14em |
| Code | JetBrains Mono | 13px-15px | 500 | 1.65 | 0.01em |

**Typography Rules:** Hero 要像电影海报，标题大、紧、克制；中文正文行高 ≥ 1.7；标签、时间、技能、AI 数据说明用等宽字体；禁止 Comic Sans、Papyrus、Impact、默认宋体、过度圆润可爱字体。

**Text Decoration:** Hero 关键词可有轻微暖橙扫光；Section H2 使用 ScrollFloat / BlurText；Label 用橙色小方块和细线，不用 emoji。

## 4. Component Stylings

### Buttons

```css
.button { display:inline-flex; align-items:center; justify-content:center; min-height:46px; padding:0 22px; border:1px solid var(--text); border-radius:0; background:var(--text); color:var(--text-inverse); font:650 13px/1 var(--font-sans); text-decoration:none; cursor:pointer; transition:transform .22s ease, background .22s ease, color .22s ease, border-color .22s ease, box-shadow .22s ease; }
.button:hover { transform:translateY(-2px); border-color:var(--accent); background:var(--accent); color:var(--text-inverse); box-shadow:var(--shadow-accent); }
.button:active { transform:translateY(0) scale(.98); box-shadow:none; }
.button:focus-visible { outline:2px solid var(--accent); outline-offset:4px; }
.button:disabled, .button[aria-disabled='true'] { cursor:not-allowed; opacity:.42; transform:none; box-shadow:none; }
.button--ghost { border-color:var(--border); background:rgba(var(--surface-rgb), .22); color:var(--text); }
.button--ghost:hover { background:rgba(var(--accent-rgb), .10); color:var(--text); }
```

### Cards

```css
.card { position:relative; overflow:hidden; border:1px solid var(--border-soft); background:linear-gradient(180deg, rgba(var(--surface-rgb), .88), rgba(var(--surface-rgb), .58)); color:var(--text); transition:transform .26s ease, border-color .26s ease, box-shadow .26s ease; }
.card::before { content:''; position:absolute; inset:0; pointer-events:none; opacity:0; background:radial-gradient(circle at var(--mx, 50%) var(--my, 50%), rgba(var(--accent-rgb), .18), transparent 34%); transition:opacity .24s ease; }
.card:hover { transform:translateY(-6px); border-color:rgba(var(--accent-rgb), .58); box-shadow:var(--shadow-soft); }
.card:hover::before { opacity:1; }
.card:focus-within { border-color:var(--accent); box-shadow:0 0 0 1px rgba(var(--accent-rgb), .36), var(--shadow-soft); }
.card__media { width:100%; aspect-ratio:4/3; object-fit:cover; background:var(--surface-alt); }
.card__meta { font-family:var(--font-mono); color:var(--text-tertiary); font-size:12px; letter-spacing:.08em; text-transform:uppercase; }
```

### Navigation / Links / Badges

```css
.site-nav { position:fixed; inset:0 0 auto; z-index:100; display:flex; align-items:center; justify-content:space-between; height:68px; padding:0 clamp(20px, 4vw, 56px); border-bottom:1px solid transparent; background:linear-gradient(180deg, rgba(var(--bg-rgb), .74), rgba(var(--bg-rgb), 0)); color:var(--text); backdrop-filter:blur(10px); transition:height .24s ease, background .24s ease, border-color .24s ease; }
.site-nav.is-scrolled { height:58px; border-bottom-color:var(--border-soft); background:rgba(var(--bg-rgb), .78); }
.site-nav__link { color:var(--text-secondary); font-size:13px; text-decoration:none; transition:color .18s ease; }
.site-nav__link:hover, .site-nav__link:focus-visible { color:var(--text); outline-color:var(--accent); }
.text-link { color:var(--text); text-decoration:none; background:linear-gradient(90deg, var(--accent), var(--accent)) 0 100%/100% 1px no-repeat; transition:color .18s ease, background-size .18s ease; }
.text-link:hover { color:var(--accent-hover); background-size:100% 2px; }
.badge { display:inline-flex; align-items:center; gap:8px; min-height:30px; padding:0 12px; border:1px solid var(--border-soft); background:rgba(var(--surface-rgb), .44); color:var(--text-secondary); font:500 11px/1.4 var(--font-mono); letter-spacing:.12em; text-transform:uppercase; }
.badge::before { content:''; width:7px; height:7px; background:var(--accent); box-shadow:0 0 14px rgba(var(--accent-rgb), .58); }
```

### Work Gallery / Timeline

```css
.archive-grid { display:grid; grid-template-columns:repeat(12, minmax(0, 1fr)); gap:1px; border:1px solid var(--border-soft); background:var(--border-soft); }
.archive-item { min-height:clamp(240px, 34vw, 520px); grid-column:span 4; background:var(--surface); }
.archive-item--wide { grid-column:span 8; }
.archive-item--tall { min-height:clamp(420px, 52vw, 720px); }
.timeline-item { display:grid; grid-template-columns:minmax(120px, .28fr) 1fr; gap:clamp(24px, 5vw, 72px); padding:clamp(28px, 5vw, 64px) 0; border-bottom:1px solid var(--border-soft); }
.timeline-item__date { color:var(--accent); font:500 12px/1.4 var(--font-mono); letter-spacing:.12em; }
```

## 5. Layout Principles

**Container:** max width `min(1440px, calc(100vw - 48px))`；窄文本 `min(820px, calc(100vw - 40px))`。  
**Spacing:** Hero `100svh`；section `clamp(88px, 13vw, 188px) 0`；gap `clamp(20px, 3vw, 48px)`；基于 8px 节奏。  
**首页结构:** Hero 个人宣言 → AI 训练作品/方法 → 多维视觉作品归档 → 3D/建模舞台 → 经历时间线 → 关于我 → 联系方式。

```css
.container { width:min(1440px, calc(100vw - 48px)); margin-inline:auto; }
.section { position:relative; padding:clamp(88px, 13vw, 188px) 0; }
.grid-12 { display:grid; grid-template-columns:repeat(12, minmax(0, 1fr)); gap:clamp(16px, 2vw, 28px); }
.grid-asymmetric { display:grid; grid-template-columns:minmax(0, .88fr) minmax(0, 1.12fr); gap:clamp(40px, 7vw, 112px); align-items:center; }
.full-bleed { width:100vw; margin-left:calc(50% - 50vw); }
```

## 6. Depth & Elevation

| Level | Treatment | Use |
|---|---|---|
| Flat | 细线边框，无阴影 | 文本区、时间线 |
| Subtle | 渐变表面 + 轻阴影 | 普通作品卡 |
| Elevated | `var(--shadow-soft)` + 暖橙边缘光 | 聚焦作品、CTA |
| Cinematic | 冷色径向雾 + 暖色点光 + 3D 透视 | Hero、建模舞台 |
| Archive Glass | `backdrop-filter: blur(10px)` | 导航、悬浮信息 |

**Rules:** backdrop-filter ≤ 14px；移动元素禁止大半径 blur；每屏只有一个主发光点。

## 7. Animation & Interaction

**Motion Philosophy**: 少数强场景 + 精确节奏，每 1-2 屏有一个 signature moment。  
**Tier**: L3

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js"></script>
<script type="module" src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js"></script>
```

**Required Signature Moments:** Hero H1 SplitText 解码入场；Hero 卡片星群；首次滑动卡片汇聚；Section H2 ScrollFloat；Label ScrambleText；CTA Magnet / ClickSpark；作品区 MagicBento + TiltedCard；建模区单个 Three.js 3D stage。

```css
.reveal { opacity:0; transform:translateY(28px); }
.reveal.is-visible { opacity:1; transform:translateY(0); transition:opacity .7s ease, transform .9s cubic-bezier(.16, 1, .3, 1); }
@keyframes heroWordIn { from { opacity:0; transform:translateY(32px) scale(.98); filter:blur(10px); } to { opacity:1; transform:translateY(0) scale(1); filter:blur(0); } }
.hero-word { display:inline-block; animation:heroWordIn .9s cubic-bezier(.16, 1, .3, 1) both; animation-delay:calc(var(--i) * 70ms); }
@media (hover:hover) { .magnet-target:hover { transform:translateY(-2px) scale(1.015); } .tilt-card { transform-style:preserve-3d; transition:transform .26s ease, border-color .26s ease; } }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration:.01ms !important; animation-iteration-count:1 !important; scroll-behavior:auto !important; transition-duration:.01ms !important; } .reveal { opacity:1; transform:none; } .star-card, .tilt-card, .pin-scene { transform:none !important; filter:none !important; } }
```

```js
gsap.registerPlugin(ScrollTrigger);
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReducedMotion) {
  gsap.utils.toArray('.reveal').forEach((el) => {
    ScrollTrigger.create({ trigger: el, start: 'top 82%', onEnter: () => el.classList.add('is-visible') });
  });
  gsap.timeline({ scrollTrigger: { trigger: '.hero-constellation', start: 'top top', end: 'bottom top', scrub: .8 } })
    .to('.star-card', { x: 0, y: 0, rotateX: 0, rotateY: 0, rotateZ: 0, scale: .86, opacity: 0, stagger: { amount: .45, from: 'random' }, ease: 'power2.inOut' })
    .from('.ai-method-panel', { scale: .78, opacity: 0, y: 80, ease: 'power3.out' }, '-=.25');
}
```

**Performance:** WebGL ≤ 1 个，pin ≤ 2 个；pointermove 必须 rAF 节流；WebGL 不可见时用 IntersectionObserver 暂停；移动端 3D 降级为 poster。

## 8. Do's and Don'ts

### Do
- 用深蓝黑、冷雾、细线、暖橙高亮建立个人品牌。
- 首页必须有 Hero、首次滑动、作品展示区 3 个视觉爆点。
- AI 训练师身份转译成数据标注、模型反馈、样本迭代、提示词实验。
- 设计师身份转译成平面档案、建模切片、视觉实验、过程记录。
- 作品优先真实素材；没有素材时用明确待替换视觉占位图。
- 每个可交互元素必须有 hover、focus、active 或 disabled 状态。
- 移动端保留叙事顺序，但减少 pin、3D 和鼠标跟随。
- 所有动效必须有 reduced-motion 降级。

### Don't
- ❌ 不要做成普通简历模板或普通三列作品集。
- ❌ 不要大面积使用亮橙。
- ❌ 不要使用 emoji 作为主要图标或装饰。
- ❌ 不要使用纯黑纯白硬切背景。
- ❌ 不要堆叠 3 个以上重型动效库。
- ❌ 不要在移动元素上使用高半径 `filter: blur()`。
- ❌ 不要让 WebGL 常驻渲染。
- ❌ 不要所有作品卡等大等距排列。
- ❌ 不要默认加入中英切换器。
- ❌ 不要用 Lorem Ipsum。

## 9. Responsive Behavior

| Name | Width | Key Changes |
|---|---:|---|
| Desktop | >1180px | 12 栏、Hero 星群、pin-swap、WebGL 可启用 |
| Laptop | 900-1180px | 降低卡片数量，作品区 8 栏 |
| Tablet | 640-899px | pin-swap 改纵向，3D stage 缩小或 poster 化 |
| Mobile | <640px | 单列，禁用复杂 pointermove，触摸目标 ≥ 44px |

```css
@media (max-width:1180px) { .archive-item, .archive-item--wide { grid-column:span 6; } .grid-asymmetric { grid-template-columns:1fr; } }
@media (max-width:899px) { .container { width:min(100% - 40px, 760px); } .site-nav__links { display:none; } .pin-swap { height:auto; } .pin-swap-inner { position:relative; height:auto; display:grid; grid-template-columns:1fr; } .pin-scene { position:relative; opacity:1; } }
@media (max-width:640px) { .container { width:min(100% - 32px, 560px); } .section { padding:76px 0; } .hero { min-height:92svh; } .archive-grid { display:block; border:0; background:transparent; } .archive-item { min-height:auto; margin-bottom:16px; } .timeline-item { grid-template-columns:1fr; gap:12px; } .button { width:100%; min-height:48px; } }
```
