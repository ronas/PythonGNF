def GravarRegistro(prmCodigo,prmNome,prmValor):        
    ponteiro = open('BancoDados.db','a')     
    ponteiro.write(prmCodigo+'|'+prmNome+'|'+prmValor+'\n')
    ponteiro.close()
    return  