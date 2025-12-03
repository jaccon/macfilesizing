# Homebrew Installation Guide

This guide explains how to publish and install `macFileSizing` via Homebrew.

## For Users

### Installation

```bash
brew tap jaccon/tap
brew install macfilesizing
```

### Usage

After installation, use the command:

```bash
macfilesizing --source /path/to/directory
macfilesizing --source ~/Documents --tree
macfilesizing --source ~/Downloads --tree --report ~/report.txt
```

## For Maintainers

### Steps to Publish to Homebrew

#### 1. Create a GitHub Release

First, create a release on GitHub:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Or create a release manually on GitHub at:
`https://github.com/jaccon/macFileSizing/releases/new`

#### 2. Calculate SHA256 of the Release

Download the tarball and calculate its SHA256:

```bash
curl -L https://github.com/jaccon/macFileSizing/archive/refs/tags/v1.0.0.tar.gz -o macFileSizing-1.0.0.tar.gz
shasum -a 256 macFileSizing-1.0.0.tar.gz
```

#### 3. Update the Formula

Edit `macfilesizing.rb` and replace `REPLACE_WITH_ACTUAL_SHA256` with the calculated SHA256.

#### 4. Create a Homebrew Tap Repository

Create a new repository on GitHub named `homebrew-tap`:

```bash
# Create the repository structure
mkdir homebrew-tap
cd homebrew-tap
git init

# Copy the formula
cp /path/to/macfilesizing.rb Formula/macfilesizing.rb

# Commit and push
git add .
git commit -m "Add macfilesizing formula"
git remote add origin https://github.com/jaccon/homebrew-tap.git
git push -u origin main
```

#### 5. Test the Formula

Test the formula locally:

```bash
brew tap jaccon/tap
brew install --build-from-source macfilesizing
brew test macfilesizing
```

#### 6. Users Can Now Install

Users can install with:

```bash
brew tap jaccon/tap
brew install macfilesizing
```

## Updating the Formula

When releasing a new version:

1. Create a new GitHub release with a new tag (e.g., v1.1.0)
2. Calculate the new SHA256
3. Update `macfilesizing.rb` with:
   - New version number
   - New URL
   - New SHA256
4. Commit and push to the homebrew-tap repository

```bash
cd homebrew-tap
# Edit Formula/macfilesizing.rb
git add Formula/macfilesizing.rb
git commit -m "Update macfilesizing to v1.1.0"
git push
```

Users can then upgrade:

```bash
brew update
brew upgrade macfilesizing
```

## Formula Structure

The `macfilesizing.rb` formula:
- Uses Python virtualenv for isolated installation
- Includes all Python dependencies (tqdm)
- Installs the command as `macfilesizing`
- Includes a basic test

## Troubleshooting

### Formula fails to install

```bash
brew install --verbose --debug macfilesizing
```

### Audit the formula

```bash
brew audit --strict macfilesizing
```

### Uninstall and reinstall

```bash
brew uninstall macfilesizing
brew install macfilesizing
```
