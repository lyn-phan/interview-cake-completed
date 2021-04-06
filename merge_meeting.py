"""Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Python 3.6
Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

Python 3.6
your function would return:

  [(0, 1), (3, 8), (9, 12)]

Python 3.6
Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges. """


### Algorithm ###
# - if times overlap == if end time of first meeting is >= start of second meeting, merge
# first meeting == < start time of next meeting
# else, we leave separate

def merge_ranges(meeting):

    #sort by start time
    sorted_meeting = sorted(meeting)
    #initialize merged meeting list with earliest meeting
    merged_meetings = [sorted_meeting[0]]
    # [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]

    for current_meeting_start, current_meeting_end in sorted_meeting[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        #if current meeting overlaps with last merged meeting, use the later end time of the two
        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = ((last_merged_meeting_start, max(current_meeting_end, last_merged_meeting_end)))
        
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))
    
    return merged_meetings

print(merge_ranges(meeting=[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
#output =   [(0, 1), (3, 8), (9, 12)]