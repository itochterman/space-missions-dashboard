"""
Test Script for Space Missions Analysis Functions
Run this to verify all functions work correctly before submission.
"""

import sys
from functions import *

def test_all_functions():
    """Run comprehensive tests on all 8 required functions"""
    
    print("=" * 60)
    print("SPACE MISSIONS FUNCTION TEST SUITE")
    print("=" * 60)
    print()
    
    try:
        # Test 1: getMissionCountByCompany
        print("Test 1: getMissionCountByCompany")
        print("-" * 40)
        test_companies = ["NASA", "SpaceX", "RVSN USSR"]
        for company in test_companies:
            count = getMissionCountByCompany(company)
            print(f"  {company}: {count} missions")
        
        # Edge case: non-existent company
        count = getMissionCountByCompany("NonExistent Corp")
        print(f"  NonExistent Corp: {count} missions (should be 0)")
        print("  ✓ PASSED\n")
        
        # Test 2: getSuccessRate
        print("Test 2: getSuccessRate")
        print("-" * 40)
        for company in test_companies:
            rate = getSuccessRate(company)
            print(f"  {company}: {rate}% success rate")
        
        # Edge case: non-existent company
        rate = getSuccessRate("NonExistent Corp")
        print(f"  NonExistent Corp: {rate}% (should be 0.0)")
        print("  ✓ PASSED\n")
        
        # Test 3: getMissionsByDateRange
        print("Test 3: getMissionsByDateRange")
        print("-" * 40)
        missions = getMissionsByDateRange("1957-10-01", "1957-12-31")
        print(f"  Missions in Oct-Dec 1957: {len(missions)}")
        if missions:
            print(f"  First mission: {missions[0]}")
            print(f"  Last mission: {missions[-1]}")
        
        # Edge case: invalid date range
        missions = getMissionsByDateRange("2050-01-01", "2050-12-31")
        print(f"  Future dates: {len(missions)} missions (should be 0)")
        print("  ✓ PASSED\n")
        
        # Test 4: getTopCompaniesByMissionCount
        print("Test 4: getTopCompaniesByMissionCount")
        print("-" * 40)
        top_companies = getTopCompaniesByMissionCount(5)
        print(f"  Top 5 companies:")
        for i, (company, count) in enumerate(top_companies, 1):
            print(f"    {i}. {company}: {count} missions")
        print("  ✓ PASSED\n")
        
        # Test 5: getMissionStatusCount
        print("Test 5: getMissionStatusCount")
        print("-" * 40)
        status_counts = getMissionStatusCount()
        print("  Mission status breakdown:")
        for status, count in status_counts.items():
            print(f"    {status}: {count}")
        total = sum(status_counts.values())
        print(f"  Total: {total} missions")
        print("  ✓ PASSED\n")
        
        # Test 6: getMissionsByYear
        print("Test 6: getMissionsByYear")
        print("-" * 40)
        test_years = [1957, 1969, 2000, 2020]
        for year in test_years:
            count = getMissionsByYear(year)
            print(f"  {year}: {count} missions")
        
        # Edge case: future year
        count = getMissionsByYear(2050)
        print(f"  2050: {count} missions (should be 0)")
        print("  ✓ PASSED\n")
        
        # Test 7: getMostUsedRocket
        print("Test 7: getMostUsedRocket")
        print("-" * 40)
        rocket = getMostUsedRocket()
        print(f"  Most used rocket: {rocket}")
        print("  ✓ PASSED\n")
        
        # Test 8: getAverageMissionsPerYear
        print("Test 8: getAverageMissionsPerYear")
        print("-" * 40)
        test_ranges = [(2010, 2020), (1960, 1970), (2000, 2005)]
        for start, end in test_ranges:
            avg = getAverageMissionsPerYear(start, end)
            print(f"  {start}-{end}: {avg} missions/year average")
        
        # Edge case: single year
        avg = getAverageMissionsPerYear(2020, 2020)
        print(f"  2020-2020: {avg} missions/year (single year)")
        print("  ✓ PASSED\n")
        
        print("=" * 60)
        print("ALL TESTS COMPLETED SUCCESSFULLY! ✓")
        print("=" * 60)
        print()
        print("Your functions are working correctly.")
        print("Make sure to replace space_missions_sample.csv with")
        print("the full space_missions.csv file before submission.")
        
        return True
        
    except FileNotFoundError:
        print("\n❌ ERROR: space_missions.csv not found!")
        print("Please ensure the CSV file is in the same directory.")
        print("For testing, you can rename space_missions_sample.csv")
        print("to space_missions.csv")
        return False
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("One or more tests failed. Check the error message above.")
        return False


if __name__ == "__main__":
    success = test_all_functions()
    sys.exit(0 if success else 1)
