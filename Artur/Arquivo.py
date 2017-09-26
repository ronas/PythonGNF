#Na linha abaixo há uma leitura da variável nomearquivo. 

nomearquivo = input("Qual é o nome do arquivo?")

#O ponteiro guarda o endereço lógico do arquivo no disco,o open cria o arquivo.
#O W diz indica qu e você quer escrever algo(Write).

ponteiro = open(nomearquivo,'w')       

#Aqui abaixo o input está sendo usado para ler a variavel texto guardado.

textoguardado = input("Qual o texto que o senhor deseja guardar?")

#O write está indicando que é para escrever o texto guardado no arquivo criado na variavel poneteiro. 

ponteiro.write(textoguardado)

#O close está indicando que é para fechar o arquivo. 

ponteiro.close()

print("Parabéns,você fez seu arquivo!")



