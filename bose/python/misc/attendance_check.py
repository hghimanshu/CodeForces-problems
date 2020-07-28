class Solution:
    def checkRecord(self, s: str) -> bool:
        self.late = 0
        self.absent = 0
        for c in s:
            if c=="L":
                self.late+=1
            else:
                self.late = 0
                if c=="A":
                    self.absent+=1
            if self.absent > 1 or self.late >=3:
                return False
        return True


# class Solution:
#     def __init__(self):
#         pass
#     def checkRecord(self, s: str) -> bool:
#         self.att ={}
#         for l in range(0,len(s)):
#             print(s[l])
#             if s[l] == "A":
#                 if s[l] not in self.att.keys():
#                     self.att.update({"A":1})
#                 else:
#                     self.att[s[l]]+=1
#                 if self.att[s[l]] > 1:
#                     print(self.att)
#                     return False
#             elif s[l] == "L":
#                 if s[l] not in self.att.keys():
#                     self.att.update({"L":0})
#                 if l==0:
#                     continue
#                 else:
#                     if s[l] == s[l-1]:
#                         self.att["L"]+=1
#                         if self.att["L"] >=2:
#                             print(self.att)
#                             return False
#                     else:
#                         self.att["L"]=0
#             print(self.att)
#         return True

c = Solution()
print(c.checkRecord("PPALLL"))



"""
Runtime: 32 ms, faster than 43.90% of Python3 online submissions for Student Attendance Record I.
Memory Usage: 13.9 MB, less than 11.11% of Python3 online submissions for Student Attendance Record I.
""'




"""
Runtime: 0 ms, faster than 100.00% of Go online submissions for Student Attendance Record I.
Memory Usage: 2 MB, less than 100.00% of Go online submissions for Student Attendance Record I.
"""