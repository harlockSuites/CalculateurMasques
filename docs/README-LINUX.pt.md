# Calculadora de Máscaras de Sub-rede IPv4 — Linux

[Français](../README-LINUX.md) · [English](README-LINUX.en.md) · [Español](README-LINUX.es.md) · **Português** · [Italiano](README-LINUX.it.md) · [Српски](README-LINUX.sr.md) · [Polski](README-LINUX.pl.md) · [Magyar](README-LINUX.hu.md) · [Русский](README-LINUX.ru.md) · [हिन्दी](README-LINUX.hi.md) · [中文](README-LINUX.zh.md) · [Tiếng Việt](README-LINUX.vi.md) · [한국어](README-LINUX.ko.md) · [日本語](README-LINUX.ja.md) · [Filipino](README-LINUX.fil.md)

> **Branch `Linux`**: versão Linux do software. A branch `main` é reservada à distribuição Windows; não mescle uma na outra.

Utilitário gráfico para calcular máscaras de sub-rede IPv4, com suporte a 15 idiomas, divisão em sub-redes, histórico e exportação.

Repositório: <https://github.com/harlockSuites/CalculateurMasques/tree/Linux>

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
- Uma **máscara invertida** (wildcard, p. ex. `0.0.0.255`) é recusada com uma mensagem traduzida: informe uma máscara de sub-rede (`255.255.255.0`)
- **Roda do mouse**: rola a página, qualquer que seja o elemento sob o cursor (X11: `Button-4`/`Button-5`; Wayland: `MouseWheel`)
- Tecla **Enter** para acionar o cálculo

### Aba Divisão
- Divisão de uma rede em N sub-redes iguais
- Ou busca do CIDR mínimo para comportar N hosts
- Tabela de sub-redes com rede, máscara, hosts, broadcast
- Limite de 65.536 sub-redes por divisão (além disso, uma mensagem avisa, em vez de travar a interface)
- Clique direito em uma célula para copiar o valor

### Aba Histórico
- Cada cálculo é registrado automaticamente, com a hora em que foi feito (mantida na exibição e na exportação)
- Duplo clique em uma entrada para recarregá-la na calculadora
- Exportação **CSV** (codificação UTF-8)
- Exportação **TXT** (formato legível)

### Seletor de idioma
15 idiomas disponíveis, acessíveis a partir do cabeçalho do aplicativo:

| Grupo | Idiomas |
|---|---|
| Românicas | Français · English · Español · Português · Italiano |
| Europa Central/Oriental | Српски · Polski · Magyar · Русский |
| Sul/Leste da Ásia | हिन्दी · 中文 · Tiếng Việt · Korean (한국어) · 日本語 · Filipino |

A troca de idioma é instantânea, sem reiniciar.

### Botão Sobre
Ao lado do seletor de idioma, ele abre uma janela com o banner e a mensagem «Este software utilitário offline é gratuito e de código aberto.», traduzida para os 15 idiomas. A tecla Esc ou o botão Fechar a fecha.

### Coreano e fonte
O coreano aparece com o nome **Korean** na lista (em inglês, pois «한국어» seria exibido como quadrados sem uma fonte coreana). Se o sistema não tiver nenhuma, escolhê-lo abre uma caixa de diálogo **em inglês** («Font needed») que explica a necessidade e oferece:
- um **comando para copiar** em um terminal (instalação para todos os usuários): `sudo apt install fonts-noto-cjk` (Debian/Ubuntu), `sudo dnf install google-noto-sans-cjk-fonts` (Fedora), `sudo pacman -S noto-fonts-cjk` (Arch) — somente o comando do Debian/Ubuntu foi verificado;
- um botão **Install automatically**: baixa a Noto Sans KR (4,6 MB, licença SIL OFL, versão fixa, soma SHA-256 verificada) para `~/.local/share/fonts/calculateur-masques/`, sem direitos de administrador. É o único caso em que o software usa a rede; no restante do tempo ele permanece offline;
- um botão **Restart now**: reinicia o software (opção `--lang ko`) para que ele enxergue a fonte; o idioma muda ao reiniciar. O idioma não é lembrado de uma sessão para outra.

Para remover a fonte baixada: `rm -r ~/.local/share/fonts/calculateur-masques && fc-cache -f`.

> Os outros idiomas de escrita não latina (hindi, japonês, chinês…) não têm uma caixa desse tipo: sem uma fonte adequada, podem aparecer quadrados. Para japonês e chinês: `sudo apt install fonts-noto-cjk`.

---

## Pré-requisitos

Python 3.8+ com o módulo `tkinter`.

```bash
# Debian / Ubuntu / Linux Mint
sudo apt install python3 python3-tk

# Fedora / RHEL / CentOS
sudo dnf install python3 python3-tkinter

# Arch Linux / Manjaro
sudo pacman -S python tk

# openSUSE
sudo zypper install python3 python3-tk
```

Nenhuma outra dependência é necessária.

---

## Execução

### Método rápido

```bash
chmod +x lancer.sh
./lancer.sh
```

O script verifica automaticamente a presença do Python e do tkinter, e exibe uma mensagem de erro explícita se alguma dependência estiver faltando.

### Via Python diretamente

```bash
python3 calculateur_masques.py
```

### Via executável autônomo

Um executável autônomo (PyInstaller) é compilado com um único comando (veja «Compilar um executável autônomo» mais abaixo). Uma versão pré-compilada é publicada (como pré-lançamento) nas [Releases](https://github.com/harlockSuites/CalculateurMasques/releases) do repositório, sob uma tag `Linux-v*`; ela é construída no Debian 12 (glibc 2.36, Python 3.11, x86-64):

```bash
chmod +x CalculateurMasquesIPv4
./CalculateurMasquesIPv4
```

> **Ressalva sobre a glibc**: este binário é construído no Debian 12. Ele foi verificado nessa distribuição; deve funcionar também em distribuições com glibc 2.36 ou mais recente, mas não em uma mais antiga. Nesse caso, recompile a partir do código-fonte.

---

## Instalação no sistema (opcional)

Para integrar o aplicativo ao menu do ambiente de desktop (GNOME, KDE, XFCE…):

```bash
# Copiar os arquivos para /opt
sudo mkdir -p /opt/calculateur-masques
sudo cp calculateur_masques.py translations.py lancer.sh icon.png banner.png /opt/calculateur-masques/
sudo chmod +x /opt/calculateur-masques/lancer.sh

# Modificar o caminho no arquivo .desktop, se necessário
# Exec=bash /opt/calculateur-masques/lancer.sh

# Adicionar ao menu de aplicativos
sudo cp calculateur-masques.desktop /usr/share/applications/
sudo update-desktop-database   # Debian/Ubuntu
# ou
sudo kbuildsycoca6              # KDE Plasma
```

---

## Compilar um executável autônomo

O PyInstaller permite gerar um binário sem dependência do Python:

```bash
pip3 install pyinstaller

pyinstaller --onefile --windowed \
    --name CalculateurMasquesIPv4 \
    --add-data "translations.py:." \
    --add-data "icon.png:." \
    --add-data "banner.png:." \
    calculateur_masques.py
```

O executável será gerado em `./dist/CalculateurMasquesIPv4`. As opções `--add-data` embutem o ícone da janela (carregado em tempo de execução via Pillow, se presente, ou senão pelo Tk) e o banner da janela «Sobre»; o Pillow é opcional (`pip3 install pillow`).

> **Nota:** um binário Linux compilado no Ubuntu não funcionará necessariamente no Arch ou no Fedora, devido às diferenças de versões da glibc. Compile na distribuição de destino ou use uma imagem Docker da distribuição desejada.

---

## Estrutura dos arquivos

```
CalculateurMasques/            (branch Linux)
├── calculateur_masques.py      # Aplicativo principal (adaptado para Linux)
├── translations.py             # Dicionário dos 15 idiomas (idêntico ao da branch main)
├── icon.png                    # Ícone da janela / do menu (512 px)
├── banner.png                  # Banner da janela «Sobre» (600 x 200)
├── lancer.sh                   # Script de execução com verificação das dependências
├── calculateur-masques.desktop # Entrada de menu para ambientes de desktop
├── INSTALLER.md                # Instruções de instalação detalhadas (em francês)
├── LICENSE                     # Licença MIT
├── README-LINUX.md             # Este guia, em francês
└── docs/README-LINUX.<code>.md # Traduções: en, es, pt, it, sr, pl, hu, ru, hi, zh, vi, ko, ja, fil
```

---

## Diferenças em relação à versão Windows

| Aspecto | Windows | Linux |
|---|---|---|
| Fontes | Segoe UI / Consolas | Detecção automática (Noto Sans, DejaVu Sans, Liberation…) |
| Roda do mouse | `MouseWheel` (WinAPI) | `Button-4` / `Button-5` (X11) + `MouseWheel` (Wayland) |
| Exportação CSV | UTF-8 com BOM (Excel) | UTF-8 sem BOM (padrão) |
| Executável | `.exe` autônomo | Binário ELF via PyInstaller (depende da distro) |
| Integração com o desktop | Atalho do Windows | Arquivo `.desktop` (XDG) |

---

## Casos especiais tratados

| Prefixo | Comportamento |
|---|---|
| `/31` | Enlace ponto a ponto (RFC 3021) — 2 endereços, sem broadcast convencional |
| `/32` | Host único — primeiro = último = endereço de rede |
| `/0` | Rede universal `0.0.0.0` |

---

## Licença

Licença MIT — veja o arquivo `LICENSE`.
