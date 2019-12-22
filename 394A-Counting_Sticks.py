def checkCond(a_count, b_count, rhs_count):
    if a_count + b_count == rhs_count:
        return True
    else:
        return False
    
def generating_answer(a, b, rhs, count):
    s = a + '+' + b + '=' + rhs
    rhs_count = rhs.count('|')
    a_count = a.count('|')
    b_count = b.count('|')
    count +=1
    val = checkCond(a_count, b_count, rhs_count)
    
    if val:
        return s
    else:
        if count <= 1:
            if a_count + b_count > rhs_count: ## lhs is greater
                if a_count > b_count:
                    ans = generating_answer(a[1:], b, rhs + '|', count)
                else:
                    ans = generating_answer(a, b[1:], rhs + '|', count)
            else:
                ans = generating_answer(a + '|', b, rhs[1:], count)
            count +=1
            return ans
        else:
            return "Impossible"



if __name__ == "__main__":
    s = input()
    count = 0
    lhs, rhs = s.split('=')[0], s.split('=')[1]
    a, b = lhs.split('+')[0], lhs.split('+')[1]

    
    ans = generating_answer(a, b, rhs, count)
    print(ans)