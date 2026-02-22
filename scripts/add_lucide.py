#!/usr/bin/env python3
"""Add Lucide script to all HTML files that use data-lucide icons"""

import os

BASE_DIR = os.path.expanduser("~/clawd/catfinder.app")

LUCIDE_SCRIPT = '''<script src="https://unpkg.com/lucide@latest"></script>
    <script>lucide.createIcons();</script>
</body>'''

def update_file(filepath):
    """Add Lucide script to file if needed"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if uses lucide but doesn't have the script
        if 'data-lucide=' in content and 'unpkg.com/lucide' not in content:
            # Add script before </body>
            new_content = content.replace('</body>', LUCIDE_SCRIPT)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True, "added"
        
        return False, "skipped"
        
    except Exception as e:
        return False, str(e)

def main():
    print("🐱 Adding Lucide script to CatFinder pages...")
    print()
    
    updated = 0
    skipped = 0
    
    for root, dirs, files in os.walk(BASE_DIR):
        for filename in files:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                rel_path = os.path.relpath(filepath, BASE_DIR)
                
                success, status = update_file(filepath)
                
                if success:
                    print(f"✅ {rel_path}")
                    updated += 1
                else:
                    skipped += 1
    
    print()
    print(f"{'='*50}")
    print(f"✅ Updated: {updated}")
    print(f"⏭️  Skipped: {skipped}")

if __name__ == "__main__":
    main()
