#!/usr/bin/env python3
"""
Quick validation script for skills

Usage:
    quick_validate.py <skill_directory>
"""

import sys
import re
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def parse_frontmatter(content):
    """Parse YAML frontmatter without requiring PyYAML."""
    if not content.startswith('---'):
        return None, "No YAML frontmatter found"

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, "Invalid frontmatter format"

    text = match.group(1)

    if HAS_YAML:
        try:
            data = yaml.safe_load(text)
            if not isinstance(data, dict):
                return None, "Frontmatter must be a YAML dictionary"
            return data, None
        except yaml.YAMLError as e:
            return None, f"Invalid YAML: {e}"

    # Simple fallback parser for name/description
    data = {}
    for line in text.split('\n'):
        line = line.strip()
        if ':' in line:
            key, _, value = line.partition(':')
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data, None


def validate_skill(skill_path):
    skill_path = Path(skill_path)

    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()
    frontmatter, error = parse_frontmatter(content)
    if error:
        return False, error

    allowed = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}
    unexpected = set(frontmatter.keys()) - allowed
    if unexpected:
        return False, f"Unexpected frontmatter keys: {', '.join(sorted(unexpected))}"

    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    name = str(frontmatter.get('name', '')).strip()
    if name:
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' must be kebab-case (lowercase, digits, hyphens)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or have consecutive hyphens"
        if len(name) > 64:
            return False, f"Name too long ({len(name)} chars, max 64)"

    description = str(frontmatter.get('description', '')).strip()
    if description:
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets"
        if len(description) > 1024:
            return False, f"Description too long ({len(description)} chars, max 1024)"

    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
