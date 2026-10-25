# Calculadora de Máscaras de Sub-rede IPv4

[Français](../README.md) · [English](README.en.md) · [Español](README.es.md) · **Português** · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

Utilitário gráfico **offline**, gratuito e de código aberto, para calcular máscaras de sub-rede IPv4, dividir uma rede em sub-redes, manter um histórico e exportá-lo. Interface em **15 idiomas**.

Repositório: <https://github.com/harlockSuites/CalculateurMasques>

> **Linux:** existe uma versão dedicada ao Linux no [ramo `Linux`](https://github.com/harlockSuites/CalculateurMasques/tree/Linux). Um executável pré-compilado (pré-lançamento, Debian 12, x86-64) está publicado na [release `Linux-v1.0`](https://github.com/harlockSuites/CalculateurMasques/releases/tag/Linux-v1.0). Este README descreve a versão para Windows.

---

## Visão geral

O aplicativo está organizado em três abas:

| Aba | Conteúdo |
|---|---|
| **Calculadora** | Cálculo principal, conversões de IP, verificação de pertencimento |
| **Divisão** | Divisão automática de uma rede em sub-redes |
| **Histórico** | Registro dos cálculos, exportação CSV / TXT |

---

## Funcionalidades

### Aba Calculadora
- Entrada por **prefixo CIDR** (`/24`) ou **máscara decimal** (`255.255.255.0`) — os dois se sincronizam automaticamente
- Resultados exibidos:
  - Endereço de rede
  - Máscara de sub-rede
  - Notação CIDR
  - Máscara curinga (wildcard)
  - Primeiro / Último endereço de host
  - Endereço de broadcast
  - Número de hosts utilizáveis
  - Intervalo completo da rede
- **Conversões** do endereço IP inserido: decimal pontilhada, binário, hexadecimal, decimal de 32 bits
- **Verificação de pertencimento**: testa se um determinado IP pertence à rede calculada
- **Clique direito** em qualquer valor para copiá-lo para a área de transferência
- Tecla **Enter** para acionar o cálculo

### Aba Divisão
- Divisão de uma rede em N sub-redes iguais
- Ou busca do CIDR mínimo para comportar N hosts
- Tabela de sub-redes com rede, máscara, hosts, broadcast (limitada a 65.536 linhas, com uma mensagem no idioma escolhido além desse limite)
- Clique direito em uma célula para copiar o valor

### Aba Histórico
- Cada cálculo é registrado automaticamente, com a hora do cálculo
- Duplo clique em uma entrada para recarregá-la na calculadora
- Exportação **CSV** (codificação UTF-8 com BOM, compatível com Excel)
- Exportação **TXT** (formato legível)

### Seletor de idioma
15 idiomas disponíveis, acessíveis a partir do cabeçalho do aplicativo:

| Grupo | Idiomas |
|---|---|
| Românicas | Français · English · Español · Português · Italiano |
| Europa Central/Oriental | Српски · Polski · Magyar · Русский |
| Sul/Leste da Ásia | हिन्दी · 中文 · Tiếng Việt · 한국어 · 日本語 · Filipino |

A troca de idioma é instantânea, sem reiniciar.

### Botão Sobre
Ao lado do seletor de idioma, o botão **Sobre** abre uma janela com o banner do autor (`banner.png`) e a mensagem «Este software utilitário offline é gratuito e de código aberto.», traduzida para os 15 idiomas.

---

## Pré-requisitos

- **Windows 10 / 11**
- **Python 3.8+** — [python.org](https://www.python.org/downloads/)
- Módulo `tkinter` (incluído na instalação padrão do Python)

Nenhuma dependência externa é necessária para executar o script. [Pillow](https://pypi.org/project/pillow/) é opcional: serve apenas para exibir o ícone da janela em resolução total.

---

## Execução

### Via Python
```
python calculateur_masques.py
```

### Via executável compilado
Dê um duplo clique em `dist\CalculateurMasquesIPv4.exe`. O executável é autônomo, sem instalação. Ele não é versionado neste repositório: compile-o (veja abaixo).

---

## Compilar o executável

O repositório fornece uma spec do PyInstaller (`CalculateurMasquesIPv4.spec`) que incorpora o ícone, o banner e as traduções. A partir desta pasta:

```
pip install pyinstaller pillow
python -m PyInstaller --clean --noconfirm CalculateurMasquesIPv4.spec
```

O executável é gerado na pasta `dist\`. O ícone (`icon.ico`) é integrado ao exe.

---

## Estrutura dos arquivos

```
CalculateurMasques\
├── calculateur_masques.py        # Aplicativo principal
├── translations.py               # Dicionário dos 15 idiomas
├── CalculateurMasquesIPv4.spec   # Especificação do PyInstaller
├── icon.ico                      # Ícone do exe (Windows)
├── icon.png                      # Ícone da janela (512 px)
├── banner.png                    # Banner da janela Sobre (600 px)
├── LICENSE                       # Licença MIT
└── README.md
```

---

## Casos especiais tratados

| Prefixo | Comportamento |
|---|---|
| `/31` | Enlace ponto a ponto (RFC 3021) — 2 endereços, sem broadcast convencional |
| `/32` | Host único — primeiro = último = endereço de rede |
| `/0` | Rede universal `0.0.0.0` |

---

## Antivírus e falsos positivos

Em 25 de outubro de 2026, o VirusTotal sinaliza o executável `CalculateurMasquesIPv4.exe` da versão 1.0 com **5 detecções em 69 mecanismos**: Arctic Wolf, Bkav Pro, Microsoft, SecureAge e Zillya. Acreditamos que sejam **falsos positivos**, comuns em um programa Python empacotado com PyInstaller, recente e sem assinatura digital. O programa não contém nenhum código de rede (usa apenas `tkinter`, `ipaddress`, `csv`, `datetime`, `math`, `sys` e `os`, além do Pillow para o ícone da janela) e todo o seu código-fonte é público neste repositório.

Relatos de falsos positivos foram enviados em 25 de outubro de 2026 aos cinco fornecedores envolvidos. Esta seção será atualizada com as respostas deles.

Para verificar o seu download:

- SHA-256 (v1.0): `6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f`
- Relatório do VirusTotal: <https://www.virustotal.com/gui/file/6e1c6d50e0232f7ca9b547336251c379ea9c607214b47540b8ad3368933b3d7f>
- SHA-256 (v1.1): `bddbfc4ce674cffa78f0a18cb7e9554d2f2fe3ced46cd1cfb99ae907e9001d65`
- Você também pode compilar o executável por conta própria a partir do código-fonte (veja «Compilar o executável»).

---

## Licença

Distribuído sob a licença [MIT](../LICENSE) — © 2026 Harlock S.
