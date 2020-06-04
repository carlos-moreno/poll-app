# Polls

Sistema de votação desenvolvido com base no tutorial do Django.


## Como rodar a aplicação?
1 - Clone o repositório.
```console
git clone https://github.com/carlos-moreno/poll-app.git
```
2 - Crie um virtualenv com Python 3.6+
```console
cd poll-app && python -m venv venv
```
3 - Ative o virtualenv (O comando abaixo é utilizado em hosts linux).
```console
source .venv/bin/activate
```
4 - Instale as dependências.
```console
pip install -r requirements.txt
```
5 - Configure a instância com o .env
```console
cp contrib/env-sample .env
```
6 - Execute os testes.
```console
python manage.py test
```
