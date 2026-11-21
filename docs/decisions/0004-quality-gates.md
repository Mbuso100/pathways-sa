# ADR 0004: Incremental quality gates for the first journey

**Status:** Accepted for v0.7, pending local frontend verification.

## Context

The first bilingual user journey and FastAPI backend are working. The frontend build alone does not prove API failure handling, bilingual content completeness or adherence to static quality checks. The project is a prototype, not a deployed public service.

## Decision

- Retain the modular React/Vite frontend and framework-independent Python domain logic; do not introduce microservices.
- Use TypeScript strict checking, ESLint with TypeScript and React Hooks rules, Vitest for isolated frontend unit tests, and pytest for backend contract and domain tests.
- Make GitHub Actions run the same frontend `npm run check` command developers run locally.
- Test API-client success, HTTP failure and network failure, and translation key parity without coupling tests to visual styling.
- Do not claim full browser end-to-end or accessibility coverage: those are separate tasks.

## Consequences and remaining work

- The frontend toolchain must be installed and verified on a machine with npm registry access.
- Generate and commit `apps/web/package-lock.json` after `npm install`; then change CI to `npm ci` for reproducible installs. Do not fabricate a lockfile.
- Add browser-level interaction and keyboard/accessibility tests, mobile checks, dependency scanning and Python lint/type checks before claiming comprehensive quality gates.
- Review the warning from FastAPI/Starlette test dependencies when upstream compatibility stabilizes.
