# JSON Data Explorer

A simple command-line tool to explore and view JSON datasets.

## Overview

This project allows users to interactively select and view JSON data files containing different types of information such as albums, comments, posts, and users.

## Features

- Interactive menu to choose from available datasets
- View complete JSON data with formatted output
- Extract and display specific fields from the data
- User-friendly prompts for navigation

## Project Structure

```
/workspace
├── main.py          # Main application script
├── errors.py        # Error handling utilities
├── data/            # Directory containing JSON data files
│   ├── albums.json
│   ├── comments.json
│   ├── posts.json
│   └── users.json
└── README.md        # This file
```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Select a dataset from the menu options (1-4):
   - Albums
   - Comments
   - Posts
   - Users

3. View the complete dataset or choose to see specific fields

## Requirements

- Python 3.x
- No external dependencies required (uses standard library modules: `json`, `pathlib`)

## How It Works

1. The program presents a menu of available JSON datasets
2. User selects a dataset by entering the corresponding number
3. The selected JSON file is loaded from the `data/` directory
4. Data is displayed in a formatted manner
5. Optionally, users can request to see specific fields from the data
