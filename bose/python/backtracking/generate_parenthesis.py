class Solution:
    def __init__(self):
        self.all_pairs = []

    ''' 
    Choice: We can either place a '(' or a ')'
    Constraints: We cannot place a ')' unless we have already
                placed a ')'. which means that cannot place ')'
                if open_bracket_num == close_bracket_num
    Goal: We append to all_pairs list as soon as length of string is 2*n.Since 
        total pairs = 3, therefore total length of valid string will be 6
    '''


    def generate(self,open_bracket,close_bracket,curr_str,n):
        if len(curr_str)==2*n:
            self.all_pairs.append(curr_str)
            return

        if open_bracket==close_bracket:
            new_str = curr_str+"("
            open_bracket-=1
            self.generate(open_bracket,close_bracket,new_str,n)
            open_bracket+=1
            return
        elif open_bracket==0:
            new_str = curr_str+")"
            close_bracket-=1
            self.generate(open_bracket,close_bracket,new_str,n)
            close_bracket+=1
            return
        else:
            new_str = curr_str+"("
            open_bracket-=1
            self.generate(open_bracket,close_bracket,new_str,n)
            open_bracket+=1

            new_str = curr_str+")"
            close_bracket-=1
            self.generate(open_bracket,close_bracket,new_str,n)
            close_bracket+=1
            return

        

    def generateParenthesis(self, n):

        open_bracket = 3
        close_bracket = 3
        curr_str = ""
        self.generate(open_bracket, close_bracket,curr_str,n)

        return self.all_pairs 

if __name__ == "__main__":
    n=3
    sol = Solution()
    print(sol.generateParenthesis(n))

