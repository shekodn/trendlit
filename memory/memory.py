from semantic_cube.semantic_cube_helper import scope_to_code, code_to_scope


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

        # Address range for TEMPORARY variables
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

    # ---- MEMORY ASSIGNATION FOR A VARIABLE ----
    def set_addr(self, scope_type, type):
        """
            Description:
            Params:
                scope_type (int): the type of the scope
                type (str): the type of the variable we want to assign
            Return:
                assigned_address (int): returns None if there was an error
         """
        if scope_type is scope_to_code.get("global"):
            return self.set_addr_global(type)
        elif scope_type is scope_to_code.get("local"):
            return self.set_addr_local(type)
        return None

    def set_addr_global(self, type):
        """
            Description:
                Select an address for GLOBAL variable, and increase the memory pointer
            Params:
                type (str): the type of the variable we want to assign
            Return:
                assigned_address (int): returns None if there was an error
         """
        assigned_address = None
        if type == "int":
            assigned_address = self.mem_global_int
            self.mem_global_int += 1
        elif type == "double":
            assigned_address = self.mem_global_double
            self.mem_global_double += 1
        elif type == "bool":
            assigned_address = self.mem_global_bool
            self.mem_global_bool += 1
        elif type == "str":
            assigned_address = self.mem_global_str
            self.mem_global_str += 1

        return assigned_address

    # Select an address for LOCAL variable, and increase the memory pointer
    def set_addr_local(self, type):

        assigned_address = None
        if type == "int":
            assigned_address = self.mem_local_int
            self.mem_local_int += 1
        elif type == "double":
            assigned_address = self.mem_local_double
            self.mem_local_double += 1
        elif type == "bool":
            assigned_address = self.mem_local_bool
            self.mem_local_bool += 1
        elif type == "str":
            assigned_address = self.mem_local_str
            self.mem_local_str += 1

        return assigned_address

    # Select an address for TEMPORARY variable, and increase the memory pointer
    def set_addr_temp(self, type):
        if type == "int":
            assigned_address = self.mem_temp_int
            self.mem_temp_int += 1
        elif type == "double":
            assigned_address = self.mem_temp_double
            self.mem_temp_double += 1
        elif type == "bool":
            assigned_address = self.mem_temp_bool
            self.mem_temp_bool += 1
        elif type == "str":
            assigned_address = self.mem_temp_str
            self.mem_temp_str += 1

        assigned_address = "(" + str(assigned_address)  # TODO: what is this??
        return assigned_address

    # ---- GET INFO FROM A MEMORY ADDRESS ----

    # Get the scope from a memory address
    def get_scope(self, dir):
        if dir >= self.mem_global_int_start and dir <= self.mem_global_int_end:
            return "global"  # TODO: ver si neceitamos usar el semantic cube
        elif dir >= self.mem_local_int_start and dir <= self.mem_local_str_end:
            return "local"
        else:
            return "temp"
