#!/usr/bin/env python3
# .env Shame Detector - Because your API keys shouldn't be public confessions

import re
import sys
from pathlib import Path

# Patterns that scream "I'm about to get hacked"
SHAME_PATTERNS = {
    r'API_KEY\s*=\s*[\"\']?[A-Za-z0-9_\-]{20,}[\"\']?': 'API_KEY="YOUR_MOTHER_WOULD_BE_ASHAMED"',
    r'PASSWORD\s*=\s*[\"\']?.+[\"\']?': 'PASSWORD="hunter2_is_not_secure"',
    r'SECRET\s*=\s*[\"\']?.+[\"\']?': 'SECRET="this_should_be_in_a_vault_not_git"',
    r'TOKEN\s*=\s*[\"\']?.+[\"\']?': 'TOKEN="github_will_ban_you_for_this"',
    r'DATABASE_URL\s*=\s*[\"\']?.+[\"\']?': 'DATABASE_URL="postgres://oops:public@shame.db"',
}

def detect_shame(file_path):
    """Scans for developer shame and replaces with educational humor."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        shame_found = False
        for pattern, replacement in SHAME_PATTERNS.items():
            if re.search(pattern, content, re.IGNORECASE):
                shame_found = True
                # Replace the shameful line with funny placeholder
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                print(f"🔍 Found shame in {file_path}: {pattern.split('=')[0].strip()}")
        
        if shame_found:
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"✅ Replaced shame with wisdom in {file_path}")
            print("💡 Pro tip: Use .env.example for templates, gitignore the real .env")
            return True
        else:
            print(f"✅ No shame detected in {file_path} (surprisingly)")
            return False
            
    except FileNotFoundError:
        print(f"❌ {file_path} not found (did you forget to create it?)")
        return False

def main():
    """Main function - because every script needs one"""
    if len(sys.argv) != 2:
        print("Usage: python env_shame_detector.py <path_to_env_file>")
        print("Example: python env_shame_detector.py .env")
        sys.exit(1)
    
    env_file = sys.argv[1]
    if detect_shame(env_file):
        sys.exit(0)  # Shame was found and fixed
    else:
        sys.exit(0)  # No shame, still success (but check your backups)

if __name__ == "__main__":
    main()
