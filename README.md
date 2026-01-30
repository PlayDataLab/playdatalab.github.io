# PlayData

PlayData is a block-based programming environment for expressive data visualization

**PlayDataLab** is the official website and documentation hub for PlayData, a Scratch 3.0 modification designed to support middle and high school students make sense of data through creative programming and visualization.

🌐 **Visit the website:** [playdatalab.github.io](https://playdatalab.github.io)

🚀 **Try PlayData now:** [playdatalab.github.io/editor](https://playdatalab.github.io/editor)

---

## 🌍 Languages / Idiomas

This website is available in:
- **English** - [/en/](https://playdatalab.github.io/en/)
- **Português** - [/pt/](https://playdatalab.github.io/pt/)

The site automatically detects your browser language and redirects accordingly.

---

## 📖 About PlayData

PlayData was developed as a research project focused on creating new approaches for kids and youth to engage with data. The tool combines:

1. **New programming blocks** for importing, analyzing, and visualizing data
2. **Embedded data table** to view imported datasets
3. **Custom sprites and backgrounds** for data visualization projects
4. **Scratch-based interface** that makes data science accessible to everyone

### Key Features

- 📊 Import data from online spreadsheets or manually
- 🎨 Create diverse representations: animations, music, artwork, and traditional charts
- 🌐 Available in English, Portuguese, Japanese and Spanish
- 🆓 Free and web-based - no installation required
- 🎓 Designed for educational use

---

## 🚀 Quick Start

### For Users

Just visit [playdatalab.github.io](https://playdatalab.github.io) and click "Try it Now" to start using PlayData!

### For Developers

This site is built with Jekyll and hosted on GitHub Pages.

**Prerequisites:**
- Ruby (3.0+)
- Bundler
- Git

**Local development:**

```bash
# Clone the repository
git clone https://github.com/PlayDataLab/playdatalab.github.io.git
cd playdatalab.github.io

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000
```

---

## 🌐 Adding a New Language

To add support for a new language:

1. Create a new folder for the language code (e.g., `es/` for Spanish)
2. Copy pages from `en/` to the new folder
3. Translate content while keeping the same `ref:` values
4. Update `_config.yml` to include the new language
5. Add translations to `_data/i18n.yml`
6. Update navbar links in `_config.yml`

Example:

```yaml
# _config.yml
languages: ["en", "pt", "es"]

navbar-links-es:
  Pruébalo: "https://playdatalab.github.io/editor"
  Acerca de: "es/acerca-de"
```

---

## 📝 Adding Content

### Blog Posts

Create a new markdown file in `_posts/en/` or `_posts/pt/`:

```markdown
---
layout: post
title: "Your Title"
date: 2024-01-30
lang: en
ref: unique-post-id
tags: [data, visualization]
---

Your content here...
```

### Pages

Create a new markdown file in the language folder:

```markdown
---
layout: page
title: "Page Title"
lang: en
ref: page-id
---

Your content here...
```

**Important:** Always use the same `ref:` value for equivalent pages across languages!


---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- 🌍 **Translate** - Help us translate PlayData to more languages
- 📝 **Documentation** - Improve guides and tutorials
- 🐛 **Bug reports** - Found an issue? Let us know!
- 💡 **Feature suggestions** - Have ideas? We'd love to hear them!

### How to Contribute

1. Fork this repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

---


## 🙏 Acknowledgments

- Based on the [Beautiful Jekyll](https://github.com/daattali/beautiful-jekyll) theme by Dean Attali
- PlayData is built on [Scratch 3.0](https://scratch.mit.edu/)
- Developed as part of ongoing research in data literacy education

