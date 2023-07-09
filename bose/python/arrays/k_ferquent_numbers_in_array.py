from collections import defaultdict,Counter
from typing import List

class Solution:
    
    def bucket_sort_based_on_count(self,num_counter: Counter, inp_array:List[int]):
        count_array: List[List[int]] = [set() for i in range(len(inp_array)+1)]
        print(f"initialized input count array is --> {count_array}")
        for i in range(len(inp_array)):
            num_count = num_counter.get(inp_array[i])
            print(f"Num count is --> {num_count}")
            ## append number to list under the count index in count_array
            count_array[num_count].add(inp_array[i])
        
        print(f"count array is --> {count_array}")
        sorted_array = []
        for j in range(len(count_array)-1,0,-1):
            print(f"Processing count array --> {count_array[j]}")
            for k in range(len(count_array[j])):
                sorted_array.append(list(count_array[j])[k])
        
        print(f"Sorted array based on count is --> {sorted_array}")
        return sorted_array
                        
        
            
    def topKfrequent(self,nums: List[int],k:int) -> List[int]:
        number_counter = Counter(nums)
        print(number_counter)
        sorted_array = self.bucket_sort_based_on_count(number_counter,nums)
        return sorted_array[0:k]
        


if __name__=="__main__":
    input_array = [1]
    print(Solution().topKfrequent(input_array,1))

