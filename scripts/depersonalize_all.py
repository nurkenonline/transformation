import os
import re

# Precise replacement dictionary
# Order matters: longest/most specific patterns first!
REPLACEMENTS = [
    # Full official legal names
    (r'Некоммерческого акционерного общества «Казахский национальный педагогический университет имени Абая»', r'[V_LEGAL_FORM] «[V_UNIVERSITY_FULL_NAME]»'),
    (r'Некоммерческое акционерное общество «Казахский национальный педагогический университет имени Абая»', r'[V_LEGAL_FORM] «[V_UNIVERSITY_FULL_NAME]»'),
    (r'НАО «Казахский национальный педагогический университет имени Абая»', r'[V_LEGAL_FORM] «[V_UNIVERSITY_FULL_NAME]»'),
    (r'НАО «КазНПУ имени Абая»', r'[V_UNIVERSITY_SHORT_NAME]'),
    (r'«КазНПУ имени Абая»', r'«[V_UNIVERSITY_SHORT_NAME]»'),
    (r'КазНПУ имени Абая', r'[V_UNIVERSITY_SHORT_NAME]'),
    (r'КазНПУ', r'[V_UNIVERSITY_SHORT_NAME]'),
    
    # Platform / SIS system names
    (r'АИС «Цифровая платформа Abai Digital»', r'АИС «[V_SIS_SYSTEM_NAME]»'),
    (r'«Цифровая платформа Abai Digital»', r'«[V_SIS_SYSTEM_NAME]»'),
    (r'Цифровая платформа Abai Digital', r'Цифровая платформа [V_SIS_SYSTEM_NAME]'),
    (r'платформы Abai Digital', r'платформы [V_SIS_SYSTEM_NAME]'),
    (r'платформе Abai Digital', r'платформе [V_SIS_SYSTEM_NAME]'),
    (r'платформу Abai Digital', r'платформу [V_SIS_SYSTEM_NAME]'),
    (r'системе Abai Digital', r'системе [V_SIS_SYSTEM_NAME]'),
    (r'системы Abai Digital', r'системы [V_SIS_SYSTEM_NAME]'),
    (r'в Abai Digital', r'в [V_SIS_SYSTEM_NAME]'),
    (r'Abai Digital', r'[V_SIS_SYSTEM_NAME]'),
    (r'RegAbai', r'[V_ADMISSION_MODULE]'),
    
    # Generic English brand references
    (r'Abai University Transformation', r'University Governance & Transformation Framework'),
    (r'Abai University', r'[V_UNIVERSITY_SHORT_NAME]'),
]

# Exceptions where Abai University is specifically cited as a Reference Case
# e.g. "Reference Case: Abai University", "на примере Abai University", etc.
REF_CASE_PRESERVATIONS = [
    (r'Reference Case:\s*\[V_UNIVERSITY_SHORT_NAME\]', 'Reference Case: Abai University'),
    (r'Reference Case 1:\s*\[V_UNIVERSITY_SHORT_NAME\]', 'Reference Case 1: Abai University'),
    (r'Кейс:\s*\[V_UNIVERSITY_SHORT_NAME\]', 'Кейс: Abai University'),
    (r'на примере\s*\[V_UNIVERSITY_SHORT_NAME\]', 'на примере Abai University'),
    (r'опыта\s*\[V_UNIVERSITY_SHORT_NAME\]', 'опыта Abai University'),
]

def process_content(text, filepath):
    # Do not replace within URLs pointing to existing files/folders
    # We replace text lines
    lines = text.split('\n')
    new_lines = []
    
    for line in lines:
        # If line contains link to workspace ABAI_, preserve the link url
        # but replace link label if needed
        modified_line = line
        
        for pat, repl in REPLACEMENTS:
            # Avoid replacing inside markdown link URLs like (file:///.../workspace/ABAI_...)
            # We split by (file:/// or (../ or (workspace/
            parts = re.split(r'(\]\([^\)]+\))', modified_line)
            new_parts = []
            for part in parts:
                if part.startswith('](') and part.endswith(')'):
                    # It's a link URL. Check if we need to depersonalize file names or keep them
                    # If it's a workspace link or existing file, keep target path
                    new_parts.append(part)
                else:
                    new_parts.append(re.sub(pat, repl, part))
            modified_line = ''.join(new_parts)
            
        # Restore explicit reference cases if any got over-replaced
        for pat, repl in REF_CASE_PRESERVATIONS:
            modified_line = re.sub(pat, repl, modified_line)
            
        new_lines.append(modified_line)
        
    return '\n'.join(new_lines)

def run():
    target_dirs = [
        'docs/regulations',
        'docs/internal_acts'
    ]
    
    processed_files = 0
    changed_files = 0
    
    for td in target_dirs:
        for root, _, files in os.walk(td):
            for f in files:
                if f.endswith('.md'):
                    fp = os.path.join(root, f)
                    processed_files += 1
                    with open(fp, 'r', encoding='utf-8') as fh:
                        orig = fh.read()
                    
                    updated = process_content(orig, fp)
                    if updated != orig:
                        changed_files += 1
                        with open(fp, 'w', encoding='utf-8') as fh:
                            fh.write(updated)
                        print(f"Updated: {fp}")

    print(f"\nDone. Processed: {processed_files} files. Changed: {changed_files} files.")

if __name__ == '__main__':
    run()
