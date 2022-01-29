class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        if time[0] == '?' and time[1] != '?' and int(time[1]) < 4: time[0] = '2'
        elif time[0] == '?' and time[1] == '?': time[0] = '2'
        elif time[0] == '?': time[0] = '1'
        if time[1] == '?' and time[0] != '2': time[1] = '9'
        elif time[1] == '?': time[1] = '3'
        if time[3] == '?': time[3] = '5'
        if time[4] == '?': time[4] = '9'
        return ''.join(time)