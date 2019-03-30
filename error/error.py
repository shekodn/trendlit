#!/usr/bin/python3


class Error(object):
    def __init__(self, code=0, custom_message=""):
        self.code = code
        self.custom_message = custom_message
        # self.message = message

    # def __str__(self):
    #     return "%d %s" % (self.code, self.error)
