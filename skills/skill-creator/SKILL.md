---
name: skill-creator
description: Guide for creating and updating skills that extend the agent's capabilities. Use when asked to create a new skill, update an existing skill, or learn a new workflow that should be reusable across sessions. Skills are stored in the skills/ directory within the working base directory and are automatically loaded on session start.
---

# Skill Creator

Create effective skills that extend agent capabilities with specialized knowledge, workflows, and tool integrations.

## About Skills

Skills are modular packages that provide specialized knowledge, workflows, and tools. They transform a general-purpose agent into a specialized one with procedural knowledge. Skills are stored in the `skills/` directory alongside `agent-workspace/` and are automatically loaded at session start.

```
~/Documents/Green Tea/
  skills/              <-- skills live here
    my-skill/
      SKILL.md
      scripts/
      references/
      assets/
  agent-workspace/
    <workspace>/
```

## Core Principles

### Concise is Key

The context window is shared with everything else. Only add context the agent doesn't already have. Prefer concise examples over verbose explanations.

### Degrees of Freedom

- **High freedom** (text instructions): Multiple valid approaches, context-dependent decisions
- **Medium freedom** (pseudocode/parameterized scripts): Preferred pattern exists, some variation acceptable
- **Low freedom** (specific scripts): Fragile operations, consistency critical, specific sequence required

### Skill Structure

```
skill-name/
  SKILL.md           (required: YAML frontmatter + markdown instructions)
  scripts/           (optional: executable code for deterministic tasks)
  references/        (optional: documentation loaded on-demand)
  assets/            (optional: templates, images, fonts used in output)
```

#### SKILL.md Frontmatter

```yaml
---
name: kebab-case-name
description: What it does and WHEN to use it. Be specific about triggers.
---
```

Only `name` and `description` are required. The description is the primary trigger mechanism — it must clearly state when the skill applies.

#### Progressive Disclosure

1. **Metadata** (name + description) — always in context (~100 words)
2. **SKILL.md body** — loaded when skill triggers (<500 lines)
3. **Bundled resources** — loaded as needed by agent

Keep SKILL.md under 500 lines. Split into reference files when approaching this limit, and clearly describe when to read each file.

## Skill Creation Process

1. Understand the skill with concrete examples
2. Plan reusable contents (scripts, references, assets)
3. Initialize the skill (run init_skill.py)
4. Edit the skill (implement resources and write SKILL.md)
5. Validate the skill (run quick_validate.py)
6. Iterate based on real usage

### Step 1: Understand with Examples

Ask clarifying questions to understand concrete usage:

- What tasks should trigger this skill?
- What are example user requests?
- What does good output look like?

### Step 2: Plan Reusable Contents

For each example, identify what would help when executing repeatedly:

- **Scripts**: Code rewritten the same way each time (e.g., `scripts/rotate_pdf.py`)
- **References**: Documentation needed during work (e.g., `references/schema.md`)
- **Assets**: Files used in output (e.g., `assets/template.pptx`)

### Step 3: Initialize

Run the init script to create the skill directory:

```bash
python3 scripts/init_skill.py <skill-name> --path <skills-directory>
```

This creates the directory with a template SKILL.md and example resource files.

### Step 4: Edit the Skill

Implement the planned resources and write SKILL.md. Key guidelines:

- **Frontmatter description**: Include all "when to use" triggers here (not in body)
- **Body**: Procedural instructions, workflows, examples
- **References**: Detailed docs, schemas, API references — linked from SKILL.md
- **Scripts**: Test by running them to verify they work
- Delete any example files not needed

For design patterns, see:

- [references/workflows.md](references/workflows.md) — sequential and conditional workflow patterns
- [references/output-patterns.md](references/output-patterns.md) — template and example output patterns

### Step 5: Validate

```bash
python3 scripts/quick_validate.py <path/to/skill-folder>
```

Fix any validation errors before considering the skill complete.

### Step 6: Iterate

After using the skill on real tasks, update SKILL.md or resources based on what worked and what didn't. The skill will be picked up on the next session.
