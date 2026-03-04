# 3D Sneaker Wheel Carousel ✨

Premium interactive 3D sneaker showcase with cinematic animations, smooth transitions, and glassmorphism design.

## ✨ Features

- 🎨 **Premium Off-White Design** - Sophisticated color palette (#FBFCF6 → #F0EEEA)
- 🎬 **Cinematic Intro Animation** - Stunning entry with interaction lock (3s)
- 🔄 **360° 3D Carousel** - Smooth 7-item wheel with depth perspective
- ⌨️ **Multiple Navigation** - Mouse drag, keyboard arrows, wheel scroll, click
- 📱 **Fully Responsive** - Works flawlessly on all devices
- ⚡ **Ultra Smooth Transitions** - Premium easing (0.55s with easeOutQuint)
- 🖼️ **High-Quality Rendering** - Anti-aliasing, zero pixelation
- 🎯 **7 Unique Sneakers** - Carefully curated collection with rich accent colors

## 🎮 Controls

- **Mouse**: Click and drag to rotate
- **Keyboard**: Arrow keys (← → ↑ ↓) to navigate
- **Wheel**: Scroll to move between items
- **Click**: Tap any card to select it

## 🛠️ Technologies

- Pure HTML5
- CSS3 (3D Transforms, Animations, Glassmorphism)
- Vanilla JavaScript (No frameworks)
- Google Fonts (Space Grotesk)

## 🚀 Getting Started

1. Clone this repository
2. Open `index.html` in your browser
3. Enjoy the experience!

```bash
git clone https://github.com/YOUR_USERNAME/3d-sneaker-carousel.git
cd 3d-sneaker-carousel
```

## 📂 Project Structure

```
work2/
├── index.html          # Main file (all-in-one: HTML, CSS, JS)
├── images/             # Sneaker images (7 PNG with transparency)
│   ├── sneaker_real_1-removebg-preview.png
│   ├── sneaker_real_2-removebg-preview.png
│   ├── sneaker_real_3-removebg-preview.png
│   ├── sneaker_real_5-removebg-preview.png
│   ├── sneaker_real_6-removebg-preview.png
│   ├── sneaker_real_11-removebg-preview.png
│   └── sneaker_real_12-removebg-preview.png
├── .gitignore
└── README.md
```

## 🎨 Customization

### Add Your Own Sneakers

Edit the `SNEAKERS` array in `index.html`:

```javascript
const SNEAKERS = [
  {
    name: 'Your Sneaker Name',
    shortDesc: 'Brief description',
    accent: '#COLOR_HEX', // Brand color
    image: 'images/your-image.png'
  },
  // ... more sneakers
];
```

### Adjust Animation Speed

```javascript
const FRICTION = 0.96;        // Smooth deceleration
const VELOCITY_STOP = 0.12;   // Stop threshold
const SENSITIVITY = 0.3;      // Drag responsiveness
const duration = 700;         // Click rotation speed (ms)
```

### Change Transition Duration

```css
/* Ultra-smooth card transitions */
transition: 
  opacity 0.55s cubic-bezier(0.25, 1, 0.5, 1),
  filter 0.55s cubic-bezier(0.25, 1, 0.5, 1);
```

## 🎯 Performance Optimizations

- ✅ **Hardware Acceleration** - `transform-style: preserve-3d`
- ✅ **Anti-Aliasing** - High-quality image rendering with optimal scaling
- ✅ **Smart Scaling** - Render large (150%), scale down to prevent pixelation
- ✅ **Efficient Updates** - Label updates only when active item changes
- ✅ **Interaction Lock** - Prevents glitches during cinematic intro (3000ms)
- ✅ **Optimized Transitions** - 0.55s duration with custom easing curves
- ✅ **Deep Contrast Colors** - Premium accent palette for light backgrounds

## 📝 Technical Highlights

### Cinematic Intro Animation
- Sneaker drops from sky with bounce effect
- Card rises from bottom
- Text reveals with staggered timing
- Label fades in with scale animation

### Smooth Transitions
- Premium easing: `cubic-bezier(0.25, 1, 0.5, 1)` for cards
- Click animation: `easeOutQuint` (700ms duration)
- Synchronized animations across all elements
- Staggered text reveal (150ms + 250ms delays)

### 3D Carousel Math
- 7 items × 51.4° spacing
- 650px radius (TRANSLATE_Z)
- 1600px perspective depth

## 🌟 Inspiration

This project draws inspiration from:
- Apple product showcases
- Awwwards winning websites
- Luxury brand e-commerce sites
- Nike & Adidas digital experiences

## 📄 License

MIT License - Feel free to use for personal or commercial projects

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 👨‍💻 Author

Created with ❤️ by [Your Name]

## 🙏 Credits

- Fonts: [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) by Google Fonts
- Images: Sneaker product photography

---

**Enjoy the smooth 3D carousel experience! ✨**
