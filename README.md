1. Do these approaches have the same answers? How would you test this? What types of edge cases did you consider?
  - Yes they have the same answers
  - I tested it by first trying if the answers are same for all combinations that could be entered, then all test values entered using an input statement
  - I consider the furthest points from the end point, the point that had no way to the end point, and another point that is quite near the endpoint
  - Here is the screenshot of the executions

![results of execution](https://github.com/PhillipSaint254/maze-puzzle-coin-collector/assets/75745682/ef94f31c-c68f-4457-8a23-4830c282352b)

2. Do all starting points that are equidistant from the goal take the same amount of time to be calculated using the D&C approach? With the DP approach? Try different distances
  -  As with the D&C approach, equidistant approaches take equal amount of time or have negligible variance in time difference
  -  The variance in execution time between two equidistant starting points is wider in DP
3. D&C proved faster as it took less execution time in all instances
