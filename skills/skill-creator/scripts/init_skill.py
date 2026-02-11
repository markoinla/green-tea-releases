#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path ~/Documents/Green\ Tea/skills
    init_skill.py data-analyzer --path /path/to/skills
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: What this skill does and WHEN to use it. Include specific triggers, file types, or tasks.]
---

# {skill_title}

[TODO: 1-2 sentences explaining what this skill enables]

[TODO: Add workflow steps, examples, and instructions. See the skill-creator skill for guidance on structure.]
"""


def title_case_skill_name(skill_name):
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


def init_skill(skill_name, path):
    skill_dir = Path(path).resolve() / skill_name

    if skill_dir.exists():
        print(f"Error: Skill directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
    except Exception as e:
        print(f"Error creating directory: {e}")
        return None

    # Create SKILL.md
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,
        skill_title=skill_title
    )
    (skill_dir / 'SKILL.md').write_text(skill_content)

    # Create optional resource directories
    (skill_dir / 'scripts').mkdir(exist_ok=True)
    (skill_dir / 'references').mkdir(exist_ok=True)
    (skill_dir / 'assets').mkdir(exist_ok=True)

    print(f"Skill '{skill_name}' initialized at {skill_dir}")
    print("Next: edit SKILL.md, add resources, delete unused directories")
    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        print("\nSkill name: kebab-case, lowercase letters/digits/hyphens, max 64 chars")
        print("\nExamples:")
        print("  init_skill.py my-skill --path ~/Documents/Green\\ Tea/skills")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    result = init_skill(skill_name, path)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
