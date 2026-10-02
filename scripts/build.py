#!/usr/bin/env python3
"""Regenera os artefatos derivados de evnttz-intake/SKILL.md (a fonte única):

- chatgpt-project/instrucoes.md — corpo do SKILL.md sem frontmatter, para o campo
  Instructions do ChatGPT Project
- evnttz-intake.zip — pacote de upload do Gemini (SKILL.md + references/)

Uso: python3 scripts/build.py
"""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "evnttz-intake" / "SKILL.md"
CHATGPT_OUT = ROOT / "chatgpt-project" / "instrucoes.md"
ZIP_OUT = ROOT / "evnttz-intake.zip"

GENERATED_HEADER = (
    "<!-- GERADO por scripts/build.py a partir de evnttz-intake/SKILL.md. "
    "Não edite este arquivo; edite o SKILL.md e rode o build. -->\n\n"
)


def skill_body() -> str:
    text = SKILL.read_text(encoding="utf-8")
    match = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
    if not match:
        raise SystemExit("SKILL.md sem frontmatter — corrija antes de gerar.")
    return text[match.end():].lstrip("\n")


def main() -> None:
    CHATGPT_OUT.write_text(GENERATED_HEADER + skill_body(), encoding="utf-8")

    with zipfile.ZipFile(ZIP_OUT, "w", zipfile.ZIP_DEFLATED) as bundle:
        bundle.write(SKILL, "SKILL.md")
        bundle.write(
            SKILL.parent / "references" / "contexto-evnttz.md",
            "references/contexto-evnttz.md",
        )

    print(f"gerado: {CHATGPT_OUT.relative_to(ROOT)} ({CHATGPT_OUT.stat().st_size} bytes)")
    print(f"gerado: {ZIP_OUT.relative_to(ROOT)} ({ZIP_OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
