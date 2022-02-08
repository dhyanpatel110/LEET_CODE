'''
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]
  
Example 2:
Input: rowIndex = 0
Output: [1]
  
Example 3:
Input: rowIndex = 1
Output: [1,1]

         |h| = |  h  | * h-r+1
         |r|   | r-1 |   -----
                           r
'''
#CODE:
  class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        
        for x in range(1, rowIndex+1):
            row.append(row[x-1]*(rowIndex - x + 1)//x)
        return row
        

        
        
        
