import logging
import os

logger = logging.getLogger('gerador-convite')


def read_file(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.read()

        return file_content
    except Exception:
        logger.error(f"Failed to open file {file_path}")
        raise


def create_file(file_name: str, content: str):
    try:
        logger.debug(f"Creating file: {file_name}")

        with open(file_name, "w", encoding="utf-8") as file_md:
            file_md.write(content)

    except Exception:
        logger.error(f"Error creating file: {file_name}")
        raise


if __name__ == '__main__':
    convidados = [
        {'nome': 'Pessoa','numero': '+5513999999999'}
    ]

    for convidado in convidados:
        nome = convidado['nome']
        numero = convidado['numero']
        if nome is None:
            raise ValueError('Nome invalido')

        arquivo = read_file('convite-template.html')
        arquivo = arquivo.replace('$NOME_CONVIDADO', nome).replace('$NUMERO_CONVIDADO', numero).replace('$NUMERO_AJUDA', '5513999999999').replace('$URL_DO_SEU_APP_SCRIPT', 'url_gerada_pelo_app_script')

        primeiro_nome = nome.split(' ')[0].lower()

        if not os.path.exists('convites'):
            os.makedirs('convites')

        create_file(f'convites/convite_{primeiro_nome}_{numero[-4:]}.html', arquivo)
