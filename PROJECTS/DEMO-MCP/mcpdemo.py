from mcp.server.fastmcp import FastMCP
import json
from typing import List

mcp = FastMCP("LeaveManager")

with open("employee_leaves.json", "r") as f:
    employee_leaves = json.load(f)
    
@mcp.tool()
def get_leave_balance_and_history(employee_id: str):
    return employee_leaves.get(employee_id, {})

@mcp.tool()
def apply_leave(employee_id: str, leave_dates: List[str]):
    '''Applies for leave for the given employee and dates.'''
    if employee_id not in employee_leaves:
        return {"error": "Employee not found"}
    
    leave_count = len(leave_dates)
    if employee_leaves[employee_id]['balance'] >= leave_count:
        employee_leaves[employee_id]['balance'] -= leave_count
        employee_leaves[employee_id]['history'].extend(leave_dates)
        
        with open("employee_leaves.json", 'w') as file:
            json.dump(employee_leaves, file, indent=2)
        return {"status": "Leave applied successfully"}
    
    else:
        return {"error": "insufficient leave balance"}
    
if __name__ == "__main__":
    mcp.run()