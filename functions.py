"""
Space Missions Data Analysis Functions
Author: Isabella Tochterman
Date: January 2026

This module contains functions for analyzing historical space mission data.
All functions follow the exact specifications from the assessment requirements.
"""

import pandas as pd
from typing import List, Tuple, Dict
from datetime import datetime


def load_data() -> pd.DataFrame:
    """
    Load space missions data from CSV file.
    
    Returns:
        DataFrame containing space missions data
    """
    try:
        df = pd.read_csv('space_missions.csv')
        # Convert Date column to datetime for proper sorting
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        return df
    except FileNotFoundError:
        raise FileNotFoundError("space_missions.csv not found in current directory")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")


def getMissionCountByCompany(companyName: str) -> int:
    """
    Returns the total number of missions for a given company.
    
    Args:
        companyName: Name of the company (e.g., "NASA", "SpaceX")
    
    Returns:
        Integer representing the total number of missions
    
    Example:
        getMissionCountByCompany("NASA") # Returns: 394
    """
    if not isinstance(companyName, str):
        return 0
    
    df = load_data()
    count = len(df[df['Company'] == companyName])
    return count


def getSuccessRate(companyName: str) -> float:
    """
    Calculates the success rate for a given company as a percentage.
    
    Args:
        companyName: Name of the company
    
    Returns:
        Float representing success rate as a percentage (0-100), rounded to 2 decimal places
        Only "Success" missions count as successful
        Returns 0.0 if company has no missions
    
    Example:
        getSuccessRate("NASA") # Returns: 87.34
    """
    if not isinstance(companyName, str):
        return 0.0
    
    df = load_data()
    company_missions = df[df['Company'] == companyName]
    
    if len(company_missions) == 0:
        return 0.0
    
    success_count = len(company_missions[company_missions['MissionStatus'] == 'Success'])
    success_rate = (success_count / len(company_missions)) * 100
    
    return round(success_rate, 2)


def getMissionsByDateRange(startDate: str, endDate: str) -> List[str]:
    """
    Returns a list of all mission names launched between startDate and endDate (inclusive).
    
    Args:
        startDate: Start date in "YYYY-MM-DD" format
        endDate: End date in "YYYY-MM-DD" format
    
    Returns:
        List of strings containing mission names, sorted chronologically
    
    Example:
        getMissionsByDateRange("1957-10-01", "1957-12-31")
        # Returns: ["Sputnik-1", "Sputnik-2", "Vanguard TV3"]
    """
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


def getTopCompaniesByMissionCount(n: int) -> List[Tuple[str, int]]:
    """
    Returns the top N companies ranked by total number of missions.
    
    Args:
        n: Number of top companies to return
    
    Returns:
        List of tuples: [(companyName, missionCount), ...]
        Sorted by mission count in descending order
        If companies have the same count, sort alphabetically by company name
    
    Example:
        getTopCompaniesByMissionCount(3)
        # Returns: [("RVSN USSR", 1777), ("Arianespace", 279), ("NASA", 199)]
    """
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


def getMissionStatusCount() -> Dict[str, int]:
    """
    Returns the count of missions for each mission status.
    
    Returns:
        Dictionary with status as key and count as value
        Keys: "Success", "Failure", "Partial Failure", "Prelaunch Failure"
    
    Example:
        getMissionStatusCount()
        # Returns: {"Success": 3879, "Failure": 485, "Partial Failure": 68, "Prelaunch Failure": 7}
    """
    df = load_data()
    
    # Count each status
    status_counts = df['MissionStatus'].value_counts().to_dict()
    
    # Ensure all expected statuses are present (even if count is 0)
    expected_statuses = ["Success", "Failure", "Partial Failure", "Prelaunch Failure"]
    result = {status: status_counts.get(status, 0) for status in expected_statuses}
    
    return result


def getMissionsByYear(year: int) -> int:
    """
    Returns the total number of missions launched in a specific year.
    
    Args:
        year: Year (e.g., 2020)
    
    Returns:
        Integer representing the total number of missions in that year
    
    Example:
        getMissionsByYear(2020) # Returns: 114
    """
    if not isinstance(year, int):
        return 0
    
    df = load_data()
    
    # Extract year from Date column and count
    df['Year'] = df['Date'].dt.year
    count = len(df[df['Year'] == year])
    
    return count


def getMostUsedRocket() -> str:
    """
    Returns the name of the rocket that has been used the most times.
    
    Returns:
        String containing the rocket name
        If multiple rockets have the same count, return the first one alphabetically
    
    Example:
        getMostUsedRocket() # Returns: "Cosmos-3M (11K65M)"
    """
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


def getAverageMissionsPerYear(startYear: int, endYear: int) -> float:
    """
    Calculates the average number of missions per year over a given range.
    
    Args:
        startYear: Starting year (inclusive)
        endYear: Ending year (inclusive)
    
    Returns:
        Float representing average missions per year, rounded to 2 decimal places
    
    Example:
        getAverageMissionsPerYear(2010, 2020) # Returns: 87.45
    """
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
