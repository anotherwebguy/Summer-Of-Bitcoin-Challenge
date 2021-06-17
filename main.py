# The idea is to sort the list in reverse order of fee/weight to maximize the fee 
# as we do in a knapsack problem. This solution follows an similar approach


# maintaining the txids of previous transaction so the row with the parent 
# transaction can search in this list if parent transactions have occured before
all_transactions = []

class MempoolTransaction():
    # init function
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        # adding the txid to the list
        all_transactions.append(txid) 
        self.fee = int(fee)
        self.weight = int(weight)        
        self.sortvalue = round((float(fee)/float(weight)),5) # This will help to sort the list 
        self.parents = parents
        # if parents is not None check if the parents have appeared before in the all_transactions list
        if parents != "" :     
            check_parents = parents.split(';')
            for i in check_parents:
                # if has occurred for all parents then make the boolean value to be true
                if i in all_transactions:  
                    self.isvalid = True
                else:     
                    # if even one parent is not present in all_transactions then make the boolean value false and break
                    self.isvalid = False      
                    break
        else:       
            # if parents is None then include them in final transaction list
            self.isvalid = True
               
    # getter functions
    def get_txid(self):
        return self.txid

    def get_fee(self):
        return self.fee         
  
    def get_weight(self):
        return self.weight

    def get_sortvalue(self):
        return self.sortvalue

    def get_isvalid(self):
        return self.isvalid   

    def get_parents(self):
        return self.parents     
        

# Method to parse the  list from csv file
def parse_mempool_csv():
    parsedlist = []
    with open('mempool.csv') as f:
        parsedlist = [MempoolTransaction(*line.strip().split(',')) for line in f.readlines()[1:]] # excluding the 1st line i.e the header
    return parsedlist    


# sort the list of objects based on sortvalue(i.e fee/weight) to maximize the fees
def sorting_MempoolTransactions(transactions):
    return sorted(transactions,key= lambda e: e.get_sortvalue(),reverse=True)    


# From the sorted list consider all the objects untill the curr_sum is less than 4000000
def generate_finallist(sortedlist):
    curr_sum = 0  # to maintain the current weight after including the list items
    total_fee = 0  # for storing the maximized fee after the loop
    final_list = [] # for storing the final list whose total weight doesn't exceeds 4000000 and fee is maximized
    for i in sortedlist:
        # if the current sum doesn't exceeds 4000000 and is a valid item the include them in final list
        if curr_sum + i.get_weight() < 4000000 and i.get_isvalid() == True:
            curr_sum+=i.get_weight()
            total_fee+=i.get_fee()
            final_list.append(i)
    # printing the final solution       
    print(f"Total weight: {curr_sum}")       
    print(f"Total maximized fees: {total_fee}")  
    print(f"Total valid transaction: {len(final_list)}")   
    return final_list


# method to write the final list into the block.txt file
def write_blockfile(finallist):
    with open("block.txt", "a") as b:
            for w in finallist:
                    b.write(w.get_txid())
                    b.write("\n")
                   

if __name__ == '__main__':
    parsed_list = parse_mempool_csv() # parsing the list from csv file
    sorted_list = sorting_MempoolTransactions(parsed_list) # sorting the list
    final_list = generate_finallist(sorted_list) # generating final list from sorted list
    write_blockfile(final_list) # writing the final list of txids in block.txt file


