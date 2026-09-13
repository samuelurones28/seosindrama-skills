# seosindrama-skills

SEO and GEO skills for AI agents (Claude Code, Codex, Cursor, and any tool
that supports [Agent Skills](https://agentskills.io)), calibrated on 731 real
audits of Spanish small-business websites.

[Versión en español](README.md)

## What this is

Three skills that teach an agent to do three specific things we do every day
at [seosindrama.com](https://www.seosindrama.com). The skill bodies are in
Spanish; descriptions carry English keywords so they trigger in both
languages, and the output language follows the user's.

| Skill | What it does | Status |
|---|---|---|
| [`traducir-a-cliente`](skills/traducir-a-cliente/) | Turns PageSpeed, Lighthouse, Screaming Frog or agency findings into explanations a non-technical client understands: business-language title, impact, everyday analogy, three steps, and a separate note for the developer | Published |
| [`auditoria-geo`](skills/auditoria-geo/) | Audits whether a site is ready to be read and cited by ChatGPT, Perplexity, Gemini or Claude: AI crawler access, JSON-LD, citable content, entity consistency. Ships a dependency-free Python script | Provisional |
| [`schema-negocio-local`](skills/schema-negocio-local/) | Generates the right `LocalBusiness` JSON-LD for a Spanish local business and explains where to paste it per CMS | Published |

## Install

Copy the skill folder wherever your agent looks for skills. With Claude Code:

```bash
git clone https://github.com/samuelurones28/seosindrama-skills.git
cp -r seosindrama-skills/skills/traducir-a-cliente ~/.claude/skills/
```

All install paths (Claude Code, Codex, Cursor, full clone) are in
[`docs/instalacion.md`](docs/instalacion.md) (Spanish).

## Example

With `traducir-a-cliente` installed, in Claude Code:

> Explain this PageSpeed warning to my client: "Reduce unused JavaScript —
> Potential savings of 3,281 KiB, est. 6,020 ms. Three chunks from
> https://www.youtube.com/... (YouTube player)". Services website, non-technical
> client.

The agent returns a finding with a plain-language title carrying the actual
figure ("3,281 KB of downloaded code goes unused"), a two-sentence business
impact that flags the 6,020 ms as a Lighthouse estimate rather than a measured
loss, an everyday analogy (hauling a huge box to deliver a few documents),
three imperative steps (confirm → fix → re-measure against the same
figures), and a copy-paste note for the developer. The Spanish original is
in [README.md](README.md); it is a real finding from a seosindrama.com audit,
domain anonymised.

## Where the data comes from

The rules, thresholds, analogies and priorities come from 731 audits across
573 Spanish SMB domains (March to September 2026), not from theory. What
fails, how often, and the sample's limitations are in
[`docs/datos.md`](docs/datos.md) (Spanish).

In short: the typical SMB site passes (mean score 78.6) but carries two or
three concrete problems. 75% have a load-speed finding, 44% unused
JavaScript, 34% accessibility.

## Contributing

- **Bugs and bad outputs:** open an issue with the input you gave the agent
  and what it returned.
- **Glossary terms, business types for the schema skill, crawler
  user-agents:** pull request on the relevant `references/` file, with a
  source.
- **New skills:** open an issue first to agree on scope. Every skill needs
  a "What it does NOT do" section.

Figures in `docs/datos.md` are recomputed from the seosindrama.com database;
PRs that edit them by hand are not accepted.

## License

MIT. Use, copy and adapt the skills in your own or client projects. Examples
are anonymised; if you spot anything identifying a real business, open an
issue and it will be removed.
