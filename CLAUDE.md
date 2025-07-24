# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML GitHub Pages site for "FIRE族" (FIRE Tribe), a Chinese community focused on FIRE (Financial Independence, Retire Early) philosophy. The site serves as a landing page displaying QR codes to direct users to the community, with a multi-channel tracking system.

## Architecture

**Static Site Structure**: Pure HTML/CSS/JavaScript with no build process or framework dependencies. Files are served directly by GitHub Pages.

**Multi-Channel System**: The site has multiple entry points for channel tracking:
- Main page at `/` with primary QR code
- Channel pages at `/pages/channels/1/`, `/pages/channels/2/`, `/pages/channels/3/` with identical content but different QR codes
- Generated using `tools/scripts/addChannel.py` script

**Domain Configuration**: Custom domain `fire-zu.cn` configured via CNAME file.

## Directory Structure

```
/
├── index.html                    # Main landing page
├── CNAME, site.webmanifest      # Configuration files
├── assets/                       # Static assets
│   ├── css/styles.css           # Global CSS styles
│   ├── js/                      # JavaScript files (empty)
│   └── images/                  # All images and icons
│       ├── qrcode_for_fire-zu/  # QR code images
│       └── favicon files
├── pages/channels/              # Channel pages (actual files)
│   ├── 1/index.html
│   ├── 2/index.html
│   └── 3/index.html
├── tools/                       # Development tools
│   ├── n8n/                    # N8N financial data tool
│   │   └── fetch-financial-data/
│   └── scripts/                 # Utility scripts
│       └── addChannel.py
└── .gitignore, CLAUDE.md       # Project files
```

## Key Components

### Core Files
- `index.html` - Main landing page
- `assets/css/styles.css` - Global CSS styles shared across all pages
- `site.webmanifest` - PWA manifest for mobile app-like experience
- `tools/scripts/addChannel.py` - Python utility to generate new channel pages

### N8N Financial Data Tool
Located at `/tools/n8n/fetch-financial-data/`:
- Password-protected interface (password: "n8n-admin")
- Fetches stock data from external API at `n8n.backend.fire-zu.cn:5678`
- Downloads JSON files with financial data
- Uses localStorage for form persistence

### Assets Organization
- CSS files in `/assets/css/`
- Images in `/assets/images/`
- QR codes in `/assets/images/qrcode_for_fire-zu/`
- Favicon files and web manifest icons in `/assets/images/`

## Development Workflow

**No Build Process**: Edit HTML/CSS files directly and test by opening in browser.

**Adding New Channels**: 
1. Navigate to `tools/scripts/` directory
2. Run `python addChannel.py` to generate new numbered channel directories in `pages/channels/`
3. Update QR codes to point to new URLs: `/pages/channels/X/`

**Deployment**: Push to main branch - GitHub Pages automatically serves the files with no build step required.

**Clean URL Structure**: All pages use their actual paths without symlinks for better maintainability.

## Configuration

- **Custom Domain**: Configured via CNAME file pointing to `fire-zu.cn`
- **PWA Support**: Web manifest enables mobile app-like installation
- **SEO**: Includes Baidu site verification meta tag for Chinese search optimization
- **Security**: N8N tool uses basic JavaScript password protection and token-based API authentication
- **Path Structure**: All asset paths use `/assets/` prefix for proper organization