# 3D Sneaker Wheel Carousel

An Awwwards-level interactive 3D sneaker showcase with cinematic animations and smooth transitions.

![Preview](preview.png)

## ✨ Features

- 🎨 **Premium Light Design** - Clean, modern, elegant interface
- 🎬 **Cinematic Intro Animation** - Stunning entry reveal effect
- 🔄 **360° 3D Carousel** - Smooth rotating wheel with depth perspective
- ⌨️ **Multiple Navigation** - Mouse drag, keyboard arrows, wheel scroll, click
- 📱 **Fully Responsive** - Works on all devices
- ⚡ **Ultra Smooth Transitions** - Premium easing functions (1s duration)
- 🖼️ **High-Quality Rendering** - Anti-aliasing, no pixelation
- 🎯 **7 Unique Sneakers** - Carefully curated collection

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
├── index.html          # Main file (all-in-one)
├── images/             # Sneaker images (PNG with transparency)
│   ├── sneaker_real_1-removebg-preview.png
│   ├── sneaker_real_2-removebg-preview.png
│   ├── sneaker_real_3-removebg-preview.png
│   ├── sneaker_real_4-removebg-preview.png
│   ├── sneaker_real_5-removebg-preview.png
│   ├── sneaker_real_6-removebg-preview.png
│   └── sneaker_real_8-removebg-preview.png
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
// In JavaScript section
const FRICTION = 0.96;        // Drag smoothness (0.9-0.98)
const VELOCITY_STOP = 0.12;   // Stop threshold
const SENSITIVITY = 0.3;      // Drag sensitivity
```

### Change Transition Duration

```css
/* In CSS section */
transition: 
  transform 1s cubic-bezier(0.19, 1, 0.22, 1); /* Change 1s to your preference */
```

## 🎯 Performance Optimizations

- **Hardware Acceleration**: `transform-style: preserve-3d`
- **Anti-Aliasing**: High-quality image rendering
- **Scale Strategy**: Render large, scale down (prevents pixelation)
- **Efficient Updates**: Label updates only on active item change
- **Debounced Events**: Prevents excessive wheel/scroll triggers

## 📝 Technical Highlights

### Cinematic Intro Animation
- Sneaker drops from sky with bounce effect
- Card rises from bottom
- Text reveals with staggered timing
- Label fades in with scale animation

### Smooth Transitions
- Premium easing: `cubic-bezier(0.19, 1, 0.22, 1)`
- 1-second duration for all major transitions
- Synchronized animations across all elements

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
