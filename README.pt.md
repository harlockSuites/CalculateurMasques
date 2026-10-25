# Calculadora de Máscaras de Sub-rede IPv4

[Français](README.md) · [English](README.en.md) · [Español](README.es.md) · **Português** · [Italiano](README.it.md) · [Српски](README.sr.md) · [Polski](README.pl.md) · [Magyar](README.hu.md) · [Русский](README.ru.md) · [हिन्दी](README.hi.md) · [中文](README.zh.md) · [Tiếng Việt](README.vi.md) · [한국어](README.ko.md) · [日本語](README.ja.md) · [Filipino](README.fil.md)

Utilitário gráfico **offline**, gratuito e de código aberto, para calcular máscaras de sub-rede IPv4, dividir uma rede em sub-redes, manter um histórico e exportá-lo. Interface em **15 idiomas**.

Repositório: <https://github.com/harlockSuites/CalculateurMasques>

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

## Licença

Distribuído sob a licença [MIT](LICENSE) — © 2026 Harlock S.
