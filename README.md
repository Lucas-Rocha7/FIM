# FIM
# File Integrity Monitoring System

Este projeto implementa um sistema básico de monitoramento de integridade de arquivos em Python. O sistema calcula e armazena hashes SHA-256 de arquivos em um diretório e monitora mudanças, como modificações, exclusões ou adições de arquivos.

## Funcionalidades

- Gera e compara hashes SHA-256 de arquivos
- Detecta alterações, adições e remoções de arquivos
- Salva o estado dos arquivos em um arquivo JSON para comparações futuras
- Monitoramento contínuo com intervalos de tempo ajustáveis

## Como Usar

1. Clone este repositório.
2. Defina o diretório a ser monitorado e execute o script.
3. O sistema irá verificar periodicamente as mudanças e exibir relatórios no terminal.

## Dependências

- Python 3.x
