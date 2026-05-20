class Solution:
    def isValid(self, s: str) -> bool:
        """
        As soon as we encounter a close bracket, 
        immediately before we should have an unaccounted open bracket
        1. Maintain a list of open brackets
        2. Traverse thru string
            a. If open bracket, add to list
            b. If close string, pop the latest open bracket and see if match
                If match continue, if not then false
        return True

        Exceptions: if empty string or odd number of brackets
        """

        if len(s)%2 != 0:
            return False
        open_list = []
        close_brackets = ')]}'

        for bracket in s:
            if bracket not in close_brackets:
                open_list.append(bracket)
            else:
                latest_open = open_list.pop() if open_list else ''
                if latest_open + bracket not in ['[]', '{}', '()']:
                    return False
        
        return len(open_list) == 0
        