# Green Tea Releases

Download the latest version of Green Tea from the [Releases](https://github.com/markoinla/green-tea-releases/releases) page.

## Changelog

### v0.2.5

- Persist bug reporter name and email for prefilling on subsequent submissions
- Fix image handling: prevent duplicate on paste, enable image input for all providers, handle MCP image content natively
- Pass connected MCP servers into agent system prompt
- Use fixed port (28106) for MCP OAuth callback so providers can use a stable redirect URL

### v0.2.4

- Add MCP (Model Context Protocol) server support with OAuth and settings UI
- Add bug report dialog with proxy-backed GitHub issue creation
- Add delayed informational tooltips to sidebar footer buttons
- Add auto-approve patches toggle and targeted find-and-replace patching (fixes multi-patch overwrite bug)
- Fix new notes not appearing in @ mention list until restart
- Fix marketplace install UX: per-button spinner and visible error messages
- Skip LLM adaptation for marketplace skill installs (prevents corruption)
- Add unified build workflow for macOS and Windows
- Fix scheduled tasks running on every app startup instead of on schedule

### v0.2.2

- Add sidebar hover-expand when collapsed
- Add Python detection at startup with toast warning
- File icons in document list
- UI polish and Prettier formatting pass

### v0.2.1

- Add task scheduler for recurring automated agent tasks (cron-based, headless, with catch-up logic)
- Add workspace memory system for cross-conversation persistence
- Add follow-up message queuing so users can type while the agent streams
- Update bundled default skills with new schemas, validators, and templates
- Make skill and directory seeding resilient to user deletion

### v0.1.9

- Add skill marketplace with browsing, installation, and auto-adaptation
- Add Cmd+F search and replace to the editor (with case toggle, navigation, replace-all)
- Switch web search to proxy endpoint
- Add subagent turn limits, timeouts, and proxy model routing
- Soften dark mode backgrounds; default to light theme

### v0.1.6

- Enable thinking/reasoning mode for OpenRouter models
- Add styled chip for slash commands in chat input
- Add OpenRouter provider with model selection (MiniMax, Gemini 3 Flash, Grok, GPT OSS)
- Sidebar tooltips and context menu icons

### v0.1.2

- Add auto-updater via GitHub Releases with user-prompted downloads and banner UI
- Add reasoning mode toggle with Kimi K2.5 compatibility
- Restore last opened workspace on launch
- Auto-trigger parallel explorer subagents for research queries
- Fix thinking indicator and activity group display bugs
- Smart auto-scroll in chat (only scrolls when near bottom)
