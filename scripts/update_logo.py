#!/usr/bin/env python3
"""Update CatFinder logo to use Lucide cat icon in gradient box"""

import os
import re

BASE_DIR = os.path.expanduser("~/clawd/catfinder.app")

# Old logo patterns (both w-7 and w-8 versions)
OLD_LOGO_PATTERNS = [
    r'<svg class="w-8 h-8 text-fuchsia-600"[^>]*>.*?</svg>',
    r'<svg class="w-7 h-7 text-fuchsia-600"[^>]*>.*?</svg>',
]

# New logo (Lucide cat icon in gradient box)
NEW_LOGO = '''<div class="w-10 h-10 bg-gradient-to-br from-fuchsia-500 to-purple-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-fuchsia-500/20">
                    <i data-lucide="cat" class="w-6 h-6"></i>
                </div>'''

def update_file(filepath):
    """Update logo in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Try each pattern
        for pattern in OLD_LOGO_PATTERNS:
            content = re.sub(pattern, NEW_LOGO, content, flags=re.DOTALL)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "updated"
        
        return False, "no old logo"
        
    except Exception as e:
        return False, str(e)

def main():
    print("🐱 Updating CatFinder logo to Lucide version...")
    print()
    
    updated = 0
    skipped = 0
    errors = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, BASE_DIR)
                
                success, status = update_file(filepath)
                
                if success:
                    print(f"✅ {rel_path}")
                    updated += 1
                elif status == "no old logo":
                    skipped += 1
                else:
                    print(f"❌ {rel_path}: {status}")
                    errors.append(rel_path)
    
    print()
    print(f"{'='*50}")
    print(f"✅ Updated: {updated}")
    print(f"⏭️  Skipped (already updated): {skipped}")
    if errors:
        print(f"❌ Errors: {len(errors)}")

if __name__ == "__main__":
    main()
