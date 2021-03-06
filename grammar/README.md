# SEMANTIC NEURAL POINTS
## PROCEDURE/MODULE SEMANTIC ACTION

### snp_script_start
Start of script global scope (adds global scope to directory)

### snp_add_module
Start of the module (add module to directory)

### snp_save_type_to_module_table
Save the last type defined

### snp_save_type
Save the last type defined

### snp_save_void_type
Save the last type as void (for modules)

## ARRAYS - SLICES
###### Retrieved from Acciones para el acceso a una variable dimensionada

### snp_add_dimension
Increases dimension of var

### snp_increase_dimension_count
Checks that array has a value bigger than 0, indicates another dimension in slice, adds upper limit to t_dimensions and calculates R

### snp_slice_access_3
Adds Verification quad and adds base address to quad (S)

### snp_update_curr_slice
Saves current slice name

### snp_increase_dim_access_count
Indicates another dimension in slice (Increase current dimension counter by 1)

### snp_reset_dim_access_count
Resets current dimension counter

### snp_init_slice_1d
initialize slice with respective initialization value (0 for int, False for bool, etc)

### snp_push_start_false_bottom
Add a false bottom to maintain precedence with arrays []

### snp_return_module
Allows return only in non-global scopes (functions)

### snp_end_module
End of the module deletes the var table (resets local contex)
snp #7 in Intermediate Code Actions for Module Definition

## Variable Semantic Actions

### snp_add_var
Adds a variable defined to the current scope variable table

## Sequential Statements

### snp_add_eval_quad
Add eval quad

### snp_push_pending_operand
Pushes pending operand to stack
###### Retrieved from: MATHEMATICAL EXPRESSIONS (INTERMEDIATE REPRESENTATION)

### snp_save_type_int
Sets INT as current type of the ID that it is being processed

### snp_save_type_double
Sets DOUBLE as current type of the ID that it is being processed

### snp_save_type_str
Sets STR as current type of the ID that it is being processed

### snp_save_type_bool
Sets BOOL as current type of the ID that it is being processed

### snp_push_pending_token
Pushes pending token to stack
###### Retrieved from: Mathematical expressions (intermediate representation

### snp_push_pending_eval_token
Pushes pending EVAL token to stack

### snp_push_solitary_operand
Variables declared without a corresponding initialization are zero-valued.
For example, the zero value for an int is 0

### snp_add_assignation_quad
If it makes semantic sense, it generates quadruple for assignations

### snp_check_precedence_and_create_quadruple_for_sign
Generates quadruple expression for arithmetic operations

### snp_check_precedence_and_create_quadruple_for_op
Generates quadruple expression for product operations

### snp_check_precedence_and_create_quadruple_for_rel
Generates quadruple expression for relational operations

### snp_check_precedence_and_create_quadruple_for_logic
Generates quadruple expression for logical operations

### snp_clean_stack_until_false_bottom
Removes false bottom from the stack

### snp_checks_for_previous_declaration
Checks for previously declared modules/variables

## Conditionals

### snp_conditional_statement_1
Actions to produce intermediate representation for non-linear statements using quadruples

### snp for single IF. Equivalent to snp_while_2

### snp_conditional_statement_2
Fills GOTOF

### snp_conditional_statement_3
For else: generates GOTO quad

## Loops

### snp_while_1
Pushes counter to stack of jumps

### snp_while_3
Gerentes GOTO quad

### snp_do_while_gotot
Generates GOTOT quad
Intermediate Code Actions for a Module Definition

### snp_counts_params
Counts number of params for module definitions

### snp_add_params_count_to_table
Creates param lists with types
###### Retrieved from snp #4 in Intermediate Code Actions for Module Definition


## Intermediate code actions for module definition (intermediate representation

### snp_add_quad_cont_to_table
###### Retrieved from snp #6 in Intermediate Code Actions for Module Definition

### snp_verify_module_existance
Verifies that the procedure exists in the Procedure Directory
###### Retrieved from snp #1 Module Call

### snp_add_era_size_quad
Generates ERA size (Activation Record expansion - NEW - size) and adds a pointer to the first parameter type in the parameter table
###### Retrieved from snp #2 Module Call

### snp_check_param
Verifies Argument type agains current parameter(#k) in parameter table Generates action PARAMETER, Argument, Argument#k
###### Retrieved from snp #3 Module Call

### snp_check_return
Checks if current function is void, to see if you can use it to assign a value

### snp_add_gosub
Generates quad GOSUB, procedure_name, -1, intitial - address
###### Retrieved from snp #6 Module Call

## HTML

### snp_open_html_tag
Creates eval token to process an html tag in the VM

### snp_class_quad
Gets STRING from the declared class
In trendlit: h2 class : "STRING" {}

### snp_href_quad
Gets STRING from the declared href
In trendlit: link href : "STRING" {}

### snp_img_quad
Gets STRING from the declared img
In trendlit: img src : "STRING" {}

### snp_close_html_tag
Checks that the respective html_tag has a closing tag.
For example: img doesn't have one, but h1 yes

### snp_br_html_tag
Generates quad for html br tag (it only closes br doesn't open br)

### snp_push_eval_pending_token
pushes eval token to stack
