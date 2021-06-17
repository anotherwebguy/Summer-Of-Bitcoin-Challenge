
all_transactions = []

class MempoolTransaction():
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        all_transactions.append(txid)
        self.fee = int(fee)
        self.weight = int(weight)
        self.sortvalue = round((float(fee)/float(weight)),5)
        self.parents = parents
        if parents != "" :
            check_parents = parents.split(';')
            for i in check_parents:
                if i in all_transactions:
                    self.isvalid = True
                else:
                    self.isvalid = False      
                    break
        else:
            self.isvalid = True
               

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
        

def parse_mempool_csv():
    parsedlist = []
    with open('mempool.csv') as f:
        parsedlist = [MempoolTransaction(*line.strip().split(',')) for line in f.readlines()[1:]]
    return parsedlist    


def sorting_MempoolTransactions(transactions):
    return sorted(transactions,key= lambda e: e.get_sortvalue(),reverse=True)    


def generate_finallist(sortedlist):
    curr_sum = 0
    total_fee = 0
    final_list = []
    for i in sortedlist:
        if curr_sum + i.get_weight() < 4000000 and i.get_isvalid() == True:
            curr_sum+=i.get_weight()
            total_fee+=i.get_fee()
            final_list.append(i)
            
    print(f"Total weight: {curr_sum}")       
    print(f"Total maximized fees: {total_fee}")  
    print(f"Total valid transaction: {len(final_list)}")   
    return final_list


def write_blockfile(finallist):
    with open("block.txt", "a") as b:
            for w in finallist:
                    b.write(w.get_txid())
                    b.write("\n")
                   

if __name__ == '__main__':
    parsed_list = parse_mempool_csv()
    sorted_list = sorting_MempoolTransactions(parsed_list)
    final_list = generate_finallist(sorted_list)
    write_blockfile(final_list)


