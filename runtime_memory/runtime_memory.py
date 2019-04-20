from semantic_cube.semantic_cube_helper import scope_to_code, code_to_scope


class RuntimeMemory(object):
    def __init__(self, scope_type):
        # Address range for GLOBAL variables
        self.mem_global_int_start = 1000
        self.mem_global_int_end = 1999
        self.mem_global_double_start = 2000
        self.mem_global_double_end = 2999
        self.mem_global_bool_start = 3000
        self.mem_global_bool_end = 3999
        self.mem_global_str_start = 4000
        self.mem_global_str_end = 4999

        # Address range for LOCAL variables
        self.mem_local_int_start = 5000
        self.mem_local_int_end = 5999
        self.mem_local_double_start = 6000
        self.mem_local_double_end = 6999
        self.mem_local_bool_start = 7000
        self.mem_local_bool_end = 7999
        self.mem_local_str_start = 8000
        self.mem_local_str_end = 8999

        # Address range for TEMPORARY variables
        self.mem_temp_int_start = 9000
        self.mem_temp_int_end = 9999
        self.mem_temp_double_start = 10000
        self.mem_temp_double_end = 10999
        self.mem_temp_bool_start = 11000
        self.mem_temp_bool_end = 11999
        self.mem_temp_str_start = 12000
        self.mem_temp_str_end = 12999

        # Memory data structure
        self.int_memory = {}
        self.double_memory = {}
        self.bool_memory = {}
        self.str_memory = {}


    # ---- GET INFO FROM A MEMORY ADDRESS ----

    def get_value():
        return

    def return_value():
        return


    # Get the scope from a memory address
    def get_scope(self, dir):
        if dir >= self.mem_global_int_start and dir <= self.mem_global_int_end:
            return "global"  # TODO: ver si neceitamos usar el semantic cube
        elif dir >= self.mem_local_int_start and dir <= self.mem_local_str_end:
            return "local"
        else:
            return "temp"
