#!/bin/bash
# A small TeX Live (scheme-basic plus the packages the print PDF uses) in a folder of one's own, no root needed:
# LuaLaTeX, which pipeline/pdf.py prefers (microtype's font expansion), TeX Gyre Pagella and GFS Didot.
#   scripts/install-texlive.sh [PREFIX]          (default ~/texlive; then put PREFIX/bin/x86_64-linux on the PATH)
# Used by .github/workflows/pages.yml and release.yml (cached); also runs under WSL on Windows.
set -euo pipefail
PREFIX="${1:-$HOME/texlive}"
BIN="$PREFIX/bin/x86_64-linux"
if [ ! -x "$BIN/lualatex" ]; then
  work="$(mktemp -d)"
  curl -fsSL -o "$work/install-tl-unx.tar.gz" https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
  tar -xzf "$work/install-tl-unx.tar.gz" -C "$work"
  cat > "$work/texlive.profile" <<EOF
selected_scheme scheme-basic
TEXDIR $PREFIX
TEXMFLOCAL $PREFIX/texmf-local
TEXMFSYSCONFIG $PREFIX/texmf-config
TEXMFSYSVAR $PREFIX/texmf-var
TEXMFHOME $PREFIX/texmf-home
binary_x86_64-linux 1
instopt_adjustpath 0
tlpdbopt_install_docfiles 0
tlpdbopt_install_srcfiles 0
tlpdbopt_autobackup 0
EOF
  perl "$work"/install-tl-*/install-tl --no-interaction --profile "$work/texlive.profile"
  rm -rf "$work"
fi
PACKAGES="collection-luatex collection-latexrecommended collection-fontsrecommended
  memoir lettrine footmisc bigfoot etoolbox iftex babel-latin hyphen-latin tex-gyre fontspec newunicodechar
  gfsdidot greek-fontenc greek-inputenc cbfonts cbfonts-fd microtype graphics hyperref url float tools"
# Once these are in, nothing is fetched again (a cached install keeps working after CTAN moves to a new year)
if [ "$(cat "$PREFIX/.castellio-packages" 2>/dev/null)" != "$PACKAGES" ]; then
  # shellcheck disable=SC2086
  "$BIN/tlmgr" install $PACKAGES
  printf '%s' "$PACKAGES" > "$PREFIX/.castellio-packages"
fi
echo "TeX Live in $PREFIX: put $BIN on the PATH"
