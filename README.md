# codinGame
My solutions for some challenges on codingame.com
- The first challenge: Implement the closestToZero function to return the temperature closer to zero which belongs to the list ts.
If ts is empty, return 0 (zero).
If two numbers are as close to zero, consider the positive number as the closest to zero (eg. if ts contains -5 and 5, return 5).
- The fourth challenge: Implement  find_largest(numbers) that should return the largest number from  numbers.
 The array  numbers always contains at least one number.
- The fifth challenge: You work in an automated factory and your objective is to write the function that will dispatch the 
packages to the correct stack, according to their volume and mass. A package is bulky if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimension is greater or equal than 150 cm. A package is heavy when its mass is greater or equal than 20 kg. You must dispatch the packages in the following stacks: STANDARD : standard packages (those which are not bulky nor heavy) can be handled normally. 
SPECIAL : packages that are either heavy or bulky can't be handled automatically.
REJECTED : packages that are both heavy and bulky are rejected.
Implement the function solve(width, height, length, mass) (units are centimeter for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.
Victory Conditions
All the packages are on the proper stack.
Lose Conditions
Your function returns a wrong answer.
Constraints
20 ≤ width, height, length ≤ 200
10 ≤ mass ≤ 1000
- The Sixth challenge: a Python function that returns the sum of all multiples of 3, 5, and 7 that are less than a number "n" between 1 and 1000.
- The last challenge: You work for a shop that wishes to give a discount of discount% to the most expensive item purchased by a given customer during the sales period. Only one product can benefit from the discount. 
You are tasked by the shop owner to implement the function calculate_total_price(prices, discount) which takes the list of prices of the products purchased by a customer and the percentage discount as parameters and returns the total purchase price as an integer (rounded down if the total is a float number).
