# Notes Manager

A beautiful, responsive, feature-rich Notes application built with Django and Bootstrap.

## Features
- **Full CRUD Operations**: Create, Read, Update, and Delete your personal notes.
- **Color Tags**: Organize notes with custom tags and intelligently assigned badge colors.
- **Timestamps**: Automatically track note creation and modification dates.
- **Edit & Delete Confirmation**: Prevent accidental changes with secure confirmations.
- **Smart Pagination**: Browse through notes efficiently with compactly elided paginated views.
- **CSV Export**: Instantly export all your tracked notes to a CSV file.

## Tech Stack
- **Backend**: Python, Django
- **Database**: SQLite
- **Frontend**: Bootstrap 5 (HTML/CSS/JS)

## How to use

Here's a quick overview of what the application looks like:

### 1. Browse All Notes
Browse your notes with pagination, search functionalities, and dynamic color tags visually categorizing your workflow.
![List View](screenshots/01_list_view.png)

### 2. Create / Edit Note
Use intelligent tag reuse and visualize your card's top-border color choices in real-time.
![Edit Note](screenshots/02_edit_note.png)

### 3. Export Data
Easily filter by specific matching tags and export your data directly to CSV with one click.
![Export Data](screenshots/03_export_dashboard.png)

*(Note: Replace the placeholder files in the `screenshots/` directory with your real snippets before publishing this to your portfolio).*

## Quick Setup and Run

Follow these steps to get the project running on your local machine:

1. **Create and activate a virtual environment:**
   ```bash
   # Create a virtual environment named .venv
   python -m venv .venv
   
   # Activate the virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

After running these commands, the application should be accessible at `http://127.0.0.1:8000/`.
