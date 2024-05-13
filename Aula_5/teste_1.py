### LIBRARIES
None

### FUNCTIONS
def fn_check_list(list_itens):

    count_str = 0
    count_empty_space = 0
    count_num = 0
    count_int = 0
    count_float = 0

    for i in range(len(list_itens)):

        if isinstance(list_itens[i], str):
            count_str = count_str + 1    
            qtd_empty_space = str(list_itens[i]).count(" ")
            count_empty_space = count_empty_space + qtd_empty_space

        elif isinstance(list_itens[i], int):
            count_num = count_num + 1
            count_int = count_int + 1
        
        elif isinstance(list_itens[i], float):
            count_num = count_num + 1
            count_float = count_float + 1

        else:
            None

    return print(f'\nA lista possui',count_str,'strings e ao todo',count_empty_space ,'espaços em branco!'),\
           print(f'A lista possui',count_num,'números.',count_int,'inteiros e',count_float,'decimais!\n')

### EXEC.
if __name__ == "__main__":
    
    list_itens = ["teste", 
                  1, 
                  2, 
                  1.2, 
                  "O pai acordou meio pumba", 
                  4.54, 
                  "Pega na minha a balança", 
                  4, 
                  5.30, 
                  "minha casa minha vida", 
                  3, 
                  "go a head and die"]

    fn_check_list(list_itens)