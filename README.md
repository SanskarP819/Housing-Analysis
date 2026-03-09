# Housing Market Trends Analysis

This project analyzes housing market trends for ABC Real Estate using Tableau and a basic Flask web integration.

## Current Workbook Status
The current Tableau workbook (`Housing Analysis Dashboard.twbx`) includes:
- Price vs Bedrooms
- Bedroom Distribution
- Living Area vs Price
- Price by Location
- Grade vs Price

## Required Scenario Status
- Scenario 1 (Overall Data Overview): Pending in Tableau workbook
- Scenario 2 (Total Sales by Years Since Renovation): Pending in Tableau workbook
- Scenario 3 (House Age by Renovation Status): Pending in Tableau workbook
- Scenario 4 (House Age by Bathrooms/Bedrooms/Floors): Pending in Tableau workbook

Detailed tracking is available in `TASK_TRACKER.md`.

## Added Deliverables (Basic)
- Flask app for dashboard/story embedding: `app.py`
- Frontend template: `templates/index.html`
- Styling: `static/styles.css`
- Python dependencies: `requirements.txt`
- Storyboard and testing checklist: `STORYBOARD_AND_TESTING.md`
- Story narrative: `STORYBOARD.md`

## Run Flask App
1. Install dependencies:
	`pip install -r requirements.txt`
2. Set Tableau embed URL (PowerShell):
	`$env:TABLEAU_EMBED_URL="https://public.tableau.com/views/YourWorkbook/YourDashboard"`
3. Start app:
	`python app.py`
4. Open in browser:
	`http://127.0.0.1:5000`

## Tools Used
- Tableau
- Flask
- GitHub

