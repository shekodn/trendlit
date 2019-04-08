class Memory(object):
    def __init__(self):
        # Address range for GLOBAL variables
        self.mem_global_int = 1000
        self.mem_global_int_start = 1000
        self.mem_global_int_end = 1999
        self.mem_global_double = 2000
        self.mem_global_double_start = 2000
        self.mem_global_double_end = 2999
        self.mem_global_bool = 3000
        self.mem_global_bool_start = 3000
        self.mem_global_bool_end = 3999
        self.mem_global_str = 4000
        self.mem_global_str_start = 4000
        self.mem_global_str_end = 4999

        # Address range for LOCAL variables
        self.mem_local_int = 5000
        self.mem_local_int_start = 5000
        self.mem_local_int_end = 5999
        self.mem_local_double = 6000
        self.mem_local_double_start = 6000
        self.mem_local_double_end = 6999
        self.mem_local_bool = 7000
        self.mem_local_bool_start = 7000
        self.mem_local_bool_end = 7999
        self.mem_local_str = 8000
        self.mem_local_str_start = 8000
        self.mem_local_str_end = 8999

        # Address range for TEMPORAL variables
        self.mem_temp_int = 9000
        self.mem_temp_int_start = 9000
        self.mem_temp_int_end = 9999
        self.mem_temp_double = 10000
        self.mem_temp_double_start = 10000
        self.mem_temp_double_end = 10999
        self.mem_temp_bool = 11000
        self.mem_temp_bool_start = 11000
        self.mem_temp_bool_end = 11999
        self.mem_temp_str = 12000
        self.mem_temp_str_start = 12000
        self.mem_temp_str_end = 12999
