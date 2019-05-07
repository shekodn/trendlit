from semantic_cube.semantic_cube_helper import scope_to_code, code_to_scope


class Memory(object):
    def __init__(self):
        self.curr_scope_type = scope_to_code.get("global")
        # Address range for GLOBAL variables
        self.next_mem_global_int = 1000
        self.mem_global_int_start = 1000
        self.mem_global_int_end = 1999
        self.next_mem_global_double = 2000
        self.mem_global_double_start = 2000
        self.mem_global_double_end = 2999
        self.next_mem_global_bool = 3000
        self.mem_global_bool_start = 3000
        self.mem_global_bool_end = 3999
        self.next_mem_global_str = 4000
        self.mem_global_str_start = 4000
        self.mem_global_str_end = 4999

        # Address range for LOCAL variables
        self.next_mem_local_int = 5000
        self.mem_local_int_start = 5000
        self.mem_local_int_end = 5999
        self.next_mem_local_double = 6000
        self.mem_local_double_start = 6000
        self.mem_local_double_end = 6999
        self.next_mem_local_bool = 7000
        self.mem_local_bool_start = 7000
        self.mem_local_bool_end = 7999
        self.next_mem_local_str = 8000
        self.mem_local_str_start = 8000
        self.mem_local_str_end = 8999

        # Address range for TEMPORARY variables
        self.next_mem_temp_int = 9000
        self.mem_temp_int_start = 9000
        self.mem_temp_int_end = 9999
        self.next_mem_temp_double = 10000
        self.mem_temp_double_start = 10000
        self.mem_temp_double_end = 10999
        self.next_mem_temp_bool = 11000
        self.mem_temp_bool_start = 11000
        self.mem_temp_bool_end = 11999
        self.next_mem_temp_str = 12000
        self.mem_temp_str_start = 12000
        self.mem_temp_str_end = 12999
        # pointers for global temp vars
        self.next_mem_temp_global_int = 9000
        self.next_mem_temp_global_double = 10000
        self.next_mem_temp_global_bool = 11000
        self.next_mem_temp_global_str = 12000

        # Address range for CONSTANT variables
        self.next_mem_const_int = 13000
        self.mem_const_int_start = 13000
        self.mem_const_int_end = 13999
        self.next_mem_const_double = 14000
        self.mem_const_double_start = 14000
        self.mem_const_double_end = 14999
        self.next_mem_const_bool = 15000
        self.mem_const_bool_start = 15000
        self.mem_const_bool_end = 15999
        self.next_mem_const_str = 16000
        self.mem_const_str_start = 16000
        self.mem_const_str_end = 16999
        self.constant_addresses = {}
        self.constant_values = {}

        self.mem_global_ptr_start = 1_000_000

    def reset(self):
        self.__init__()

    # ---- MEMORY ASSIGNATION FOR A VARIABLE ----
    def set_var_addr(self, scope_type, type):
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

    def set_addr_global(self, var_type):
        """
            Description:
                Select an address for GLOBAL variable, and increase the memory pointer
            Params:
                type (str): the type of the variable we want to assign
            Return:
                assigned_address (int): returns None if there was an error
         """
        assigned_address = None
        if var_type == "int":
            assigned_address = self.next_mem_global_int
            self.next_mem_global_int += 1
        elif var_type == "double":
            assigned_address = self.next_mem_global_double
            self.next_mem_global_double += 1
        elif var_type == "bool":
            assigned_address = self.next_mem_global_bool
            self.next_mem_global_bool += 1
        elif var_type == "str":
            assigned_address = self.next_mem_global_str
            self.next_mem_global_str += 1
        return assigned_address

    # Select an address for LOCAL variable, and increase the memory pointer
    def set_addr_local(self, type):
        assigned_address = None
        if type == "int":
            assigned_address = self.next_mem_local_int
            self.next_mem_local_int += 1
        elif type == "double":
            assigned_address = self.next_mem_local_double
            self.next_mem_local_double += 1
        elif type == "bool":
            assigned_address = self.next_mem_local_bool
            self.next_mem_local_bool += 1
        elif type == "str":
            assigned_address = self.next_mem_local_str
            self.next_mem_local_str += 1
        return assigned_address

    # Select an address for TEMPORARY variable, and increase the memory pointer
    def set_addr_temp(self, type):
        assigned_address = None
        if self.curr_scope_type == scope_to_code.get("global"):
            assigned_address = self.set_addr_temp_global(type)
        elif type == "int":
            assigned_address = self.next_mem_temp_int
            self.next_mem_temp_int += 1
        elif type == "double":
            assigned_address = self.next_mem_temp_double
            self.next_mem_temp_double += 1
        elif type == "bool":
            assigned_address = self.next_mem_temp_bool
            self.next_mem_temp_bool += 1
        elif type == "str":
            assigned_address = self.next_mem_temp_str
            self.next_mem_temp_str += 1
        return assigned_address

    def set_addr_temp_global(self, type):
        assigned_address = None
        if type == "int":
            assigned_address = self.next_mem_temp_global_int
            self.next_mem_temp_global_int += 1
        elif type == "double":
            assigned_address = self.next_mem_temp_global_double
            self.next_mem_temp_global_double += 1
        elif type == "bool":
            assigned_address = self.next_mem_temp_global_bool
            self.next_mem_temp_global_bool += 1
        elif type == "str":
            assigned_address = self.next_mem_temp_global_str
            self.next_mem_temp_global_str += 1
        return assigned_address

    # Select an address for POINTER variable, and increase the memory pointer
    def set_addr_ptr(self, ptr_value):
        """
            Description:
                Select an address for POINTER variable.
                assigned_address = mem_ptr_start + ptr_value
            Params:
                ptr_value (int): the memory address that will be 'stored' as value in ptr
            Return:
                assigned_address (int): returns None if there was an error
         """
        return self.mem_global_ptr_start + ptr_value

    # Makes sure constants don't have multiple addresses
    def get_or_set_addr_const(self, value, type):
        """
            Description:
                Assigns and/or returns a memory address for a constant variable
            Params:
                value (str): the memory address that will be stored as value
                type (str): the type of the value that will be stored (int, double, bool etc)
            Return:
                assigned_address (int): the memory address assigned to the constant sent
         """
        real_value = self.convert_to_type(value, type)
        if value in self.constant_addresses:
            assigned_address = self.constant_addresses[value]
        else:  # add new constant
            assigned_address = self.set_addr_const(type)
            self.constant_addresses[value] = assigned_address
            self.constant_values[assigned_address] = real_value
        # For debuging
        # print(f"VLUE: {value}, REALVAL:{real_value}, REALTYPE:{type}, assigned_address:{assigned_address}")
        # print(f"\n constant_addresses: {self.constant_addresses}\n")
        # print(f"\n constant_values: {self.constant_values}\n")
        return assigned_address

    def convert_to_type(self, value, type):
        if type == "int":
            return int(value)
        elif type == "double":
            return float(value)
        elif type == "bool":
            return False if value == "False" else True
        elif type == "str":
            return value.strip('"')
        return None

    # Select an address for CONSTANT variable, and increase the memory pointer
    def set_addr_const(self, type):
        assigned_address = None
        if type == "int":
            assigned_address = self.next_mem_const_int
            self.next_mem_const_int += 1
        elif type == "double":
            assigned_address = self.next_mem_const_double
            self.next_mem_const_double += 1
        elif type == "bool":
            assigned_address = self.next_mem_const_bool
            self.next_mem_const_bool += 1
        elif type == "str":
            assigned_address = self.next_mem_const_str
            self.next_mem_const_str += 1
        return assigned_address

    def increase_next_mem(self, scope_type, type, amount):
        """
            Description: Increases the counter a certain amount for the next_mem of a specific scope and var_type. The module is used after an array is declared, this sets the counters to be ready for the next variable. This is how the memory is saved for all slice cells.
            Params:
                scope_type (int): the type of the scope
                type (str): the type of the variable we want to assign
            Return:
                assigned_address (int): returns None if there was an error
         """
        if scope_type is scope_to_code.get("global"):
            return self.increase_next_global_mem(type, amount)
        elif scope_type is scope_to_code.get("local"):
            return self.increase_next_local_mem(type, amount)
        return None

    def increase_next_global_mem(self, type, amount):
        if type == "int":
            self.next_mem_global_int += amount
        elif type == "double":
            self.next_mem_global_double += amount
        elif type == "bool":
            self.next_mem_global_bool += amount
        elif type == "str":
            self.next_mem_global_str += amount

    def increase_next_local_mem(self, type, amount):
        if type == "int":
            self.next_mem_local_int += amount
        elif type == "double":
            self.next_mem_local_double += amount
        elif type == "bool":
            self.next_mem_local_bool += amount
        elif type == "str":
            self.next_mem_local_str += amount

    def reset_local_vars(self):
        """
            Description: reset the local var counters, , this module is called when a module ends. Var table is deleted from procedure directory, so addresses must be ready for next module.
            Params:
            Return:
         """
        self.next_mem_local_int = 5000
        self.next_mem_local_double = 6000
        self.next_mem_local_bool = 7000
        self.next_mem_local_str = 8000
        self.reset_temp_vars()

    def reset_temp_vars(self):
        """
            Description: reset the temp var counters, this module is called when a module ends. Var table is deleted from procedure directory, so addresses must be ready for next module.
            Params:
            Return:
        """
        self.next_mem_temp_int = 9000
        self.next_mem_temp_double = 10000
        self.next_mem_temp_bool = 11000
        self.next_mem_temp_str = 12000
        self.next_mem_local_ptr = 18000

    # ---- GET INFO FROM A MEMORY ADDRESS ----

    # Get the scope from a memory address
    # def get_scope(self, dir):
    #     if dir >= self.mem_global_int_start and dir <= self.mem_global_int_end:
    #         return "global"  # TODO: ver si neceitamos usar el semantic cube
    #     elif dir >= self.mem_local_int_start and dir <= self.mem_local_str_end:
    #         return "local"
    #     else:
    #         return "temp"
