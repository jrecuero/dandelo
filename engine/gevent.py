"""gevent.py module contains all functionality required to create any game
event.
"""

class GEvent:
    """GEvent class contains all attributes and functionality for any game
    event.

    Event: trigger/destination/role[/timing]

    trigger: action
    destination: top/parent
    role: component:function
    timing: now/<time>
    """

    def __init__(self, a_type, a_data):
        """__init__ method creates a new GEvent instance.

        = type attribute contains the event type.

        - data dictionary contains all information required to process the
        event.
        """
        self.type = a_type
        self.data = a_data

    @property
    def trigger(self):
        """trigger property returns the event trigger value.
        """
        a_segments = self.type.split("/")
        #if a_segments[0] == "action":
        #    return self.actions.get("/".join(a_segments[1:]), None)
        #return None        
        return a_segments[0]

    @property
    def destination(self):
        """destination property returns the event destination value.
        """
        a_segments = self.type.split("/")
        return a_segments[1]

    @property
    def role(self):
        """role property returns the event role value.
        """
        a_segments = self.type.split("/")
        return a_segments[2]

    @property
    def timing(self):
        """timing property returns the event timing value.
        It could be not defined, which means the event should be processed
        normally.
        """
        a_segments = self.type.split("/")
        return a_segments[3] if len(a_segments) >= 4 else None

    @property
    def handler(self):
        """handler property returns the last handler provided in the 
        event.data["handler"] property.
        """
        if self.data and self.data.get("handler"):
            return self.data["handler"][-1]
        return None

    def __repr__(self):
        """__repr__ internal method represents the GEvent instance as a
        string.
        """
        return "event:{} - data:{}".format(self.type, self.data)
