from modules.event import Event



sarahs_party = Event("2022-02-5", "Sarah's Birthday Party", 10, "The Silver Suite", "Sarah's 21st Birthday Party", False)
peters_party = Event("2022-05-9", "Peter's Retirement Party", 40, "The Gold Suite", "Peter wants karaoke", False)

event_list = [sarahs_party, peters_party]

def add_event_to_list(event):
    event_list.append(event)