Interactive dashboard for exploring historical space launch data (1957-present). Built for a technical assessment.

## Quick Start

```bash
# Install dependencies
pip install streamlit pandas plotly

# Run it
streamlit run app.py
```

Opens in the browser automatically at `localhost:8501`.

## Requirements

- Python 3.8+
- streamlit
- pandas  
- plotly

Can be installed with:
```bash
pip install -r requirements.txt
```

## What This Does

Analyzes ~4600 space missions with 8 programmatic functions and an interactive web dashboard. You can filter by date, company, mission status and see various charts/stats.

### The 8 Required Functions

All in `functions.py`:

1. `getMissionCountByCompany(companyName)` - count missions per company
2. `getSuccessRate(companyName)` - success rate % for a company  
3. `getMissionsByDateRange(start, end)` - list missions in date range
4. `getTopCompaniesByMissionCount(n)` - top N companies by launches
5. `getMissionStatusCount()` - breakdown of success/failure/etc
6. `getMissionsByYear(year)` - count for specific year
7. `getMostUsedRocket()` - most frequently used rocket
8. `getAverageMissionsPerYear(start, end)` - average over year range

### The Dashboard

Has 4 visualizations:
- **Success rate over time** - Shows how reliability improved from the 1950s to modern 95%+ success rates
- **Top companies** - Bar chart of who launches the most
- **Mission outcomes** - Pie chart showing overall success vs. failure breakdown
- **Launch activity** - Area chart of missions per year

Plus filters for date/company/status, summary stats, and a searchable data table.

## Why These Visualizations?

**Line chart for success rate**: Correlative, temporal trends are best shown with lines. You can clearly see technology improving over decades.

**Bar chart for companies**: Easy to compare and rank. Horizontal bars handle long company names better.Discrete data points.

**Pie chart for status**: Quick sense of overall reliability.

**Area chart for activity**: Shows volume/magnitude well. The "weight" of the filled area emphasizes busy vs quiet periods in space history.

I added the fourth one (wasn't required to have 4) because the data is interesting and it's cool to see the Space Race era vs the modern commercial space boom.

## Project Structure

Main files:
- `app.py` - Streamlit dashboard
- `functions.py` - The 8 main functions  
- `requirements.txt` - Dependencies
- `space_missions.csv` - Dataset (needs to be here)
- `README.md` - You are here

## Testing the Functions

```bash
python test_functions.py
```

Should output results for all 8 functions with sample data.

## Tech Stack Choices

**Streamlit** - Chose this over building a React app because I wanted to focus on the data analysis, not fighting with frontend frameworks. Plus it has interactive filters built-in.

**Plotly** - Better interactivity than matplotlib (hover, zoom, pan). Looks more professional.

**Pandas** - Industry standard for this kind of data manipulation. Great CSV support.

## Data File

You need `space_missions.csv` in the project root. A valid data table input will have have these columns:
- Company
- Location  
- Date (YYYY-MM-DD)
- Time (HH:MM:SS)
- Rocket
- Mission
- RocketStatus
- Price (optional/empty for many)
- MissionStatus

The full dataset has 4631 rows.

## Known Issues / Future Ideas

- The company filter defaults to only 5 companies for performance, more selection decreases performance
- Would be nice to add a map visualization showing launch sites geographically
- Could add cost analysis for missions that have price data
- Might add rocket family grouping, i.e by make/model

## Notes

Built with Python/Streamlit because it's fast to prototype and the interactivity is built in. The assessment required specific function signatures and return types which are all in `functions.py`.

The visualizations all update based on the filters, so you can filter specific time periods and/or companies.

---

Isabella Tochterman
January 2026