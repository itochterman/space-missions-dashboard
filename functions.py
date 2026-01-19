import pandas as pd
from typing import List, Tuple, Dict
from datetime import datetime
from functools import lru_cache

# Load space missions data from CSV file. Cache after first call for performance. 
@lru_cache(maxsize=1)
def load_data() -> pd.DataFrame:
    try:
        df = pd.read_csv('space_missions.csv')
        # Validate required columns exist
        required_columns = ['Company', 'Location', 'Date', 'Time', 'Rocket', 
                          'Mission', 'RocketStatus', 'Price', 'MissionStatus']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            raise ValueError(f"CSV is missing required columns: {', '.join(missing_columns)}")
        
        # Convert Date column to datetime for proper sorting
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        return df
    except FileNotFoundError:
        raise FileNotFoundError("space_missions.csv not found in current directory")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")


# Returns the total number of missions for a given company.
def getMissionCountByCompany(companyName: str) -> int:
    if not isinstance(companyName, str):
        return 0
    
    df = load_data()
    count = len(df[df['Company'] == companyName])
    return count


# Calculates the success rate for a given company as a percentage.

def getSuccessRate(companyName: str) -> float:
    if not isinstance(companyName, str):
        return 0.0
    
    df = load_data()
    company_missions = df[df['Company'] == companyName]
    
    if len(company_missions) == 0:
        return 0.0
    
    success_count = len(company_missions[company_missions['MissionStatus'] == 'Success'])
    success_rate = (success_count / len(company_missions)) * 100
    
    return round(success_rate, 2)

# Returns a list of all mission names launched between startDate and endDate (inclusive).
def getMissionsByDateRange(startDate: str, endDate: str) -> List[str]:
    try:
        start = pd.to_datetime(startDate)
        end = pd.to_datetime(endDate)
    except:
        return []
    
    df = load_data()
    
    # Filter by date range
    mask = (df['Date'] >= start) & (df['Date'] <= end)
    filtered_df = df[mask].copy()
    
    # Sort by date and return mission names
    filtered_df = filtered_df.sort_values('Date')
    missions = filtered_df['Mission'].tolist()
    
    return missions

# Returns the top N companies ranked by total number of missions.
def getTopCompaniesByMissionCount(n: int) -> List[Tuple[str, int]]:
    if not isinstance(n, int) or n <= 0:
        return []
    
    df = load_data()
    
    # Count missions per company
    company_counts = df['Company'].value_counts().reset_index()
    company_counts.columns = ['Company', 'Count']
    
    # Sort by count (descending) and company name (ascending) for ties
    company_counts = company_counts.sort_values(
        by=['Count', 'Company'], 
        ascending=[False, True]
    )
    
    # Return top n as list of tuples
    top_n = company_counts.head(n)
    result = list(zip(top_n['Company'], top_n['Count']))
    
    return result

# Returns the count of missions for each mission status.

def getMissionStatusCount() -> Dict[str, int]:
    df = load_data()
    
    # Count each status
    status_counts = df['MissionStatus'].value_counts().to_dict()
    
    # Ensure all expected statuses are present (even if count is 0)
    expected_statuses = ["Success", "Failure", "Partial Failure", "Prelaunch Failure"]
    result = {status: status_counts.get(status, 0) for status in expected_statuses}
    
    return result

# Returns the total number of missions launched in a specific year.

def getMissionsByYear(year: int) -> int:
    if not isinstance(year, int):
        return 0
    
    df = load_data()
    
    # Extract year from Date column and count
    df['Year'] = df['Date'].dt.year
    count = len(df[df['Year'] == year])
    
    return count

# Returns the name of the rocket that has been used the most times.
def getMostUsedRocket() -> str:
    df = load_data()
    
    # Count rocket usage
    rocket_counts = df['Rocket'].value_counts()
    
    if len(rocket_counts) == 0:
        return ""
    
    # Get max count
    max_count = rocket_counts.max()
    
    # Get all rockets with max count
    most_used = rocket_counts[rocket_counts == max_count]
    
    # Return alphabetically first if there's a tie
    return sorted(most_used.index)[0]

# Calculates the average number of missions per year over a given range.
def getAverageMissionsPerYear(startYear: int, endYear: int) -> float:
    if not isinstance(startYear, int) or not isinstance(endYear, int):
        return 0.0
    
    if startYear > endYear:
        return 0.0
    
    df = load_data()
    
    # Extract year
    df['Year'] = df['Date'].dt.year
    
    # Filter by year range
    filtered_df = df[(df['Year'] >= startYear) & (df['Year'] <= endYear)]
    
    # Calculate number of years in range
    num_years = endYear - startYear + 1
    
    if num_years == 0:
        return 0.0
    
    # Calculate average
    total_missions = len(filtered_df)
    average = total_missions / num_years
    
    return round(average, 2)


# Test functions if run directly
if __name__ == "__main__":
    print("Testing functions...")
    print(f"Mission count for NASA: {getMissionCountByCompany('NASA')}")
    print(f"Success rate for NASA: {getSuccessRate('NASA')}%")
    print(f"Top 3 companies: {getTopCompaniesByMissionCount(3)}")
    print(f"Mission status counts: {getMissionStatusCount()}")
    print(f"Most used rocket: {getMostUsedRocket()}")
    print(f"Missions in 2020: {getMissionsByYear(2020)}")
    print(f"Average missions per year (2010-2020): {getAverageMissionsPerYear(2010, 2020)}")