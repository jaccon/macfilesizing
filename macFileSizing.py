#!/usr/bin/env python3

import os
import argparse
from pathlib import Path
from tqdm import tqdm
from datetime import datetime


def getSize(path):
    total = 0
    try:
        if os.path.isfile(path):
            total = os.path.getsize(path)
        elif os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total += os.path.getsize(filepath)
                    except (OSError, PermissionError):
                        pass
    except (OSError, PermissionError):
        pass
    return total


def formatSize(bytesSize):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytesSize < 1024.0:
            return f"{bytesSize:.2f} {unit}"
        bytesSize /= 1024.0
    return f"{bytesSize:.2f} PB"


def listItemsBySize(sourcePath, treeMode=False, reportPath=None):
    if not os.path.exists(sourcePath):
        print(f"Error: The path '{sourcePath}' does not exist.")
        return
    
    if not os.path.isdir(sourcePath):
        print(f"Error: '{sourcePath}' is not a directory.")
        return
    
    output = []
    
    header = f"\nAnalyzing directory: {sourcePath}"
    print(header)
    output.append(header)
    
    if treeMode:
        mode_msg = "Mode: Recursive (tree mode)"
        print(mode_msg)
        output.append(mode_msg)
    
    wait_msg = "Please wait, calculating sizes...\n"
    print(wait_msg)
    output.append(wait_msg)
    
    items = []
    
    try:
        if treeMode:
            allItems = []
            for root, dirs, files in os.walk(sourcePath):
                for d in dirs:
                    fullPath = os.path.join(root, d)
                    relativePath = os.path.relpath(fullPath, sourcePath)
                    allItems.append((relativePath, fullPath, "DIR"))
                for f in files:
                    fullPath = os.path.join(root, f)
                    relativePath = os.path.relpath(fullPath, sourcePath)
                    allItems.append((relativePath, fullPath, "FILE"))
            
            for relativePath, fullPath, itemType in tqdm(allItems, desc="Calculating sizes", unit="item"):
                size = getSize(fullPath)
                items.append((relativePath, fullPath, size, itemType))
        else:
            itemsList = os.listdir(sourcePath)
            for item in tqdm(itemsList, desc="Calculating sizes", unit="item"):
                itemPath = os.path.join(sourcePath, item)
                size = getSize(itemPath)
                itemType = "DIR" if os.path.isdir(itemPath) else "FILE"
                items.append((item, itemPath, size, itemType))
    except PermissionError:
        print(f"Error: Permission denied to access '{sourcePath}'")
        return
    
    items.sort(key=lambda x: x[2], reverse=True)
    
    header_line = f"\n{'Type':<6} {'Size':<12} {'Path' if treeMode else 'Name'}"
    separator = "-" * 80
    
    print(header_line)
    print(separator)
    output.append(header_line)
    output.append(separator)
    
    for itemName, itemPath, size, itemType in items:
        formattedSize = formatSize(size)
        line = f"{itemType:<6} {formattedSize:<12} {itemName}"
        print(line)
        output.append(line)
    
    totalSize = sum(item[2] for item in items)
    print(separator)
    output.append(separator)
    
    total_line = f"Total: {formatSize(totalSize)}"
    items_line = f"Items found: {len(items)}"
    
    print(total_line)
    print(items_line)
    output.append(total_line)
    output.append(items_line)
    
    if reportPath:
        try:
            reportPath = os.path.expanduser(reportPath)
            reportPath = os.path.abspath(reportPath)
            
            os.makedirs(os.path.dirname(reportPath), exist_ok=True)
            
            with open(reportPath, 'w', encoding='utf-8') as f:
                f.write(f"File Sizing Report\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 80 + "\n")
                f.write("\n".join(output))
            
            print(f"\nReport saved to: {reportPath}")
        except Exception as e:
            print(f"\nError saving report: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='List files and directories sorted by size (largest to smallest)'
    )
    parser.add_argument(
        '--source',
        type=str,
        required=True,
        help='Path of the directory to be analyzed'
    )
    parser.add_argument(
        '--tree',
        action='store_true',
        help='Recursively scan all subdirectories and rank by size'
    )
    parser.add_argument(
        '--report',
        type=str,
        help='Path to save the report file (e.g., ~/report.txt)'
    )
    
    args = parser.parse_args()
    
    sourcePath = os.path.expanduser(args.source)
    sourcePath = os.path.abspath(sourcePath)
    
    listItemsBySize(sourcePath, treeMode=args.tree, reportPath=args.report)


if __name__ == '__main__':
    main()
