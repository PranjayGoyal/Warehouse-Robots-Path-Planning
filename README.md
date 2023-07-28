# Warehouse-Robots-Path-Planning
Designing an optimized path for multiple robots in a warehouse for picking and delivery operations using A* algorithm (shortest path) and linear programming (task allocation).
There are 3 scenarios

    1) Total Minimum Cost
    2) Priority Task Allocation
    3) Multiple Load Capacity of robots

Warehouse Environment 

    1) Initially → All robots at starting station (GREY)
    2) Picking Station (Purple)
    3) Delivery Station (Light Blue)
    4) Shelf / Inventory (BLACK)
    5) 6 Robots (EACH OF DIFFERENT COLOR)
    6) 6 Task Locations (GREEN)

![WhatsApp Image 2023-07-28 at 8 16 36 PM (1)](https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/da4ce2f9-580a-40d8-9b29-10ea9e9468ec)


Total Minimum Cost

       1) Shortest path distance (Cost) is calculated using A* algorithm for every robot-task pair (6 x 6 cost matrix)
       2) Min obj = sum_i,sum_j(r_i*cost(task_j))
       3) Constraints: Task_j  can be allocated to only unique robot

https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/e24ed4af-03ba-4c81-9e33-f0022c5ab2c3

![WhatsApp Image 2023-07-28 at 8 59 00 PM (1)](https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/c401d064-35c1-45e5-9d43-7076830fcfc2)


Priority Task Allocation

       1) Here Algorithm will not optimize the overall cost / distance of all 6 robots together like in above scenario.
       2) Nearest robot will be assigned to each task in decreasing order of priority P1>P2>P3>P4>P5>P6
       3) Priority varies from Brightest Yellow to Darkest Yellow
       
https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/ed258b7f-5587-4a30-9b6f-ef11a9288a7b

![WhatsApp Image 2023-07-28 at 8 28 55 PM](https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/f2e71396-2167-4714-aec5-80aa0066fc23)


Load Capacity

       1) Here the load capacity of each robot is k (constant), for this example k=2
       2) Suppose 2 tasks are near each other then instead of 2 robots going to the individual task, 
          1 robot can complete both the tasks.
   
https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/5f494798-d8d7-400b-bd84-d4c97a60fe75



Comparison between A* and Dijkstra Algorithm for finding the shortest path between robot and an end point
( Why we have used A* and not Dijkstra for calculating the shortest path distance )

    1) A* is faster because it avoids searching extra nodes
    2) A* is also an informed search algorithm (takes goal state into account)

A* Algorithm Visualization - Time Taken - 5.385 sec

https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/46847313-d5d5-4799-b81c-4470113c09dd


Dijkstra Algorithm Visualization - Time Taken - 5.385 sec

https://github.com/PranjayGoyal/Warehouse-Robots-Path-Planning/assets/89729339/da7b6d27-12b9-4c21-a921-463bb563335e









