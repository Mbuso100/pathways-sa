# Pathways SA

Independent, free-to-use South African career exploration prototype, beginning with a KwaZulu-Natal pilot in English and isiZulu.

**Status: v0.9 engineering-readiness candidate — local prototype, not deployed or validated for public reliance.** No verified live vacancies, AI integration, database, accounts, or real-world outcome evidence. All isiZulu content needs review by fluent speakers.

## What works

A mobile-first React/TypeScript interface supports welcome → fictional three-stage water challenge → non-diagnostic reflection → exploratory career area → official information portals. A FastAPI backend validates stages and serves curated content. A separate eligibility evaluator uses synthetic examples only. No user profiles or answers are stored.

The portal links are **not verified open applications**, and career examples are not accredited career guidance. The project does not claim to assess intelligence or determine career fit.

## Architecture

| Location | Responsibility |
| --- | --- |
| `apps/web/src/Landing.tsx` | Approved homepage and presentation |
| `apps/web/src/api.ts`, `types.ts`, `copy.ts` | HTTP transport, types, bilingual copy |
| `apps/web/e2e/` | Chromium end-to-end English/isiZulu journeys |
| `apps/api/pathways/domain/` | Deterministic domain rules and curated references |
| `apps/api/pathways/api/` | FastAPI HTTP interface and response contracts |
| `apps/api/tests/` | Domain and API contract tests |
| `docs/decisions/` | Architecture and quality decisions |
| `.github/workflows/` | API, web, and browser checks on push/PR |

## Prerequisites

- Node.js 22 and npm
- Python 3.12+ (CI uses 3.12; local Windows verification used 3.14)
- Chromium installed through Playwright for browser tests

## Setup and run locally

From the repository root, set up the backend:

```powershell
cd apps/api
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -q
```

On macOS/Linux, use `.venv/bin/python` instead of `.venv\Scripts\python.exe`.

In a separate terminal, start the backend from `apps/api`:

```powershell
.\.venv\Scripts\python.exe -m uvicorn pathways.api.main:app --reload
```

From `apps/web`, install and run the frontend:

```powershell
npm ci
npm run dev
```

Open http://127.0.0.1:5173. API documentation: http://127.0.0.1:8000/docs.

## Quality gates

From `apps/api`:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

From `apps/web`:

```powershell
npm ci
npm run check
npx playwright install chromium
npm run test:e2e
npm audit
```

`npm run check` runs TypeScript, ESLint, Vitest, and a production build. Playwright starts both development servers when necessary and prefers `apps/api/.venv` automatically, falling back to `python` on PATH in CI. Browser tests run with one worker to reduce local resource pressure. Avoid running an extra backend server on port 8000 unless deliberately reusing it.

**Observed local verification on the supplied v0.8 sources:** 24 backend tests, 6 Vitest tests and 2 Chromium journeys passed; frontend check/build passed; npm audit reported zero vulnerabilities. **v0.9 configuration and CI have not yet been rerun or verified on GitHub.**

## Engineering review and limitations

See `docs/engineering-review.md` for a real test-runner conflict and the resolution. The decision records explain the deterministic, non-diagnostic design and modular boundaries.

Remaining work before public use: independent isiZulu review; content provenance and source review dates; accessibility and mobile usability testing; privacy/safeguarding review; real opportunity verification; deployment and security assessment. Do not describe the current prototype as an AI guidance engine.

The product name is provisional. This project is not affiliated with the linked information providers.
