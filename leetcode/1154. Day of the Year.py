class Solution:
    def dayOfYear(self, date: str) -> int:
        y = int(date[:4])
        m = int(date[5:7])
        d = int(date[8:])
        if y % 4 == 0 and y % 100 != 0: #閏年
            if m == 1 or m == 2 :
                return 31 * (m - 1) + d
            if m == 3 or m == 4 :
                return 31 * (m - 1) + d - 2
            if m == 5 or m == 6 :
                return 31 * (m - 1) + d - 3
            if m == 7 or m == 8 or m == 9:
                return 31 * (m - 1) + d - 4
            if m == 10 or m == 11 :
                return 31 * (m - 1) + d - 5
            if m == 12 :
                return 31 * (m - 1) + d - 6
        else:
            if m == 1 or m == 2 :
                return 31 * (m - 1) + d
            if m == 3 or m == 4 :
                return 31 * (m - 1) + d - 3
            if m == 5 or m == 6 :
                return 31 * (m - 1) + d - 4
            if m == 7 or m == 8 or m == 9:
                return 31 * (m - 1) + d - 5
            if m == 10 or m == 11 :
                return 31 * (m - 1) + d - 6
            if m == 12 :
                return 31 * (m - 1) + d - 7
