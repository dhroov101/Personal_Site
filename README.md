# Personal Portfolio

A clean developer portfolio inspired by Brittany Chiang's site.
Built with plain HTML, CSS, and vanilla JavaScript. No frameworks, no build step.

## File structure

```
portfolio/
├── index.html   ← All content lives here
├── style.css    ← All styles
├── script.js    ← Cursor glow + active nav logic
├── resume.pdf   ← Drop your CV here
└── images/      ← Add project screenshots here
```

## How to customize

### 1. Update your info — index.html
- Replace `Your Name` with your name (appears in `<h1>` and `<title>`)
- Replace `Frontend Developer` with your role
- Update the tagline and About section paragraphs
- Update social links (`href` on the `<a>` tags in `.socials`)
- Replace `mailto:you@example.com` with your email

### 2. Experience — index.html
Each job is a `.card` block. Duplicate or delete them as needed.
Update the date range, job title, company name and link, description, and tags.

### 3. Projects — index.html
Each project is a `.card.project-card` block.
- Replace the `.project-img-placeholder` div with an `<img>` tag:
  ```html
  <img src="images/project1.png" alt="Project screenshot" />
  ```
- Add your project screenshots to an `images/` folder.

### 4. Résumé
Drop your CV as `resume.pdf` in the root folder.
The "View Full Résumé" link already points to `resume.pdf`.

### 5. Colors & fonts — style.css
All colors are CSS variables at the top of `style.css` under `:root`.
Change `--teal` to any accent color you like, e.g. `#f97316` for orange.

---

## Deploy to GitHub Pages

1. Create a new GitHub repository (e.g. `yourusername.github.io`)
2. Push all files to the `main` branch
3. Go to **Settings → Pages → Source → Deploy from branch → main / root**
4. Your site will be live at `https://yourusername.github.io`

If you use a different repo name (e.g. `portfolio`), the site will be at
`https://yourusername.github.io/portfolio` — no other changes needed.
