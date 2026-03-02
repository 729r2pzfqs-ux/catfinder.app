#!/usr/bin/env python3
"""Update DE and ES homepage breed cards to match EN (larger images)."""

import re

# German breed cards
DE_BREEDS = '''<!-- Popular Breeds -->
        <section class="py-16 px-4">
            <div class="max-w-6xl mx-auto">
                <h2 class="font-display text-3xl text-slate-900 mb-2">Beliebte Rassen</h2>
                <p class="text-slate-600 mb-8">Die beliebtesten Katzenrassen weltweit</p>
                
                <div class="grid grid-cols-2 md:grid-cols-4 gap-5">
                    <a href="breeds/persian/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/persian.webp" alt="Perser" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Perser</div>
                            <div class="text-sm text-slate-500 mt-1">Sanft · Ruhig · Flauschig</div>
                        </div>
                    </a>
                    <a href="breeds/maine-coon/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/maine-coon.webp" alt="Maine Coon" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Maine Coon</div>
                            <div class="text-sm text-slate-500 mt-1">Sanfter Riese · Freundlich</div>
                        </div>
                    </a>
                    <a href="breeds/ragdoll/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/ragdoll.webp" alt="Ragdoll" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Ragdoll</div>
                            <div class="text-sm text-slate-500 mt-1">Sanftmütig · Anhänglich</div>
                        </div>
                    </a>
                    <a href="breeds/british-shorthair/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/british-shorthair.webp" alt="Britisch Kurzhaar" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Britisch Kurzhaar</div>
                            <div class="text-sm text-slate-500 mt-1">Entspannt · Treu</div>
                        </div>
                    </a>
                    <a href="breeds/siamese/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/siamese.webp" alt="Siamese" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Siamese</div>
                            <div class="text-sm text-slate-500 mt-1">Gesprächig · Sozial · Klug</div>
                        </div>
                    </a>
                    <a href="breeds/bengal/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/bengal.webp" alt="Bengal" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Bengal</div>
                            <div class="text-sm text-slate-500 mt-1">Athletisch · Wild</div>
                        </div>
                    </a>
                    <a href="breeds/sphynx/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/sphynx.webp" alt="Sphynx" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Sphynx</div>
                            <div class="text-sm text-slate-500 mt-1">Haarlos · Kuschelig</div>
                        </div>
                    </a>
                    <a href="breeds/russian-blue/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/russian-blue.webp" alt="Russisch Blau" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Russisch Blau</div>
                            <div class="text-sm text-slate-500 mt-1">Elegant · Scheu · Treu</div>
                        </div>
                    </a>
                </div>'''

# Spanish breed cards
ES_BREEDS = '''<!-- Popular Breeds -->
        <section class="py-16 px-4">
            <div class="max-w-6xl mx-auto">
                <h2 class="font-display text-3xl text-slate-900 mb-2">Razas Populares</h2>
                <p class="text-slate-600 mb-8">Las razas de gatos más queridas del mundo</p>
                
                <div class="grid grid-cols-2 md:grid-cols-4 gap-5">
                    <a href="breeds/persian/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/persian.webp" alt="Persa" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Persa</div>
                            <div class="text-sm text-slate-500 mt-1">Gentil · Tranquilo · Esponjoso</div>
                        </div>
                    </a>
                    <a href="breeds/maine-coon/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/maine-coon.webp" alt="Maine Coon" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Maine Coon</div>
                            <div class="text-sm text-slate-500 mt-1">Gigante Gentil · Amigable</div>
                        </div>
                    </a>
                    <a href="breeds/ragdoll/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/ragdoll.webp" alt="Ragdoll" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Ragdoll</div>
                            <div class="text-sm text-slate-500 mt-1">Dócil · Cariñoso</div>
                        </div>
                    </a>
                    <a href="breeds/british-shorthair/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/british-shorthair.webp" alt="Británico de Pelo Corto" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Británico de Pelo Corto</div>
                            <div class="text-sm text-slate-500 mt-1">Tranquilo · Leal</div>
                        </div>
                    </a>
                    <a href="breeds/siamese/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/siamese.webp" alt="Siamés" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Siamés</div>
                            <div class="text-sm text-slate-500 mt-1">Vocal · Social · Inteligente</div>
                        </div>
                    </a>
                    <a href="breeds/bengal/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/bengal.webp" alt="Bengalí" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Bengalí</div>
                            <div class="text-sm text-slate-500 mt-1">Atlético · Aspecto Salvaje</div>
                        </div>
                    </a>
                    <a href="breeds/sphynx/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/sphynx.webp" alt="Sphynx" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Sphynx</div>
                            <div class="text-sm text-slate-500 mt-1">Sin Pelo · Mimoso</div>
                        </div>
                    </a>
                    <a href="breeds/russian-blue/" class="bg-white rounded-2xl card-shadow border border-cream-300 hover:border-teal-300 transition group overflow-hidden">
                        <div class="aspect-[4/3] overflow-hidden">
                            <img src="../images/breeds/russian-blue.webp" alt="Azul Ruso" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-300" loading="lazy">
                        </div>
                        <div class="p-4">
                            <div class="font-semibold text-slate-800">Azul Ruso</div>
                            <div class="text-sm text-slate-500 mt-1">Elegante · Tímido · Leal</div>
                        </div>
                    </a>
                </div>'''

def update_file(filepath, new_breeds):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the Popular Breeds section
    # Pattern matches from <!-- Popular Breeds --> to the closing </div> of the grid
    pattern = r'<!-- Popular Breeds -->.*?<div class="grid grid-cols-2 md:grid-cols-4 gap-5">.*?</div>\s*</div>'
    
    content = re.sub(pattern, new_breeds + '\n            </div>', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")

def main():
    update_file('de/index.html', DE_BREEDS)
    update_file('es/index.html', ES_BREEDS)
    print("\nDone!")

if __name__ == '__main__':
    main()
