import os
import sys

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True

import json
from solution import Solution


if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    testcase_path = os.path.join(script_dir, "testcase.txt")
    
    # Read from Testcase.txt
    with open(testcase_path, 'r', encoding='utf-8-sig') as f:
        # Read all lines and filter out empty ones
        lines = [line.strip() for line in f.readlines() if line.strip()]
        
        # Read grid (as JSON array)
        grid = json.loads(lines[0])
        
        # Read k value
        k = int(lines[1])
    
    print(f"Grid: {grid}")
    print(f"k: {k}")
    print()
    
    # Create solution instance and run
    solution = Solution()
    result = solution.minCost(grid, k)
    print(f"\nResult: {result}")
