from semantic_cube.semantic_cube_helper import scope_to_code, code_to_scope


class RuntimeMemory(object):
    def __init__(self, scope_type):
        self.scope_type = scope_type
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

        # Address range for POINTER variables
        self.next_mem_global_ptr = 1000000
        self.next_mem_local_ptr = 2000000

        # Memory data structure
        self.int_memory = {}
        self.double_memory = {}
        self.bool_memory = {}
        self.str_memory = {}
        self.temp_memory = {} # All in the same hash (int, str, double, bool)
        # self.ptr_memory = {} # I think we do not need this with our solution. (we dont need to store the value, just -1000000 or -2000000 depending on curr scope)


    # ---- GET INFO FROM A MEMORY ADDRESS ----

    def get_value(self, addr):
        if self.is_int_addr(addr): # int
            return self.int_memory[addr]
        elif self.is_double_addr(addr): # double
            return self.double_memory[addr]
        elif self.is_bool_addr(addr): # bool
            return self.bool_memory[addr]
        elif self.is_str_addr(addr): # str
            return self.str_memory[addr]
        elif self.is_temp_addr(addr): # temp
            return self.temp_memory[addr]

    def set_value(self, value, addr):
        if self.is_int_addr(addr): # int
            self.int_memory[addr] = value
        elif self.is_double_addr(addr): # double
            self.double_memory[addr] = value
        elif self.is_bool_addr(addr): # bool
            self.bool_memory[addr] = value
        elif self.is_str_addr(addr): # str
            self.str_memory[addr] = value
        elif self.is_temp_addr(addr): # temp
            self.temp_memory[addr] = value


    def is_int_addr(self, addr):
        if self.scope_type is scope_to_code.get("global"):
            return self.is_addr_in_range(addr, self.mem_global_int_start, self.mem_global_int_end)
        else:
            return self.is_addr_in_range(addr, self.mem_local_int_start, self.mem_local_int_end)
        return False

    def is_double_addr(self, addr):
        if self.scope_type is scope_to_code.get("global"):
            return self.is_addr_in_range(addr, self.mem_global_double_start, self.mem_global_double_end)
        else:
            return self.is_addr_in_range(addr, self.mem_local_double_start, self.mem_local_double_end)

    def is_bool_addr(self, addr):
        if self.scope_type is scope_to_code.get("global"):
            return self.is_addr_in_range(addr, self.mem_global_bool_start, self.mem_global_bool_end)
        else:
            return self.is_addr_in_range(addr, self.mem_local_bool_start, self.mem_local_bool_end)

    def is_str_addr(self, addr):
        if self.scope_type is scope_to_code.get("global"):
            return self.is_addr_in_range(addr, self.mem_global_str_start, self.mem_global_str_end)
        else:
            return self.is_addr_in_range(addr, self.mem_local_str_start, self.mem_local_str_end)

    def is_temp_addr(self, addr):
        return self.is_addr_in_range(addr, self.mem_temp_int_start, self.mem_temp_str_end)


    def is_addr_in_range(self, addr, start_range, end_range):
        if addr >= start_range and addr <= end_range:
            return True
        return False
