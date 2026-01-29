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
        source = json.loads(lines[0])
        
        # Read target string
        target = json.loads(lines[1])

        # Read list of characters
        original = json.loads(lines[2])

        # Read list of characters
        changed = json.loads(lines[3])

        #read list of ints
        cost = json.loads(lines[4])
    
    print(f"source: {source}")
    print(f"target: {target}")
    print(f"original: {original}")
    print(f"changed: {changed}")
    print(f"cost: {cost}")
    
    print()
    
    # Create solution instance and run
    solution = Solution()
    result = solution.minimumCost(source, target, original, changed, cost)
    print(f"\nResult: {result}")
