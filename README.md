# Poll-App
[![Build Status](https://travis-ci.org/carlos-moreno/poll-app.svg?branch=master)](https://travis-ci.org/carlos-moreno/poll-app)
[![Maintainability](https://api.codeclimate.com/v1/badges/5022e5360597bb0762ae/maintainability)](https://codeclimate.com/github/carlos-moreno/poll-app/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5022e5360597bb0762ae/test_coverage)](https://codeclimate.com/github/carlos-moreno/poll-app/test_coverage)
[![Updates](https://pyup.io/repos/github/carlos-moreno/poll-app/shield.svg)](https://pyup.io/repos/github/carlos-moreno/poll-app/)
[![Python 3](https://pyup.io/repos/github/carlos-moreno/poll-app/python-3-shield.svg)](https://pyup.io/repos/github/carlos-moreno/poll-app/)


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
