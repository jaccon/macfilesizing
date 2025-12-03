# Setup Instructions for Homebrew

Follow these steps to publish your package via Homebrew:

## Step 1: Create GitHub Release

First, commit and push all files to GitHub:

```bash
git add .
git commit -m "Prepare for Homebrew release v1.0.0"
git push origin main
```

Then create a release tag:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Or create the release manually on GitHub:
- Go to: https://github.com/jaccon/jcfilesizer/releases/new
- Tag version: `v1.0.0`
- Release title: `v1.0.0`
- Click "Publish release"

## Step 2: Calculate SHA256

After creating the release, calculate the SHA256 hash:

```bash
curl -L https://github.com/jaccon/jcfilesizer/archive/refs/tags/v1.0.0.tar.gz -o jcfilesizer-1.0.0.tar.gz
shasum -a 256 jcfilesizer-1.0.0.tar.gz
```

Copy the SHA256 hash output.

## Step 3: Update the Formula

Edit `macfilesizing.rb` and replace `REPLACE_WITH_ACTUAL_SHA256` with the SHA256 hash from Step 2.

## Step 4: Create homebrew-tap Repository

Create a new repository on GitHub named `homebrew-tap`:

1. Go to: https://github.com/new
2. Repository name: `homebrew-tap`
3. Description: "Homebrew tap for jaccon's formulae"
4. Public repository
5. Click "Create repository"

## Step 5: Initialize and Push the Tap

```bash
# Create temporary directory for the tap
mkdir ~/temp-homebrew-tap
cd ~/temp-homebrew-tap
git init
git branch -M main

# Create Formula directory
mkdir Formula

# Copy the formula
cp /Users/jaccon/Documents/Workspaces/macFileSizing/macfilesizing.rb Formula/

# Create README
cat > README.md << 'EOF'
# Homebrew Tap

## Installation

```bash
brew tap jaccon/tap
brew install macfilesizing
```

## Available Formulae

- **macfilesizing** - List files and directories sorted by size
EOF

# Commit and push
git add .
git commit -m "Add macfilesizing formula"
git remote add origin https://github.com/jaccon/homebrew-tap.git
git push -u origin main

# Cleanup
cd ..
rm -rf ~/temp-homebrew-tap
```

## Step 6: Test the Installation

```bash
brew tap jaccon/tap
brew install macfilesizing
```

## Step 7: Test the Command

```bash
macfilesizing --source ~/Documents
macfilesizing --help
```

## Troubleshooting

If you get errors, check:

1. **Repository exists**: https://github.com/jaccon/homebrew-tap
2. **Formula is correct**: Check Formula/macfilesizing.rb in the tap repo
3. **SHA256 is correct**: Recalculate if needed
4. **Release exists**: https://github.com/jaccon/jcfilesizer/releases/tag/v1.0.0

Debug with:
```bash
brew install --verbose --debug macfilesizing
```

## Quick Command Summary

```bash
# 1. Push main project
cd /Users/jaccon/Documents/Workspaces/macFileSizing
git add .
git commit -m "Prepare for Homebrew release v1.0.0"
git push origin main
git tag v1.0.0
git push origin v1.0.0

# 2. Calculate SHA256
curl -L https://github.com/jaccon/jcfilesizer/archive/refs/tags/v1.0.0.tar.gz -o jcfilesizer-1.0.0.tar.gz
shasum -a 256 jcfilesizer-1.0.0.tar.gz

# 3. Update macfilesizing.rb with the SHA256

# 4. Create and setup tap repository
# (Follow Step 5 commands above)

# 5. Install
brew tap jaccon/tap
brew install macfilesizing
```
