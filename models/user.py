class User:
    def __init__(self, id, vkid, group, sender_status):
        self.id = id
        self.vkid = vkid
        self.group = group
        self.sender_status = sender_status

    def invert_sender_status(self):
        if self.sender_status:
            self.sender_status = False
        else:
            self.sender_status = True

    def update(self):
        pass
