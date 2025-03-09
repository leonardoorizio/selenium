import sys
import os
from cx_Freeze import setup, Executable

# Definir o que será o executável
arquivo = 'base_func_atual_v2.py'

# Saida de arquivo

configuracao = Executable(
    script=arquivo,
    icon='Foto-de-Perfil-Leonardo.ico'
)

# Configuração do executável
setup(
    name='Bot exportação base de funcionarios atual',
    version='1.0',
    description='Bot para exportar base de funcionarios atual',
    author='Leonardo Gomes Orizio',
    options={'build_exe': {
        'include_files': arquivo,
        'include_msvcr': True,
    }},
    Executable=[configuracao]

)

# >> View -> Terminal -> python setup.py build

#Obs:Esta dando erro, precisa investigar o porque.