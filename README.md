# Marketing Knowledge Base

An expert-level, agent-friendly marketing knowledge system built for **general use across companies, products, markets, and channels**.

This repository is not a collection of book summaries. It is an operational system for turning durable marketing principles into research, positioning, messaging, copy, campaigns, content, funnels, experiments, and critique.

The knowledge base synthesizes ideas from four source documents supplied during construction:

- *Breakthrough Advertising* — Eugene M. Schwartz
- *The Copywriter's Handbook* — Robert W. Bly
- *This Is Marketing* — Seth Godin
- *Hook Point* — Brendan Kane (the supplied file is a third-party Bookey summary, not the full original book)

The source books are **not included** in this repository. The files here use original explanation, synthesis, diagnostic models, checklists, and workflows rather than reproducing source text.

## What this repo is for

Use it when you need to:

- understand a market before writing anything;
- identify audience desire, awareness, sophistication, worldview, and status dynamics;
- choose a positioning strategy;
- turn product capabilities into benefits, mechanisms, proof, and offers;
- write or critique headlines, landing pages, ads, emails, sales pages, and scripts;
- create short-form content and hooks without collapsing into clickbait;
- diagnose weak conversion, weak attention, weak trust, or weak differentiation;
- design marketing experiments and interpret results;
- give an AI agent a disciplined marketing operating system rather than a bag of formulas.

## The core idea

**Diagnose first. Create second.**

Most bad marketing starts too late. Someone asks for a landing page, ad, email, or video and immediately starts writing. This repository forces the work upstream:

`market → audience → desire → awareness → sophistication → positioning → mechanism → proof → message → creative → distribution → measurement`

If any upstream layer is wrong, polishing downstream copy rarely fixes the problem.

## Repository map

```text
marketing-knowledge-base/
├── README.md
├── SKILL.md                     # master router / operating protocol
├── AGENTS.md                    # generic agent instructions
├── CLAUDE.md                    # Claude Code-friendly entry point
├── knowledge/
│   ├── 00-foundations/          # desire, awareness, worldview, trust, status
│   ├── 01-strategy/             # positioning, value, mechanism, pricing, funnels
│   ├── 02-copy/                 # headlines, proof, objections, copy structure
│   ├── 03-content/              # hooks, story, packaging, testing
│   └── 04-diagnostics/          # audit and diagnosis systems
├── skills/                      # task-specific SKILL.md files
├── prompts/                     # reusable prompt shells
├── templates/                   # briefs and experiment documents
├── rubrics/                     # scoring systems
├── examples/                    # cross-industry worked examples
└── sources/                     # bibliography, provenance, source quality
```

## Quick start for humans

1. Read `SKILL.md`.
2. Fill in `templates/universal-marketing-brief.md` or give an agent the equivalent information.
3. Pick the relevant task skill under `skills/`.
4. Let the skill route into the knowledge files it needs.
5. Score the result with the matching rubric before shipping.

## Quick start for AI agents

Point your agent at this repo and say:

> Use the repository's marketing skill system. Diagnose the market before creating. Read the master `SKILL.md`, then load only the task-specific skill and knowledge files needed for this request. State assumptions when information is missing. Do not invent evidence.

Examples:

> Use the marketing knowledge base to create three positioning territories for a new bookkeeping service for solo consultants. Do not write copy until you classify audience awareness and market sophistication.

> Audit this landing page using the landing-page skill. Identify whether the primary failure is attention, relevance, belief, value, friction, or offer strength. Then rewrite only the sections implicated by the diagnosis.

> Generate 20 short-form hooks for a consumer finance app. First determine the dominant desire, likely awareness stage, and hook families worth testing. Avoid generic curiosity bait.

## Agent compatibility

This repo intentionally uses plain Markdown instead of depending on one vendor's agent format. It can be used with:

- Claude Code
- OpenAI Codex / coding agents
- Cursor
- GitHub Copilot
- local agent frameworks
- custom RAG pipelines
- ChatGPT projects after uploading relevant files

`skills/<skill-name>/SKILL.md` files use a consistent, self-contained schema so they can be loaded selectively.

## Design principles

1. **Principles over slogans.** Framework names are only useful if they change a decision.
2. **Diagnosis over imitation.** Do not copy winning examples blindly; infer why they worked in that market and moment.
3. **Specificity over generic persuasion.** Concrete claims, mechanisms, proof, and audience language outperform vague superiority.
4. **Believability constrains promise.** A larger promise is worthless when credibility collapses.
5. **Attention is not persuasion.** A hook earns the next moment; it does not complete the sale.
6. **Positioning is selective.** Strong positioning deliberately excludes poor-fit buyers and alternatives.
7. **Trust compounds.** Short-term attention tactics that damage trust are usually negative expected value.
8. **Testing is part of strategy.** Hooks, promises, proof, offers, and distribution assumptions are hypotheses.
9. **Source-aware reasoning.** The supplied sources differ in completeness and reliability. See `sources/source-quality.md`.
10. **No invented proof.** Never fabricate testimonials, numbers, case studies, research, scarcity, or urgency.

## What this repo is not

It is not:

- a substitute for customer research;
- a prompt library that generates finished marketing from nothing;
- a list of headline formulas to mechanically fill in;
- a license to make unsupported claims;
- a repository of the source books.

## Recommended workflow

```text
1. Define objective
2. Define observable conversion behavior
3. Identify audience / smallest viable market
4. Map desire + problem + desired change
5. Classify awareness
6. Classify sophistication
7. Map alternatives and status/worldview
8. Pick positioning edge
9. Define mechanism / reason-to-believe
10. Assemble proof
11. Choose message architecture
12. Create hooks and copy
13. Remove friction
14. Design test
15. Learn and iterate
```

The repository's strongest value is not any single framework. It is the **ordering** of the frameworks so the wrong problem is not solved beautifully.
