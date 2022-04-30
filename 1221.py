# Split a String in Balanced Strings


s = 'RLRRLLRLRL'
# s = 'RLLLLRRRLR'
# s = 'LLLLRRRR'
# s = 'RLRRRLLRLL'


class Solution:

    @staticmethod
    def balancedStringSplit(s: str) -> int:
        splits_counter = 0
        balance_counter = 0
        for c in s:
            balance_counter += -1 if c == 'L' else 1
            splits_counter += balance_counter == 0
        return splits_counter


if __name__ == '__main__':
    print(Solution.balancedStringSplit(s))