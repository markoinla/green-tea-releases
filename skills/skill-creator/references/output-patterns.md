# Output Patterns

## Template Pattern

Provide templates for consistent output format.

**Strict (API responses, data formats):**

```markdown
## Report structure

ALWAYS use this exact template:

# [Analysis Title]

## Executive summary

[One-paragraph overview]

## Key findings

- Finding 1 with data
- Finding 2 with data

## Recommendations

1. Actionable recommendation
2. Actionable recommendation
```

**Flexible (when adaptation is useful):**

```markdown
## Report structure

Sensible default format — adjust as needed:

# [Analysis Title]

## Executive summary

[Overview]

## Key findings

[Adapt sections based on discoveries]

## Recommendations

[Tailor to context]
```

## Examples Pattern

For quality-dependent output, provide input/output pairs:

```markdown
## Commit message format

**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication

**Example 2:**
Input: Fixed date display bug in reports
Output: fix(reports): correct date formatting in timezone conversion
```

Examples convey style and detail more clearly than descriptions.
