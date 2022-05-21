

----------------------------------------------------------------

Tower_of_Hanoi: 

There are one object defined. That is Object
  Object  = { A, B, C }

To run the program with facts file 1
    ./graphplan -o hanoi/hanoi_ops.txt -f hanoi/hanoi_facts1.txt

To run the program with facts file 2
    ./graphplan -o hanoi/hanoi_ops.txt -f hanoi/hanoi_facts2.txt

To run the program with the facts
    ./graphplan -o hanoi/hanoi_ops.txt -f [fact-file]

----------------------------------------------------------------

7_Puzzle:

There are two objects defined. That is a Tile and a Location
  Tile = { t1, t2, t3, t4, t5, t6, t7 }
  Location  = { l1, l2, l3, l4, l5, l6, l7, l8, l9 }

To run the program with facts file 1
    ./graphplan -o 7puzzle/7puzzle_ops.txt -f 7puzzle/7puzzle_facts1.txt

To run the program with facts file 2
    ./graphplan -o 7puzzle/7puzzle_ops.txt -f 7puzzle/7puzzle_facts2.txt

To run the program with the facts
Note: Use the same format of the above fact files with adj literals in your fact file
./graphplan -o 7puzzle/7puzzle_ops.txt -f [fact-file]

