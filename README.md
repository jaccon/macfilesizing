# macFileSizing

A Python script to list files and directories sorted by size (largest to smallest).

## Features

- 📊 Lists files and directories ranked by size
- 🌲 Tree mode for recursive scanning of subdirectories
- 📄 Export reports to file
- 📈 Progress bar with tqdm
- 💾 Human-readable size formatting (B, KB, MB, GB, TB)

## Requirements

- Python 3.6+
- tqdm

## Installation

### Option 1: Homebrew (Recommended for macOS)

Once the tap is available, install via Homebrew:

```bash
brew tap jaccon/tap
brew install macfilesizing
```

Then use the command directly:

```bash
macfilesizing --source /path/to/directory
```

### Option 2: pip install

Install using pip:

```bash
pip install git+https://github.com/jaccon/macFileSizing.git
```

Then use:

```bash
macfilesizing --source /path/to/directory
```

### Option 3: Manual Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/jaccon/macFileSizing.git
cd macFileSizing
pip install -r requirements.txt
```

Make the script executable (optional):

```bash
chmod +x macFileSizing.py
```

Run directly:

```bash
python3 macFileSizing.py --source /path/to/directory
```

## Usage

### Basic Usage

List files and directories in a specific path:

```bash
python3 macFileSizing.py --source /path/to/directory
```

### Tree Mode

Recursively scan all subdirectories and rank all items by size:

```bash
python3 macFileSizing.py --source /path/to/directory --tree
```

### Generate Report

Save the output to a report file:

```bash
python3 macFileSizing.py --source /path/to/directory --report ~/report.txt
```

### Combined Options

You can combine multiple flags:

```bash
python3 macFileSizing.py --source ~/Documents --tree --report ~/reports/docs_analysis.txt
```

## Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--source` | Yes | Path of the directory to be analyzed |
| `--tree` | No | Recursively scan all subdirectories and rank by size |
| `--report` | No | Path to save the report file |

## Examples

### Example 1: Analyze Downloads folder

```bash
python3 macFileSizing.py --source ~/Downloads
```

**Output:**
```
Analyzing directory: /Users/username/Downloads
Please wait, calculating sizes...

Type   Size         Name
--------------------------------------------------------------------------------
DIR    2.45 GB      large_project
FILE   856.32 MB    video.mp4
DIR    345.67 MB    documents
FILE   123.45 MB    archive.zip
--------------------------------------------------------------------------------
Total: 3.75 GB
Items found: 4
```

### Example 2: Recursive analysis with report

```bash
python3 macFileSizing.py --source ~/Documents --tree --report ~/size_report.txt
```

This will scan all files and directories recursively and save the results to `~/size_report.txt`.

### Example 3: Analyze current directory

```bash
python3 macFileSizing.py --source .
```

## Output Format

The script displays:

- **Type**: `FILE` or `DIR`
- **Size**: Human-readable size (automatically formatted)
- **Name/Path**: Item name (basic mode) or relative path (tree mode)
- **Total**: Sum of all items
- **Items found**: Count of items

## Report File Format

When using `--report`, the generated file includes:

```
File Sizing Report
Generated: 2025-12-03 14:30:45
================================================================================

Analyzing directory: /Users/username/Documents
Mode: Recursive (tree mode)
Please wait, calculating sizes...

Type   Size         Path
--------------------------------------------------------------------------------
DIR    2.45 GB      Projects/webapp
FILE   856.32 MB    Videos/presentation.mp4
...
--------------------------------------------------------------------------------
Total: 10.23 GB
Items found: 1523
```

## Tips

1. **Use tree mode for deep analysis**: `--tree` will scan all subdirectories
2. **Save large outputs**: Use `--report` when analyzing large directories
3. **Path shortcuts**: You can use `~` for home directory and `.` for current directory
4. **Permission errors**: The script will skip files/directories it cannot access

## Troubleshooting

### Permission Denied

If you encounter permission errors:
- Run with appropriate permissions
- The script will automatically skip inaccessible items

### tqdm not found

Install the required package:
```bash
pip install tqdm
```

### Report directory doesn't exist

The script automatically creates the necessary directories for the report file.

## License

Free to use and modify.
