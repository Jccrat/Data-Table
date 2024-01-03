# neste arquivo, criamos algumas linhas de código para mapear
# e anotar as instâncias da classe. Isso nos permitirá acessar
# facilmente cada instância quando precisarmos mudar alguma coisa

global control_reference
control_reference={}

def add_to_control_reference(key, value):
    #Esta função será chamada antes de criar uma instância de uma classe. 
    # Ele recebe dois argumentos, uma chave e um valor,que serão emparelhados
    # no ditado global como uma chave: par de valores
    
    global control_reference
    try:
        control_reference[key]= value 
    except KeyError as e:
        print(e)
    finally:
        pass
    
# podemos criar outra função que retorne o dict

def return_control_reference():
    global control_reference
    return control_reference