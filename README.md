
# Pathways SA

**A bilingual career exploration platform for South African youth.**

Pathways SA is an independently developed, mobile-first web application that introduces young South Africans to career possibilities through an interactive decision-making experience.

The initial prototype focuses on KwaZulu-Natal and supports English and isiZulu. It combines a React and TypeScript frontend with a Python/FastAPI backend, emphasizing clear application architecture, deterministic business logic, API contracts, and automated testing.

> **Project status:** Version 0.9 — functional engineering prototype. The application has been tested locally and through GitHub Actions but has not yet been deployed for public use.

## Features

### Interactive career exploration

The application guides users through a fictional, three-stage water-management challenge. Each stage presents a practical situation and allows users to explore different approaches to solving it.

At the end of the challenge, users receive a reflection on their choices, an introduction to related career areas, and links to established South African information portals.

The experience is exploratory rather than diagnostic. It does not measure intelligence, determine career suitability, or establish eligibility for employment or study.

### Bilingual user experience

The interface supports:

- English
- isiZulu

Both language journeys are covered by automated browser tests. The isiZulu content requires independent language review before public deployment.

### Backend services

The Python/FastAPI backend provides:

- Scenario content and progression.
- Validation of challenge stages.
- Structured API responses.
- Curated career-related information.
- A separate, deterministic eligibility evaluator using synthetic test cases.

The current prototype does not require user registration or store individual challenge responses.

## Technology Stack

| Layer | Technologies |
| --- | --- |
| Frontend | React, TypeScript, Vite |
| Backend | Python, FastAPI, Pydantic |
| Backend testing | Pytest |
| Frontend testing | Vitest |
| End-to-end testing | Playwright, Chromium |
| Code quality | TypeScript, ESLint |
| Continuous integration | GitHub Actions |
| Version control | Git, GitHub |

## System Architecture

The application separates user-interface presentation, HTTP communication, and backend domain logic.

| Directory | Responsibility |
| --- | --- |
| `apps/web/src/` | Frontend components, API client, types, and localization |
| `apps/web/e2e/` | English and isiZulu browser tests |
| `apps/api/pathways/api/` | FastAPI endpoints and response contracts |
| `apps/api/pathways/domain/` | Domain rules, scenarios, and resources |
| `apps/api/tests/` | Backend unit and API contract tests |
| `docs/decisions/` | Architecture decision records |
| `docs/engineering-review.md` | Engineering review and debugging case study |
| `.github/workflows/` | Automated backend and frontend verification |

### Repository structure

```text
pathways-sa/
├── .github/
│   └── workflows/
├── apps/
│   ├── api/
│   │   ├── pathways/
│   │   │   ├── api/
│   │   │   ├── application/
│   │   │   └── domain/
│   │   ├── tests/
│   │   └── pyproject.toml
│   └── web/
│       ├── e2e/
│       ├── src/
│       ├── package.json
│       └── playwright.config.ts
├── docs/
│   ├── decisions/
│   └── engineering-review.md
└── README.md
```

## Installation and Local Development

### Prerequisites

- Node.js 22 and npm
- Python 3.12 or later
- Git
- Chromium, installed through Playwright for browser testing

### 1. Clone the repository

```bash
git clone https://github.com/Mbuso100/pathways-sa.git
cd pathways-sa
```

### 2. Configure the backend

From the project root:

```powershell
cd apps/api
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

Start the FastAPI development server:

```powershell
.\.venv\Scripts\python.exe -m uvicorn pathways.api.main:app --reload
```

The API will be available at:

- API: http://127.0.0.1:8000
- API documentation: http://127.0.0.1:8000/docs

On macOS and Linux, use `.venv/bin/python` instead of the Windows virtual-environment executable.

### 3. Configure the frontend

Open a second terminal and navigate to `apps/web`:

```powershell
cd apps/web
npm ci
npm run dev
```

Open the application at:

http://127.0.0.1:5173

## Testing and Quality Assurance

The project uses automated testing at the domain, API, frontend, and browser levels.

### Verified test results

| Verification | Result |
| --- | --- |
| Python backend tests | 24 passed |
| Frontend unit tests | 6 passed |
| End-to-end browser tests | 2 passed |
| TypeScript type checking | Passed |
| ESLint | Passed |
| Production build | Passed |
| npm dependency audit | 0 reported vulnerabilities |
| GitHub Actions — API tests | Passed |
| GitHub Actions — Web quality checks | Passed |

**Total: 32 automated tests passed locally.**

Both GitHub Actions workflows also completed successfully for the initial release commit, `63aa8e9`.

### Backend tests

From `apps/api`:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

### Frontend quality checks

From `apps/web`:

```powershell
npm run check
```

This command executes:

1. TypeScript type checking.
2. ESLint static analysis.
3. Vitest unit tests.
4. Production build verification.

### Browser tests

```powershell
npx playwright install chromium
npm run test:e2e
```

Playwright verifies the complete Water Challenge journey in both English and isiZulu. The test configuration uses one worker to reduce resource consumption during local execution.

## Engineering Decisions

Several design decisions were documented during development.

### Deterministic application logic

The backend uses explicit, testable rules for scenario progression and eligibility evaluation.

This approach provides predictable behavior and makes the application's decisions easier to verify.

### Separation of responsibilities

Frontend presentation, API communication, and domain logic are organized into separate modules.

This structure improves maintainability and allows components to be tested independently.

### Automated verification

Backend tests validate domain behavior and API contracts, while frontend unit tests cover client-side utilities.

Playwright adds browser-level verification of the complete user experience.

### AI-assisted software engineering

AI assistance was used during development, alongside manual execution, debugging, and verification.

One documented example involved a conflict between Vitest test discovery and Playwright test files. The issue was investigated and resolved by explicitly separating the test configurations.

The investigation and corrective changes are recorded in [Engineering Review](docs/engineering-review.md).

Further architectural decisions are documented in [Architecture Decision Records](docs/decisions).

## Current Development Status

Version 0.9 establishes a tested engineering foundation for the Pathways SA prototype.

The current implementation includes the interactive discovery experience, bilingual content, Python backend services, automated tests, and continuous integration.

Before a public pilot, additional work is required on independent isiZulu review, accessibility and mobile usability, content verification, privacy and security assessment, and deployment.

The prototype does not currently include a database, user accounts, verified live vacancies, or an integrated AI recommendation engine. Links to external information portals are provided for exploration and do not represent confirmed open applications.

## Development Roadmap

Pathways SA is being developed as a long-term, independent, free-to-use platform to help South Africans discover their interests, explore career and education pathways, build practical skills, and navigate trustworthy opportunities.

The project begins with a planned KwaZulu-Natal pilot supporting English and isiZulu, with the ambition to expand nationally.

### Where the project is today

Version 0.9 is a local engineering prototype featuring a bilingual, three-stage Water Challenge, non-diagnostic reflections, exploratory career information, a FastAPI backend, and automated testing.

The platform is not yet publicly deployed or validated. AI guidance, verified live opportunities, user accounts, and persistent progress tracking have not been implemented.

### Where we're going

Development is organized into nine phases:

1. **Product validation** — Research user needs, validate assumptions, and refine the experience.
2. **Technical foundation** — Strengthen architecture, testing, accessibility, security, and documentation.
3. **Discover My Direction** — Expand interactive activities, interests exploration, and reflections.
4. **Career exploration** — Build evidence-backed career profiles and education pathways.
5. **Opportunity navigation** — Introduce verified bursaries, learnerships, training, and employment resources.
6. **AI guidance and learning** — Explore grounded, explainable AI assistance alongside practical learning activities.
7. **My Journey** — Introduce optional progress tracking, goals, and personal learning journeys.
8. **KwaZulu-Natal pilot** — Conduct user testing, language review, and safeguarding assessments.
9. **National expansion** — Improve coverage, partnerships, and accessibility across South Africa.

These are planned development stages, not claims that the features have already been delivered.

### Engineering priorities

The immediate priorities are accessibility and keyboard navigation, bilingual experience quality, stronger career information structures, and the next version of the discovery journey.

Development progress, engineering decisions, and limitations will be documented openly as the project evolves.

**Full roadmap:** [Development Roadmap](docs/ROADMAP.md)

## Project Ownership

Pathways SA is an independently developed software engineering project.

**GitHub:** [Mbuso100](https://github.com/Mbuso100)

**Repository:** [Pathways SA](https://github.com/Mbuso100/pathways-sa)

The project is not affiliated with the external information providers linked within the application.
