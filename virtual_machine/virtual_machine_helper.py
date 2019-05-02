#!/usr/bin/python3
class VMH(object):
    def __init__(self):
        self.queue_results = []

    def reset(self):
        self.__init__()

    def print_to_file(self, file_name):
        """
        Description: Generates .html file
        """
        file = open(file_name, "w")
        for line in self.queue_results:
            file.write(str(line))
            file.write("\n")
        file.close()
