# Workflow Patterns

## Sequential Workflows

Break complex tasks into clear steps with an overview at the top of SKILL.md:

```markdown
Filling a PDF form involves these steps:

1. Analyze the form (run analyze_form.py)
2. Create field mapping (edit fields.json)
3. Validate mapping (run validate_fields.py)
4. Fill the form (run fill_form.py)
5. Verify output (run verify_output.py)
```

## Conditional Workflows

Guide through decision points with branching logic:

```markdown
1. Determine the modification type:
   **Creating new content?** -> Follow "Creation workflow" below
   **Editing existing content?** -> Follow "Editing workflow" below

2. Creation workflow: [steps]
3. Editing workflow: [steps]
```
