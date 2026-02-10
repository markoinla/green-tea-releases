# Meeting Notes

Structure, summarize, and extract action items from meeting notes.

## When to use

Use this skill when the user wants to:
- Clean up raw meeting notes into a structured format
- Extract action items and decisions from meeting transcripts
- Summarize key discussion points from a meeting
- Create follow-up task lists from meeting content
- Organize notes from multiple meetings on a topic

## Instructions

When processing meeting notes:

1. **Identify key sections** — Parse the raw notes to find:
   - Attendees and date
   - Agenda items discussed
   - Decisions made
   - Action items assigned
   - Open questions or follow-ups

2. **Structure the output** — Rewrite the notes with clear sections:
   - **Meeting Info** — Date, attendees, purpose
   - **Summary** — 2-3 sentence overview of what was discussed
   - **Discussion Points** — Key topics with brief notes on each
   - **Decisions** — Clear list of what was decided
   - **Action Items** — Who, what, and when for each task
   - **Next Steps** — Follow-ups and next meeting topics

3. **Extract action items** — Pull out every commitment or task mentioned. Format each with:
   - Owner (who is responsible)
   - Task description
   - Due date (if mentioned)

4. **Preserve context** — Keep enough detail that someone who missed the meeting can understand the decisions and reasoning.

5. **Write to notes** — Save the structured notes using the notes tools.

## Output format

Use this template:

```
# Meeting: [Topic]
**Date:** [Date]
**Attendees:** [Names]

## Summary
[2-3 sentence overview]

## Discussion Points
- [Topic 1]: [Key points]
- [Topic 2]: [Key points]

## Decisions
- [Decision 1]
- [Decision 2]

## Action Items
- [ ] [Owner]: [Task] (due: [date])
- [ ] [Owner]: [Task] (due: [date])

## Next Steps
- [Follow-up items]
```
