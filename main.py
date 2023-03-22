def sintaxe_basica_str_bytes():
  texto = 'Sou uma str'
  bin = b'Sou bytes'
  return f'Representação por String: {texto} vs Representação por byte: {bin}'


def sintaxe_str_byte():
  s = 'Olá em str'
  b = b'Ola em bytes'  # acentuação não esta na tabela ASCII.
  print(s)
  print(b)

  s = "Olá em str\n"
  b = b"Ola em bytes\n"
  print(s)
  print(b)

  s = r"Olá em str\n"
  b = rb"Ola em bytes\n"
  print(s)
  print(b)

  s = f"Olá em str de {__name__}"
  # b = fb"Ola em bytes de {__name__}" # Não interpresta name.
  print(s)


def converte_byte_str():
  s = "Raphael"
  b = s.encode("utf-8")
  print(s)
  print(b)

  b = b"Raphael"
  s = b.decode("utf-8")
  print(s)
  print(b)


def sorriso():
  s = "😊"
  s = "\U0001F60A"
  # b = b"😊" Erro pois o b não interprreta o emot
  b = s.encode("utf-8")
  print(
    f'Tentando printar o {s}, que vai em string, so que em byte: {b} temos está representação'
  )
  usando = '\xf0\x9f\x98\x8a'
  print(f'Tentando manipular a representação temos como resposta: {usando}')
  print(f"Tamanho da nossa string: {len(s)=}")
  print(f"Tamanho do nosso valor em bytes: {len(b)=}")
  print(f'Listando o valores em uma lista: {list(b)}')
  print(
    'byteorder "big", o byte mais significativo está no início da matriz de bytes.',
    int.from_bytes(b, byteorder="big"))
  print(
    'byteorder "little" , o byte mais significativo está no final da matriz de bytes.',
    int.from_bytes(b, byteorder="little"))
  print(f'Convertendo o byte para UTF-8: {b.decode("utf-8")}')


def funcao_str_bytes():
  str_functions = set(dir(str))
  bytes_functions = set(dir(bytes))
  print("str e byte funções comuns:")
  for func in sorted(str_functions & bytes_functions):
    print(func)
  print()

  print("Funções str apenas: ")
  for func in sorted(str_functions - bytes_functions):
    print(func)
  print()

  print("Funções bytes apenas: ")
  for func in sorted(bytes_functions - str_functions):
    print(func)
  print()


def escrever_em_um_arquivo():
  with open("arquivo.txt", "w") as fp:
    fp.write("Sou um texto comum, em um código comum, com uma beleza comum.")
    # fp.write(b"bytes aleatorios para serem escritos") # Sem conversão erro!
    fp.write(b"Sou um texto interpretado em bytes.".decode())

  with open("arquivo.txt", "ab") as fp:
    # fp.write("Mais um texto aleatório.") # Sem conversão erro!
    fp.write(
      "Mais um texto aleatório representando uma boa e velha string.".encode())
    fp.write(b"E agora interpretado em bytes.")


def exemplo_codificar_decodificar():
  # on computer with utf-8 encoding
  s = "Hello, world! 😊"

  with open("dados.txt", "w", encoding="utf-8") as fp:
    fp.write(s)

  # OK
  with open("dados.txt", encoding="utf-8") as fp:
    print(fp.read())

  # Gera lixo no final.
  with open("dados.txt", encoding="iso-8859-1") as fp:
    print(fp.read())

  # with open("data.txt", encoding="Windows-1251") as fp:
  #     print(fp.read())

  # Obs: utf-8 está programado para se tornar o padrão no Python 3.15
  # https://peps.python.org/pep-0686/

  # Obs: in Python 3.10+ run with -X warn_default_encoding to get a warning
  # if you forget to specify encoding

  # Obs: in Python 3.7+ run with -X utf8 to assume utf-8 if not specified


def main():
  print('\nVerificando as sintaxe de str e byte:\n ')
  print(sintaxe_basica_str_bytes())
  print('Usando o conversor de Byte e String:\n')
  converte_byte_str()
  print('\nManipulação de emot(ASCII):\n ')
  sorriso()
  print('\nFunção de manipulação de String e Byte:\n')
  #funcao_str_bytes()
  escrever_em_um_arquivo()
  sintaxe_str_byte()
  exemplo_codificar_decodificar()


if __name__ == '__main__':
  main()
