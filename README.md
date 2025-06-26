# Django Ecommerce Website

Este projeto é um site de e-commerce desenvolvido com Django.

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   ```
2. **Acesse a pasta do projeto:**
   ```bash
   cd django_ecommerce_website/ecommerce
   ```
3. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
4. **Instale as dependências:**
   ```bash
   pip install django
   ```
5. **Rode as migrações:**
   ```bash
   python manage.py migrate
   ```
6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```
7. **Acesse no navegador:**
   - http://127.0.0.1:8000/

## Estrutura do Projeto

- `ecommerce/` - Projeto Django principal
- `store/` - Aplicação de loja
- `static/` - Arquivos estáticos (CSS, imagens)
- `templates/` - Templates HTML

## Funcionalidades
- Listagem de produtos
- Carrinho de compras
- Checkout com formulário de usuário e endereço

## Observações
- Para que as imagens dos produtos apareçam, coloque os arquivos em `ecommerce/static/images/`.
- O botão "Paypal Options" só aparece após a submissão do formulário de checkout.

---

Projeto para fins de estudo com Django paseado nos videos da serie Django Ecommerce Website de Dennis Ivy no youtube.