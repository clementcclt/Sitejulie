#!/usr/bin/env python3
"""
Script pour corriger les liens de navigation pour GitHub Pages.
Les liens absolus (/page) doivent devenir relatifs (page.html).
"""

import os
import re
from pathlib import Path

# Mapping des liens absolus vers relatifs pour les pages principales (à la racine)
LINKS_ROOT = {
    'href="/"': 'href="index.html"',
    "href='/'": "href='index.html'",
    'href="/votre-chiropracteur"': 'href="votre-chiropracteur.html"',
    'href="/les-traitements"': 'href="les-traitements.html"',
    'href="/articles"': 'href="articles.html"',
    'href="/informations-pratiques"': 'href="informations-pratiques.html"',
    'href="/prendre-rdv"': 'href="prendre-rdv.html"',
    'href="/faq"': 'href="faq.html"',
}

# Mapping des liens absolus vers relatifs pour les articles (dans articles/)
LINKS_ARTICLES = {
    'href="/"': 'href="../index.html"',
    "href='/'": "href='../index.html'",
    'href="/votre-chiropracteur"': 'href="../votre-chiropracteur.html"',
    'href="/les-traitements"': 'href="../les-traitements.html"',
    'href="/articles"': 'href="../articles.html"',
    'href="/informations-pratiques"': 'href="../informations-pratiques.html"',
    'href="/prendre-rdv"': 'href="../prendre-rdv.html"',
    'href="/faq"': 'href="../faq.html"',
}

def fix_links(filepath, is_article=False):
    """Corrige les liens dans un fichier HTML."""
    print(f"Traitement de: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    links = LINKS_ARTICLES if is_article else LINKS_ROOT

    for old_link, new_link in links.items():
        content = content.replace(old_link, new_link)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  -> Liens corriges")
    else:
        print(f"  -> Aucun changement")

def main():
    base_dir = Path("/home/user/Sitejulie")

    # Traiter les pages principales à la racine
    print("=" * 60)
    print("PAGES PRINCIPALES")
    print("=" * 60)
    root_html_files = list(base_dir.glob("*.html"))
    for filepath in sorted(root_html_files):
        fix_links(filepath, is_article=False)

    # Traiter les articles
    print("\n" + "=" * 60)
    print("ARTICLES")
    print("=" * 60)
    articles_dir = base_dir / "articles"
    if articles_dir.exists():
        article_files = list(articles_dir.glob("*.html"))
        for filepath in sorted(article_files):
            fix_links(filepath, is_article=True)

    print("\n" + "=" * 60)
    print("Traitement termine!")

if __name__ == "__main__":
    main()
