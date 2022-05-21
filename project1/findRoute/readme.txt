Programming Language Used : Python
#PART:1


Code Execution Instructions:
->For Executing uninformed Search:
  python find_route.py input1.txt startNode goalNode
  -For Example:
   python find_route.py input1.txt Bremen Kassel

->For Executing informed Search:
  python find_route.py input1.txt startNode goalNode
  -For Example:
  python find_route.py input1.txt Bremen Kassel h_kassel.txt

Command Line:
# python find_route.py input1.txt Bremen Kassel
# python find_route.py input1.txt Bremen Kassel h_kassel.txt

Code Structure:
  There are multiple functions defined in the program. Which are explained below.
  There are two read function one for Reading Input file and one for Heuristic values.
  There is one function to get the total cost to the goal.
  There is one function for printing  the final output which has the starting node and 
  end node and the distance. 
  Apart from these there are two functions that are specific to the Searching
  - Uniform Cost Search as Uniformed_UCS
  - Informed Search as InformedAStarSearch

Using all these function we get the final output by printing.  path from start state to goal state.