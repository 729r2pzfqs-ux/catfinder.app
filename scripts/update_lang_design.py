#!/usr/bin/env python3
"""Update DE and ES index pages with new cream/teal design."""

import re

# New tailwind config and fonts
NEW_STYLES = '''    <script src="https://cdn.tailwindcss.com"></script>
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
        .hero-gradient {
            background: linear-gradient(135deg, #f7f6f2 0%, #f3f0ec 50%, #eef8f8 100%);
        }
    </style>'''

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace old styles block
    old_pattern = r'<script src="https://cdn\.tailwindcss\.com"></script>.*?</style>'
    content = re.sub(old_pattern, NEW_STYLES, content, flags=re.DOTALL)
    
    # Update body class
    content = content.replace('class="bg-white min-h-screen', 'class="bg-cream-100 min-h-screen')
    
    # Update header
    content = content.replace('bg-white/80 backdrop-blur-md border-b border-slate-100', 
                              'bg-cream-100/80 backdrop-blur-md border-b border-cream-400/50')
    
    # Update logo gradient to solid teal
    content = content.replace('bg-gradient-to-br from-fuchsia-500 to-purple-600', 'bg-teal-500')
    content = content.replace('shadow-fuchsia-500/20', 'shadow-teal-500/20')
    
    # Update logo text
    content = content.replace('bg-gradient-to-r from-fuchsia-600 to-purple-600 bg-clip-text text-transparent', 
                              'font-display text-slate-900')
    
    # Update nav links
    content = content.replace('hover:text-fuchsia-600', 'hover:text-teal-600')
    
    # Update buttons
    content = content.replace('bg-gradient-to-r from-fuchsia-500 to-purple-600', 'bg-teal-500')
    content = content.replace('hover:shadow-fuchsia-500/25', 'hover:shadow-teal-500/25')
    content = content.replace('from-fuchsia-500', 'bg-teal-500')
    content = content.replace('to-purple-600', '')
    
    # Update dropdown
    content = content.replace('border-slate-200', 'border-cream-400')
    content = content.replace('hover:bg-slate-50', 'hover:bg-cream-100')
    content = content.replace('text-fuchsia-600', 'text-teal-600')
    
    # Update hero section
    content = content.replace('bg-fuchsia-50', 'bg-teal-50')
    content = content.replace('text-fuchsia-700', 'text-teal-700')
    content = content.replace('border-fuchsia-200/50', 'border-teal-200/50')
    content = content.replace('text-fuchsia-500', 'text-teal-500')
    
    # Update headings to use display font
    content = content.replace('font-extrabold', 'font-display')
    content = content.replace('bg-gradient-to-r from-fuchsia-600 via-purple-600 to-purple-700 bg-clip-text text-transparent', 
                              'text-slate-900')
    
    # Update search input
    content = content.replace('border-slate-200', 'border-cream-400')
    content = content.replace('focus:ring-fuchsia-500/20', 'focus:ring-teal-500/20')
    content = content.replace('focus:border-fuchsia-400', 'focus:border-teal-400')
    content = content.replace('bg-slate-100', 'bg-cream-200')
    content = content.replace('hover:bg-slate-200', 'hover:bg-cream-300')
    
    # Update primary buttons in hero
    content = content.replace('from-fuchsia-600 to-purple-600', 'bg-teal-500')
    content = content.replace('hover:from-fuchsia-500 hover:to-purple-500', 'hover:bg-teal-600')
    content = content.replace('shadow-fuchsia-500/30', 'shadow-teal-500/25')
    
    # Update secondary buttons
    content = content.replace('border-slate-300', 'border-cream-400')
    content = content.replace('hover:border-fuchsia-300', 'hover:border-teal-300')
    
    # Update cards
    content = content.replace('border-slate-200', 'border-cream-300')
    content = content.replace('hover:border-fuchsia-200', 'hover:border-teal-300')
    
    # Update feature cards
    content = content.replace('bg-fuchsia-100', 'bg-teal-100')
    content = content.replace('bg-purple-100', 'bg-teal-100')
    
    # Update icons
    content = content.replace('text-fuchsia-600', 'text-teal-600')
    content = content.replace('text-purple-600', 'text-teal-600')
    
    # Update footer
    content = content.replace('bg-slate-900', 'bg-teal-700')
    content = content.replace('text-slate-400', 'text-teal-200')
    content = content.replace('text-slate-300', 'text-cream-200')
    content = content.replace('hover:text-white', 'hover:text-white')
    
    # Clean up any remaining fuchsia/purple references
    content = content.replace('fuchsia', 'teal')
    content = content.replace('purple', 'teal')
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Updated {filepath}")

if __name__ == '__main__':
    update_file('de/index.html')
    update_file('es/index.html')
    print("Done!")
