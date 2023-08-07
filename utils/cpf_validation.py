from validate_docbr import CPF
from utils.format_text import formatCPF

def cpfValidator():
    validatedCpf = CPF()


    while True:
        cpf = input("CPF: ")
        validity = validatedCpf.validate(cpf)
        if validity:
            return formatCPF(cpf)
        else:
            print("CPF inválido! Tente novamente:")




def gera_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return cpf_gerado
