# Ativar GitHub Pages

Siga estes passos para ativar o GitHub Pages:

## Passo 1: Acessar Configurações

1. Acesse: https://github.com/jaccon/jcfilesizer/settings/pages
2. Ou vá para o repositório → Settings → Pages (menu lateral)

## Passo 2: Configurar Source

Em "Build and deployment":
- **Source**: Selecione "Deploy from a branch"
- **Branch**: Selecione `main`
- **Folder**: Selecione `/html` (ou `/root` se a página está na raiz)
- Clique em **Save**

## Passo 3: Aguardar Deploy

O GitHub levará alguns minutos para fazer o build e deploy.
Você verá uma mensagem como:
> Your site is live at https://jaccon.github.io/jcfilesizer/

## Passo 4: Acessar o Site

Após o deploy, acesse:
- **URL**: https://jaccon.github.io/jcfilesizer/

## Nota sobre Localização do index.html

Criei a página em `html/index.html`. Se preferir na raiz:

```bash
mv html/index.html .
rmdir html
git add .
git commit -m "Move index.html to root"
git push
```

Então configure o GitHub Pages para usar `/root` em vez de `/html`.

## Verificar Status

Você pode verificar o status do deploy em:
https://github.com/jaccon/jcfilesizer/actions

## Personalização

O arquivo `index.html` está pronto com:
- ✅ Design moderno e responsivo
- ✅ Instruções de instalação (Homebrew, pip, manual)
- ✅ Exemplos de uso
- ✅ Tabela de argumentos
- ✅ Links para o GitHub
- ✅ Features destacadas

Você pode editar o arquivo para personalizar cores, textos e conteúdo!
