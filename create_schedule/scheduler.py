class Teacher:
    def __init__(self, name, lessons=None, rooms=None, ):
        if rooms is None:
            rooms = {}
        else:
            self.rooms = rooms
        if lessons is None:
            lessons = []
        else:
            self.lessons = lessons
        self.name = name
