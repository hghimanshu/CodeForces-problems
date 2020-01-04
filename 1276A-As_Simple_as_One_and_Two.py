def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def processString(arr):
    not_req = {"twone", "one", "two"}
    for v in arr:
        count = {}
        if 'twone' in v:
            count['twone'] = v.count('twone')
        if 'one' in v:
            if 'twone' in list(count.keys()):
                count['one'] = v.count('one') - count['twone']
            else:
                count['one'] = v.count('one')
        if 'two' in v:
            count['two'] = v.count('two')
        print(v, count)
    return count
if __name__ == "__main__":
    # n = int(input())
    n = 4
    arr = []
    # for i in range(n):
    #     arr.append(input())
    arr = ['onetwone','onetwonetwooneooonetwooo','oneoneone','twotwo']
    answers = processString(arr)
