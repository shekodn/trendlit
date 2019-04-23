from stack.stack import Stack


class ParserHelper(object):
    def __init__(self):
        self.procedure_directory = {}  # [name] = {type, var_table}
        self.curr_dimension_counter = 0  # last defined array dimension counter
        self.curr_scope = ""  # The current scope inside the program
        self.curr_slice = None
        self.curr_r = 1
        self.curr_type = ""  # The current type used (module or var)
        self.curr_module_param_counter = 0
        self.curr_module_var_counter = 0
        self.queue_params = []
        self.stack_calls = Stack()
        self.stack_calls.push(999)
        self.stack_param_pointers = Stack()
        self.stack_param_pointers.push(0)

    def reset(self):
        self.__init__()

    def is_var_declared(self, var_name):
        return self.is_var_in_current_scope(var_name) or self.is_var_in_global_scope(
            var_name
        )

    def get_var_type_from_dir(self, var_name):
        if self.is_var_in_current_scope(var_name):
            return self.procedure_directory[self.curr_scope]["var_table"][var_name][
                "type"
            ]
        elif self.is_var_in_global_scope(var_name):
            return self.procedure_directory["global_script"]["var_table"][var_name][
                "type"
            ]
        return self.curr_type

    def get_var_address_from_dir(self, var_name):
        if self.is_var_in_current_scope(var_name):
            return self.procedure_directory[self.curr_scope]["var_table"][var_name][
                "memory_address"
            ]
        elif self.is_var_in_global_scope(var_name):
            return self.procedure_directory["global_script"]["var_table"][var_name][
                "memory_address"
            ]
        return None  # variable not declared

    def is_var_in_global_scope(self, var_name):
        return var_name in self.procedure_directory["global_script"]["var_table"]

    def is_scope_global(self, scope_name):
        return self.procedure_directory[scope_name]["scope_type"] is scope_to_code.get(
            "global"
        )

    def get_module_type(self, module_name):
        """
            Description:
            Params:
                module_name (str): the name of the scope
            Return:
                type (str): returns "bool" "str" "void" etc
         """
        return self.procedure_directory[module_name]["type"]

    def get_scope_type(self, scope_name):
        """
            Description:
            Params:
                scope_name (str): the name of the scope
            Return:
                scope_type (int): returns 1 for global, 2 for local
         """
        return self.procedure_directory[scope_name]["scope_type"]

    def is_var_in_current_scope(self, var_name):
        return var_name in self.procedure_directory[self.curr_scope]["var_table"]

    def get_count_of_local_vars(self, scope):
        """
            Description: Aux function to get snp #5 in Intermediate Code Actions for Module Definition

            Params:
                scope ():
            Return:
                num_local_vars (int):
         """
        num_total_vars = len(self.procedure_directory[scope]["var_table"])
        num_params = self.procedure_directory[scope]["params_count"]
        num_local_vars = num_total_vars - num_params

        if num_local_vars < 0:
            num_local_vars = 0

        return num_local_vars

    def is_module_in_procedure_dir(self, module_name):
        return module_name in self.procedure_directory

    def get_queue_params(self, module_name):
        if self.is_module_in_procedure_dir(module_name):
            return self.procedure_directory[module_name]["queue_params"]
        return None

    def get_upper_limit(self, slice_name, dimension):
        if self.is_var_in_current_scope(slice_name):
            return self.procedure_directory[self.curr_scope]["var_table"][slice_name][
                "t_dimensions"
            ]["ls" + str(dimension)]
        elif self.is_var_in_global_scope(slice_name):
            return self.procedure_directory["global_script"]["var_table"][slice_name][
                "t_dimensions"
            ]["ls" + str(dimension)]
        return 0  # slice_name not declared
