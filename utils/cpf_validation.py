from validate_docbr import CPF
# from utils.format_text import formatCPF

def cpfValidator():
    validatedCpf = CPF()


    while True:
        cpf = input("CPF: ")
        validity = validatedCpf.validate(cpf)
        if validity:
            if len(cpf) > 11:
                return cpf
            else:
                return validatedCpf.mask(cpf)
        else:
            print("CPF inválido! Tente novamente:")




def gera_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return cpf_gerado
