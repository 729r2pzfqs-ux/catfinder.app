#!/usr/bin/env python3
"""Update all article pages with new cream/teal design."""

import os
import re
from pathlib import Path

# New head section with fonts and tailwind config
NEW_HEAD_STYLES = '''    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        display: ['Instrument Serif', 'Georgia', 'serif']
                    },
                    colors: {
                        cream: {
                            50: '#faf9f6',
                            100: '#f7f6f2',
                            200: '#f3f0ec',
                            300: '#edeae5',
                            400: '#dcd9d5',
                        },
                        teal: {
                            50: '#eef8f8',
                            100: '#d5eded',
                            200: '#aadada',
                            300: '#6fbfc0',
                            400: '#3da0a3',
                            500: '#01696f',
                            600: '#0c4e54',
                            700: '#0f3638',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        .card-shadow {
            box-shadow: 0 1px 3px rgba(40,37,29,0.04), 0 4px 12px rgba(40,37,29,0.03);
        }
        .card-shadow:hover {
            box-shadow: 0 4px 12px rgba(40,37,29,0.06), 0 8px 24px rgba(40,37,29,0.05);
        }
        .prose h2 { font-size: 1.5rem; font-weight: 700; margin-top: 2rem; margin-bottom: 1rem; color: #0f172a; }
        .prose h3 { font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.5rem; color: #334155; }
        .prose p { margin-bottom: 1rem; color: #475569; line-height: 1.8; }
        .prose ul { margin-left: 1.5rem; margin-bottom: 1rem; list-style: disc; color: #475569; }
        .prose li { margin-bottom: 0.5rem; }
    </style>'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace old styles block (Plus Jakarta Sans + old style)
    old_pattern = r'<script src="https://cdn\.tailwindcss\.com"></script>.*?</style>'
    content = re.sub(old_pattern, NEW_HEAD_STYLES, content, flags=re.DOTALL)
    
    # Update body class
    content = content.replace('class="bg-slate-50 text-slate-900"', 'class="bg-cream-100 min-h-screen text-slate-800"')
    content = content.replace('class="bg-white text-slate-900"', 'class="bg-cream-100 min-h-screen text-slate-800"')
    
    # Update header
    content = content.replace('bg-white border-b border-slate-200', 'bg-cream-100/80 backdrop-blur-md border-b border-cream-400/50')
    content = content.replace('bg-white border-b border-slate-100', 'bg-cream-100/80 backdrop-blur-md border-b border-cream-400/50')
    
    # Update cat icon color
    content = content.replace('text-fuchsia-600" viewBox', 'text-teal-500" viewBox')
    
    # Update logo text gradient to solid
    content = content.replace('bg-gradient-to-r from-fuchsia-600 to-purple-600 bg-clip-text text-transparent', 'font-display text-slate-900')
    
    # Update link colors
    content = content.replace('hover:text-fuchsia-600', 'hover:text-teal-600')
    content = content.replace('text-fuchsia-600 underline', 'text-teal-600 underline hover:text-teal-700')
    content = content.replace('text-fuchsia-600 font-medium', 'text-teal-600 font-medium')
    content = content.replace('text-fuchsia-600 text-sm', 'text-teal-600 text-sm')
    
    # Update article cards
    content = content.replace('hover:border-fuchsia-200', 'hover:border-teal-300')
    content = content.replace('border-slate-100', 'border-cream-300')
    content = content.replace('bg-white rounded-2xl', 'bg-white rounded-2xl card-shadow')
    
    # Update callout boxes
    content = content.replace('bg-fuchsia-50 border-l-4 border-fuchsia-500', 'bg-teal-50 border-l-4 border-teal-500')
    content = content.replace('text-fuchsia-900', 'text-teal-900')
    
    # Update colored backgrounds
    content = content.replace('bg-fuchsia-100', 'bg-teal-100')
    content = content.replace('bg-purple-100', 'bg-teal-100')
    content = content.replace('bg-rose-100', 'bg-teal-100')
    content = content.replace('bg-amber-100', 'bg-teal-100')
    content = content.replace('bg-emerald-100', 'bg-teal-100')
    
    # Update text colors
    content = content.replace('text-rose-600', 'text-teal-600')
    content = content.replace('text-purple-600', 'text-teal-600')
    content = content.replace('text-amber-600', 'text-teal-600')
    content = content.replace('text-emerald-600', 'text-teal-600')
    
    # Update footer
    content = content.replace('bg-slate-900', 'bg-teal-700')
    content = content.replace('text-slate-400', 'text-teal-200')
    content = content.replace('text-slate-300', 'text-cream-200')
    
    # Clean up remaining fuchsia/purple
    content = content.replace('fuchsia', 'teal')
    content = content.replace('purple', 'teal')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")

def main():
    articles_dir = Path('articles')
    
    # Update articles index
    index_file = articles_dir / 'index.html'
    if index_file.exists():
        update_file(index_file)
    
    # Update each article
    for article_dir in articles_dir.iterdir():
        if article_dir.is_dir():
            article_index = article_dir / 'index.html'
            if article_index.exists():
                update_file(article_index)
    
    print("\nDone! All articles updated.")

if __name__ == '__main__':
    main()
