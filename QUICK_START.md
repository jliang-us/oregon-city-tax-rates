# Quick Start Guide

## ✅ Your Repository is Ready!

All files are committed and ready to push to GitHub.

## 🚀 Push to GitHub (3 Commands)

```bash
# 1. Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/oregon-city-tax-rates.git

# 2. Rename branch to main
git branch -M main

# 3. Push to GitHub
git push -u origin main
```

## 🌐 Share Your App

Once pushed, share this URL (replace YOUR_USERNAME):

```
https://marimo.io/p/@YOUR_USERNAME/oregon-city-tax-rates/explore_city_tax_data.py
```

**Example:** If your username is `jsmith`, the URL would be:
```
https://marimo.io/p/@jsmith/oregon-city-tax-rates/explore_city_tax_data.py
```

## 📝 After Pushing

1. **Update README Badge**: Edit `README.md` and replace `YOUR_USERNAME` with your actual GitHub username
2. **Test the Link**: Click your marimo.io link to verify it works
3. **Share**: Send the link to anyone who wants to see the data

## 🔍 Troubleshooting

### Error: "FileNotFoundError: /marimo/notebook.py"
- **Fix**: Make sure you're using `path=` parameter or the `@username/repo/file.py` format
- **Correct**: `https://marimo.io/p/@user/repo/explore_city_tax_data.py`
- **Wrong**: `https://marimo.io/run?repo=user/repo&file=explore_city_tax_data.py`

### Large File Warning
If GitHub warns about files over 50MB:
```bash
# Install Git LFS
git lfs install
git lfs track "*.xlsx"
git add .gitattributes
git commit -m "Add Git LFS for Excel files"
git push
```

### Repository Not Found
- Make sure the repository is **public** (marimo.io requires public repos)
- Check the repository name matches exactly

## 📚 More Options

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for:
- Hugging Face Spaces deployment
- Docker deployment
- Authentication options
- Advanced configuration
