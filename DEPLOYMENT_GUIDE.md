# GitHub Repository Deployment Guide

Your local git repository is ready! Now you need to create a GitHub repository and push your code.

## Step 1: Create GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Fill in the details:
   - **Repository name**: `oregon-city-tax-rates` (or your preferred name)
   - **Description**: "Interactive marimo app displaying Oregon city property tax rates and 2024 population data"
   - **Visibility**: Public (required for marimo.io integration)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

## Step 2: Push Your Code to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
# Set the remote repository
git remote add origin https://github.com/YOUR_USERNAME/oregon-city-tax-rates.git

# Rename branch to main (if you prefer)
git branch -M main

# Push your code
git push -u origin main
```

**Replace `YOUR_USERNAME`** with your actual GitHub username!

## Step 3: Deploy with marimo.io

Once your code is on GitHub, you can use marimo's GitHub integration:

### Option A: Direct marimo.io Link

Share this URL format with anyone:
```
https://marimo.io/p/@YOUR_USERNAME/oregon-city-tax-rates/explore_city_tax_data.py
```

**Example:** If your username is `johnsmith`:
```
https://marimo.io/p/@johnsmith/oregon-city-tax-rates/explore_city_tax_data.py
```

**Alternative format:**
```
https://marimo.io/run?repo=YOUR_USERNAME/oregon-city-tax-rates&path=explore_city_tax_data.py
```

Note: The parameter is `path=` not `file=`

### Option B: Add marimo Badge to README

Add this badge to your README.md to make it easy for visitors to run your app:

```markdown
[![Run with marimo](https://marimo.io/shield.svg)](https://marimo.io/p/@YOUR_USERNAME/oregon-city-tax-rates/explore_city_tax_data.py)
```

### How marimo.io Works

When someone clicks the link:
1. marimo.io clones your GitHub repository
2. Installs dependencies from the script header (pandas, numpy, etc.)
3. Runs the notebook in a sandboxed environment
4. Displays the interactive app in their browser

**Benefits:**
- ✅ Completely free
- ✅ No server setup needed
- ✅ Updates automatically when you push to GitHub
- ✅ Runs in user's browser (WASM)
- ✅ Shareable link

## Alternative: Using GitHub CLI (if you have it)

If you have GitHub CLI installed (`gh`), you can do this in one command:

```bash
gh repo create oregon-city-tax-rates --public --source=. --remote=origin --push
```

## Verifying Your Setup

After pushing, check that these files are visible on GitHub:
- ✅ explore_city_tax_data.py
- ✅ FY 2024-25 Property Tax Statistics Supplement.xlsx
- ✅ PSU_2024_Certified_Population_Estimates.xlsx
- ✅ Dockerfile
- ✅ README.md
- ✅ .gitignore

## Making Updates

When you make changes to your notebook:

```bash
git add explore_city_tax_data.py
git commit -m "docs: update analysis"
git push
```

The marimo.io link will automatically use the latest version!

## Troubleshooting

### Large File Warning
If GitHub warns about large files (>50MB), the Excel files might be too big. Options:
1. Use Git LFS: `git lfs install && git lfs track "*.xlsx"`
2. Host Excel files elsewhere and load via URL in the notebook
3. Convert Excel to CSV/JSON and embed in notebook

### Private Repository
If you created a private repo by mistake:
1. Go to repository Settings on GitHub
2. Scroll to "Danger Zone"
3. Click "Change visibility" → Make public

Note: marimo.io only works with public repositories.

## Next Steps

Once on GitHub, you can also:
- Deploy to Hugging Face Spaces (see README.md)
- Deploy with Docker to any cloud provider
- Set up GitHub Actions for automated testing
- Add more datasets or visualizations

---

**Your current status:**
- ✅ Git repository initialized
- ✅ All files committed
- ⏳ Waiting for GitHub repository creation and push

Run the commands from Step 2 above to push to GitHub!
