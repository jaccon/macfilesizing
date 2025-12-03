# macFileSizing 📊

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey.svg)

**Uma ferramenta de linha de comando poderosa e intuitiva para analisar o uso de espaço em disco**

[Características](#características) •
[Instalação](#instalação) •
[Uso](#uso) •
[Exemplos](#exemplos) •
[Contribuir](#contribuir)

</div>

---

## 📖 Sobre o Projeto

**macFileSizing** é uma ferramenta open source desenvolvida em Python que permite analisar e visualizar o uso de espaço em disco de forma clara e organizada. Ideal para identificar rapidamente quais arquivos e diretórios estão consumindo mais espaço no seu sistema.

### 🎯 Para que serve?

- **Liberar espaço em disco**: Identifique rapidamente os maiores arquivos e pastas
- **Análise de projetos**: Descubra quais componentes do seu projeto ocupam mais espaço
- **Auditoria de armazenamento**: Gere relatórios detalhados sobre o uso de disco
- **Limpeza de sistema**: Encontre arquivos grandes esquecidos em diretórios profundos
- **Otimização**: Tome decisões informadas sobre o que manter ou remover

## ✨ Características

- 📊 **Listagem ordenada por tamanho** - Visualize arquivos e diretórios do maior para o menor
- 🌲 **Modo recursivo (tree)** - Escaneie toda a árvore de diretórios profundamente
- 📄 **Exportação de relatórios** - Salve análises em arquivos de texto para referência futura
- 📈 **Barra de progresso** - Acompanhe o progresso da análise com feedback visual
- 💾 **Formatação inteligente** - Tamanhos exibidos em formato legível (B, KB, MB, GB, TB, PB)
- 🚀 **Performance otimizada** - Análise rápida mesmo em diretórios grandes
- 🛡️ **Tratamento de erros** - Ignora automaticamente arquivos sem permissão de acesso
- 🎨 **Interface limpa** - Output organizado e fácil de ler

## 📦 Instalação

### Opção 1: Homebrew (Recomendado para macOS)

A forma mais simples de instalar o macFileSizing no macOS é através do Homebrew:

```bash
# Adicione o tap do repositório
brew tap jaccon/tap

# Instale o macFileSizing
brew install macfilesizing
```

Após a instalação, o comando estará disponível globalmente:

```bash
macfilesizing --source /caminho/do/diretorio
```

**Vantagens do Homebrew:**
- ✅ Instalação com um único comando
- ✅ Gerenciamento automático de dependências
- ✅ Atualizações fáceis com `brew upgrade`
- ✅ Desinstalação limpa com `brew uninstall`
- ✅ Ambiente virtual Python isolado

### Opção 2: pip install

Instale diretamente do repositório GitHub usando pip:

```bash
pip install git+https://github.com/jaccon/macfilesizing.git
```

Depois use o comando:

```bash
macfilesizing --source /caminho/do/diretorio
```

### Opção 3: Instalação Manual

Clone o repositório e instale as dependências:

```bash
# Clone o repositório
git clone https://github.com/jaccon/macfilesizing.git
cd macfilesizing

# Instale as dependências
pip install -r requirements.txt

# (Opcional) Torne o script executável
chmod +x macFileSizing.py
```

Execute diretamente:

```bash
python3 macFileSizing.py --source /caminho/do/diretorio
```

## 🚀 Uso

### Sintaxe Básica

```bash
macfilesizing --source <caminho> [opções]
```

### Argumentos de Linha de Comando

| Argumento | Obrigatório | Descrição |
|-----------|-------------|-----------|
| `--source` | ✅ Sim | Caminho do diretório a ser analisado |
| `--tree` | ❌ Não | Escaneia recursivamente todos os subdiretórios |
| `--report` | ❌ Não | Caminho para salvar o relatório em arquivo |

### Comandos Básicos

#### 1. Análise Simples

Lista arquivos e diretórios no nível raiz:

```bash
macfilesizing --source ~/Downloads
```

#### 2. Análise Recursiva (Modo Tree)

Escaneia toda a árvore de diretórios:

```bash
macfilesizing --source ~/Documents --tree
```

#### 3. Gerar Relatório

Salva a análise em um arquivo de texto:

```bash
macfilesizing --source ~/Projects --report ~/relatorio_projetos.txt
```

#### 4. Análise Completa

Combina todas as opções:

```bash
macfilesizing --source ~/Documents --tree --report ~/analise_completa.txt
```

## 📋 Exemplos Práticos

### Exemplo 1: Analisar pasta de Downloads

```bash
macfilesizing --source ~/Downloads
```

**Saída esperada:**
```
Analyzing directory: /Users/usuario/Downloads
Please wait, calculating sizes...

Type   Size         Name
--------------------------------------------------------------------------------
DIR    2.45 GB      projeto_grande
FILE   856.32 MB    video.mp4
DIR    345.67 MB    documentos
FILE   123.45 MB    arquivo.zip
FILE   45.12 MB     apresentacao.pptx
--------------------------------------------------------------------------------
Total: 3.75 GB
Items found: 5
```

### Exemplo 2: Análise recursiva de projetos

```bash
macfilesizing --source ~/Projects --tree --report ~/analise_projetos.txt
```

Este comando:
- Escaneia recursivamente todos os arquivos em `~/Projects`
- Mostra o caminho relativo de cada item
- Salva o resultado em `~/analise_projetos.txt`

### Exemplo 3: Encontrar arquivos grandes no sistema

```bash
macfilesizing --source / --tree --report ~/sistema_completo.txt
```

⚠️ **Nota**: Análise do sistema completo pode demorar e requer permissões adequadas.

### Exemplo 4: Analisar diretório atual

```bash
macfilesizing --source .
```

### Exemplo 5: Analisar com caminho absoluto

```bash
macfilesizing --source /Users/usuario/Library/Caches
```

## 📊 Formato de Saída

### Saída no Terminal

A ferramenta exibe:

- **Type**: Tipo do item (`FILE` para arquivo, `DIR` para diretório)
- **Size**: Tamanho formatado automaticamente (B, KB, MB, GB, TB, PB)
- **Name/Path**: Nome do item (modo básico) ou caminho relativo (modo tree)
- **Total**: Soma total de todos os itens analisados
- **Items found**: Quantidade de itens encontrados

### Formato do Relatório

Quando você usa a opção `--report`, o arquivo gerado inclui:

```
File Sizing Report
Generated: 2025-12-03 14:30:45
================================================================================

Analyzing directory: /Users/usuario/Documents
Mode: Recursive (tree mode)
Please wait, calculating sizes...

Type   Size         Path
--------------------------------------------------------------------------------
DIR    2.45 GB      Projetos/webapp
FILE   856.32 MB    Videos/apresentacao.mp4
DIR    543.21 MB    Projetos/mobile-app
FILE   234.56 MB    Backups/backup_2024.zip
...
--------------------------------------------------------------------------------
Total: 10.23 GB
Items found: 1523
```

## 💡 Dicas de Uso

1. **Use o modo tree para análise profunda**
   ```bash
   macfilesizing --source ~/Documents --tree
   ```

2. **Salve saídas grandes em arquivo**
   ```bash
   macfilesizing --source / --tree --report ~/analise_sistema.txt
   ```

3. **Atalhos de caminho**
   - `~` para diretório home
   - `.` para diretório atual
   - `..` para diretório pai

4. **Combine com outros comandos**
   ```bash
   # Analise e visualize com less
   macfilesizing --source ~/Documents --tree --report /tmp/report.txt && less /tmp/report.txt
   ```

5. **Automatize análises periódicas**
   ```bash
   # Adicione ao crontab para análise semanal
   0 0 * * 0 macfilesizing --source ~/Documents --tree --report ~/relatorios/semanal_$(date +\%Y\%m\%d).txt
   ```

## 🔧 Solução de Problemas

### Erro: Permission Denied

**Problema**: Erro de permissão ao acessar alguns arquivos.

**Solução**: A ferramenta automaticamente ignora arquivos sem permissão. Se precisar analisar diretórios do sistema, execute com privilégios adequados:

```bash
sudo macfilesizing --source /var/log
```

### Erro: tqdm not found

**Problema**: Módulo tqdm não encontrado.

**Solução**: Instale a dependência:

```bash
pip install tqdm
```

### Diretório do relatório não existe

**Problema**: Caminho do relatório inválido.

**Solução**: A ferramenta cria automaticamente os diretórios necessários. Certifique-se de ter permissão de escrita no local.

### Análise muito lenta

**Problema**: Análise demorando muito tempo.

**Solução**: 
- Evite analisar o sistema completo (`/`)
- Use análise não-recursiva primeiro para identificar diretórios grandes
- Exclua diretórios de sistema conhecidos

## 🛠️ Requisitos

- **Python**: 3.6 ou superior
- **Dependências**: 
  - `tqdm` - Barra de progresso

## 📚 Casos de Uso

### Desenvolvimento de Software

```bash
# Identifique dependências pesadas no projeto
macfilesizing --source ./node_modules --tree --report node_modules_analysis.txt
```

### Limpeza de Sistema

```bash
# Encontre caches grandes
macfilesizing --source ~/Library/Caches --tree
```

### Backup e Arquivamento

```bash
# Analise antes de fazer backup
macfilesizing --source ~/Documents --tree --report pre_backup_report.txt
```

### Auditoria de Servidor

```bash
# Monitore uso de disco em servidores
macfilesizing --source /var/www --tree --report /var/log/disk_usage.txt
```

## 🤝 Contribuir

Contribuições são bem-vindas! Sinta-se à vontade para:

- 🐛 Reportar bugs
- 💡 Sugerir novas funcionalidades
- 🔧 Enviar pull requests
- 📖 Melhorar a documentação

### Como Contribuir

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Desenvolvido por **Jaccon** - [@jaccon](https://github.com/jaccon)

## 🌟 Mostre seu Apoio

Se este projeto foi útil para você, considere dar uma ⭐️ no repositório!

---

<div align="center">

**[⬆ Voltar ao topo](#macfilesizing-)**

Feito com ❤️ por [Jaccon](https://github.com/jaccon)

</div>
