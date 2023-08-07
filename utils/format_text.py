# Formatação do Nome
def formatName(text):
    formattedName = text.title()
    return formattedName


# Formatação do CPF
def formatCPF(text):
    formattedCpf = f"{text[:3]}.{text[3:6]}.{text[6:9]}-{text[9:]}"
    return formattedCpf


# Formatação do RG
def formatRg(text):
    formattedRg = f"{text[:3]}.{text[3:6]}.{text[6:9]}-{text[9:]}"
    return formattedRg
