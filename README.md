# HRL Universal Ecosystem Sync & Rollout Engine (`hrl-sync`)

Automated one-command synchronization, validation, and dual-branch deployment toolchain for all HRL International repositories, documentation, patents, and web portals.

**Author**: Pavan Kumar Sadashiv (Founder & Managing Director, HRL International Private Limited)

---

## ⚡ The Single Universal Rollout Command

Whenever you update a feature, patent, or platform in any repository, run this single command to validate, synchronize cross-links, commit, and deploy across all repositories and GitHub Pages:

```bash
# Execute universal rollout across all HRL projects
python3 -m hrl_sync.cli rollout -m "feat: updated new feature across ecosystem"
```
Or use the direct launcher:
```bash
./hrl-sync -m "feat: updated new feature across ecosystem"
```

---

## 📦 What the Rollout Command Executes Automatically:
1. **Validates SEO & Schema**: Audits JSON-LD Knowledge Graph on `hrl-brand-seo`.
2. **Runs Language Test Suite**: Executes 100% unit tests & typechecks on `hrl-lang`.
3. **Synchronizes Cross-References**: Ensures patents, links, and banners match across all sites.
4. **Enforces Zero-Emoji Policy**: Guarantees pure, professional Apple minimalist typography.
5. **Performs Dual-Branch Git Push**: Pushes to both `main` and `gh-pages` across all active projects.
6. **Emits Live Directory**: Prints confirmed live production URLs.

---

## 🌐 Managed Ecosystem Repositories:
- `hrl-international-website-`: Corporate Portal (`hrlpavan.github.io/hrl-international-website-/`)
- `hrl-lang`: Domain-Specific Language for LLMs (`github.com/hrlpavan/hrl-lang`)
- `hrl-project-extreme`: Autonomous Spatial Physics Engine (`hrlpavan.github.io/hrl-project-extreme/`)
- `omnitransform-ai-resources`: Central Government IPA Platform (`hrlpavan.github.io/omnitransform-ai-resources/`)
- `hrlpavan`: GitHub Executive Profile (`github.com/hrlpavan`)
