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
        
        # Read source string
        source = lines[0]
        
        # Read target string
        target = lines[1]
    
    print(f"source: {source}")
    print(f"target: {target}")
    print()
    
    # Create solution instance and run
    solution = Solution()
    result = solution.minCost(source, target)
    print(f"\nResult: {result}")
