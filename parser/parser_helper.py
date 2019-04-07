class ParserHelper(object):
    def __init__(self):
        self.procedure_directory = {}  # [name] = {type, var_table}
        self.curr_scope = ""  # The current scope inside the program
        self.curr_type = ""  # The current type used (module or var)
        self.curr_module_param_counter = 0
        self.curr_module_var_counter = 0

    def reset(self):
        self.__init__()
