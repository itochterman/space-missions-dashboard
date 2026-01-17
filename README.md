# Space Missions Dashboard

An interactive dashboard for visualizing and analyzing historical space mission data from 1957 to present. Built as part of the Rely Health technical assessment.

**Author**: Isabella Tochterman  
**Date**: January 2026

## 🚀 Overview

This project provides a comprehensive analysis platform for space mission data, featuring:
- 8 programmatically testable functions for data analysis
- Interactive web dashboard with multiple visualizations
- Real-time filtering and data exploration capabilities
- Clean, production-ready code with extensive error handling

## 📋 Requirements

- Python 3.8+
- pandas
- streamlit
- plotly

## 🔧 Installation & Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd space-missions-dashboard
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Ensure data file is present**
- Place `space_missions.csv` in the project root directory
- The CSV should contain columns: Company, Location, Date, Time, Rocket, Mission, RocketStatus, Price, MissionStatus

4. **Run the dashboard**
```bash
streamlit run app.py
```

The dashboard will automatically open in your browser at `http://localhost:8501`

## 🏗️ Project Structure

```
space-missions-dashboard/
├── app.py                  # Streamlit dashboard application
├── functions.py            # Core analysis functions (programmatic grading)
├── requirements.txt        # Python dependencies
├── space_missions.csv      # Dataset (not included in repo)
└── README.md              # This file
```

## 📊 Visualization Rationale

### 1. Mission Success Rate Trends Over Time (Line Chart)

**Purpose**: Track how mission reliability has evolved across decades.

**Why this method?**
- Line charts excel at showing temporal trends and patterns
- Enables identification of pivotal moments in space technology
- Reveals correlation between historical events and success rates
- Useful for risk assessment and trend forecasting

**Key Insights**: This visualization reveals the Space Race era's trial-and-error phase, followed by steady improvement in the 1970s-80s as technology matured, and modern commercial space's consistently high success rates.

### 2. Top Space Organizations by Launch Volume (Horizontal Bar Chart)

**Purpose**: Compare launch activity across different space agencies and companies.

**Why this method?**
- Horizontal bars handle long organization names better than vertical
- Color gradient emphasizes relative scale differences
- Easy to rank and compare at a glance
- Natural reading flow from top to bottom

**Key Insights**: Clearly shows dominance of government programs (USSR, US agencies) in early space era vs. emergence of commercial players (SpaceX, Arianespace) in recent decades.

### 3. Overall Mission Outcome Distribution (Pie Chart)

**Purpose**: Visualize the proportion of different mission outcomes.

**Why this method?**
- Pie charts effectively communicate part-to-whole relationships
- Immediate understanding of overall reliability
- Color coding makes status categories instantly recognizable
- Important for stakeholder communication about risk

**Key Insights**: Provides a clear overview of mission reliability—critical for insurance underwriters, investors, and safety regulators evaluating the space industry.

### 4. Global Launch Activity Over Time (Area Chart)

**Purpose**: Show volume of space launches across history.

**Why this method?**
- Area charts emphasize volume and magnitude changes
- Visual "weight" of the fill conveys activity intensity
- Effective for showing boom/bust cycles in the industry
- Complements the success rate trend by adding volume context

**Key Insights**: Reveals the intense Space Race peak (1960s-70s), Cold War decline, and the dramatic resurgence driven by commercial spaceflight and small satellite markets.

## 🔍 Core Functions

All functions follow exact specifications from the assessment requirements:

### `getMissionCountByCompany(companyName: str) -> int`
Returns total number of missions for a given company.

### `getSuccessRate(companyName: str) -> float`
Calculates success rate percentage (0-100, 2 decimal places).

### `getMissionsByDateRange(startDate: str, endDate: str) -> list`
Returns mission names within date range, sorted chronologically.

### `getTopCompaniesByMissionCount(n: int) -> list`
Returns top N companies as list of (name, count) tuples.

### `getMissionStatusCount() -> dict`
Returns count of missions for each status category.

### `getMissionsByYear(year: int) -> int`
Returns total missions launched in a specific year.

### `getMostUsedRocket() -> str`
Returns the most frequently used rocket name.

### `getAverageMissionsPerYear(startYear: int, endYear: int) -> float`
Calculates average missions per year over a range.

## 🧪 Testing Functions

Run the function tests directly:
```bash
python functions.py
```

This will execute basic tests on all 8 functions with sample data.

## 🎨 Dashboard Features

### Interactive Filters
- **Date Range Selector**: Filter missions by launch date
- **Company Multi-Select**: Focus on specific organizations
- **Mission Status Filter**: Analyze successes, failures, or specific outcomes

### Summary Statistics
Real-time metrics based on filtered data:
- Total missions count
- Overall success rate
- Number of unique companies
- Variety of rocket types

### Data Explorer
- Sortable, searchable data table
- Customizable column display
- CSV export functionality

## 💡 Design Decisions

### Technology Stack
- **Streamlit**: Chosen for rapid development, native interactivity, and clean UI without frontend code
- **Plotly**: Selected for professional, interactive visualizations with zoom, pan, and hover details
- **Pandas**: Industry-standard for data manipulation with excellent CSV handling

### Code Quality
- Type hints for all function signatures
- Comprehensive docstrings following Google style
- Extensive input validation and error handling
- Separation of concerns (data logic vs. presentation)
- Efficient data caching to improve performance

### User Experience
- Responsive layout that adapts to screen size
- Clear visual hierarchy with sections and dividers
- Intuitive filter controls in sidebar
- Download capability for filtered datasets
- Professional color scheme and styling

## 🚨 Error Handling

The application handles common edge cases:
- Missing or invalid CSV file
- Malformed date formats
- Empty company names
- Division by zero in success rate calculations
- Invalid function inputs (wrong types, negative values)
- Missing data in optional fields (Price, Time)

## 📈 Performance Considerations

- Data loading is cached using `@st.cache_data` decorator
- Filters are applied efficiently using pandas vectorized operations
- Chart rendering optimized by limiting default company selections
- Functions load data on-demand to avoid memory overhead

## 🔐 Healthcare Relevance

While this project analyzes space mission data, the skills demonstrated are directly applicable to healthcare AI integration:

1. **Data Quality & Validation**: Healthcare systems require rigorous input validation—demonstrated through comprehensive error handling in all functions.

2. **Regulatory Compliance**: Following exact specifications mirrors healthcare's need for precise adherence to HIPAA, HL7, and FDA guidelines.

3. **Stakeholder Communication**: Clear visualizations are essential for explaining AI model outputs to clinicians, administrators, and patients.

4. **System Integration**: The modular architecture (separate data layer and presentation layer) reflects best practices for integrating with existing EHR systems.

5. **Edge Case Handling**: Healthcare data is messy—the defensive programming approach used here is critical for production medical systems.

## 🙏 Acknowledgments

Dataset represents historical space launch data compiled from public sources. Dashboard built using open-source tools: Streamlit, Plotly, and Pandas.

## 📧 Contact

Isabella Tochterman  
[GitHub Profile](https://github.com/yourusername)  
[Portfolio](https://isabellatochterman.com)

---

*Built with ☕ and 🚀 in San Francisco*
