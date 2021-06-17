# Summer-Of-Bitcoin-Challenge

Source code and Solution for the Summer Of Bitcoin challenge

----

## Approach
The idea here is that I've maintained an list with all the items having attriutes txid, fee, weight, parents, sortvalue (which will be used to sort the list based on this value in reverse order to maximize the fee), isvalid (This indicates whether an list item is a valid item i.e if it's parents is none or the parents have appeared before that row item in the list).
<br />
After parsing the list from the csv file getting the parsed list with above attributes , i've sorted the list based on sortvalue in reverse order to maximize the fee as we do in a knapsack problem.
<br />
Then the sorted list is put under a method to generate the final list which contains only those items till where the current weight doesn't exceed 4000000.
 For that i've maintained an curr_sum variable that keeps adding the weight of the item from top and including them in final list untill curr_ssum does'nt exceed 4000000
 <br />
 
 ----
 
 ## Solution
  ![sol](https://user-images.githubusercontent.com/66346161/122337641-3b136600-cf5c-11eb-975b-6156373a4e90.png)
  
  So it includes a total of <b>3214</b> transactions with maximized fee as <b>5769626<b/> and total weight <b>3999940<b/> which doesn't exceeds 4000000
