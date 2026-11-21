
# Pathways SA — Development Roadmap

> Discover yourself. Explore possibilities. Build your future.

## 1. Vision

Pathways SA is an independent, free-to-use South African career exploration platform being developed to help people better understand their interests, explore possible futures, develop practical skills, and find trustworthy routes into education, training, employment, and entrepreneurship.

The project begins with a planned KwaZulu-Natal pilot in English and isiZulu, with a longer-term ambition to serve communities across South Africa.

Pathways SA is not intended to be another job board or a chatbot that simply recommends careers. Its goal is to create an accessible, interactive journey that connects self-exploration with practical information and meaningful next steps.

The platform will not claim to measure intelligence, diagnose personal characteristics, or determine someone's ideal career. Users should remain in control of their decisions.

## 2. Current Project Status

**Version:** v0.9 engineering-readiness candidate

**Stage:** Local prototype — not publicly deployed or validated for public reliance.

### Implemented

- Mobile-first React and TypeScript interface.
- English and isiZulu interface content.
- Fictional three-stage Water Challenge.
- Non-diagnostic reflection and exploratory career areas.
- Links to official information portals.
- Python/FastAPI backend and deterministic domain rules.
- Synthetic eligibility evaluation examples.
- Automated backend, frontend, and browser tests.
- GitHub Actions continuous integration.
- Engineering documentation and architecture decisions.

### Not Yet Implemented

- Integrated AI guidance.
- Persistent database and user accounts.
- Saved personal journeys or progress.
- Verified live opportunity listings.
- Comprehensive career and education profiles.
- Public deployment.
- Independent isiZulu language validation.
- Real-world pilot testing and outcome evidence.

The current prototype is an engineering foundation, not the completed Pathways SA product.

## 3. Planned Platform Modules

### Module 1 — Discover Me

Help users explore interests, preferences, strengths, and possible directions through accessible activities and reflections.

Planned capabilities:

- Interest exploration.
- Scenario-based discovery activities.
- Reflective questions.
- Explainable exploratory suggestions.
- Optional discovery history.

The current Water Challenge provides an early prototype of this approach.

### Module 2 — Play & Discover

Use interactive experiences to make career and skill exploration engaging.

Proposed experiences include:

- Pattern Detective.
- Community Challenge.
- Run a Small Shop.
- What Would You Do?
- Career Explorer.

Activities should encourage curiosity, reasoning, creativity, and reflection without assigning intelligence scores or fixed career labels.

### Module 3 — Learn & Develop

Provide practical opportunities to build knowledge and skills.

Planned capabilities:

- Short learning activities.
- Practical exercises.
- Knowledge checks.
- Skill development pathways.
- Optional learning progress.

Learning content should be understandable, useful, and accessible to users with different educational backgrounds.

### Module 4 — Explore My Future

Help users investigate career areas and the different routes available to them.

Planned capabilities:

- Career profiles supported by credible sources.
- Qualifications and education requirements.
- University, TVET, learnership, and alternative pathways.
- Related skills and practical expectations.
- Career comparisons.
- Guidance for users considering a change in direction.

Career information must distinguish verified facts from general exploratory suggestions.

### Module 5 — Opportunity & Application Navigator

Help users navigate trustworthy opportunities and understand application requirements.

Potential categories include:

- Education and training.
- Bursaries and financial assistance.
- Learnerships and internships.
- Employment.
- Remote work.
- Entrepreneurship and business support.

Planned safeguards:

- Original source links.
- Source and verification dates.
- Clear eligibility information.
- Application preparation checklists.
- Expiry and availability checks where possible.
- No invented vacancies, deadlines, or guarantees.

This module will require a reliable source-review process before being offered for public reliance.

### Module 6 — My Journey

Allow users to optionally organize their exploration and progress.

Planned capabilities:

- Saved interests and activities.
- Learning progress.
- Goals and next steps.
- Opportunity bookmarks.
- Application preparation tracking.
- Ability to revisit and reconsider previous choices.

The platform should remain useful without requiring an account for basic exploration.

### Module 7 — Wellbeing-Aware Experience

Create an encouraging and respectful experience for users facing uncertainty about education, work, or their future.

Design principles:

- Avoid judgmental language.
- Respect different circumstances and starting points.
- Do not diagnose mental health conditions.
- Do not pressure users into particular careers.
- Provide clear boundaries around automated guidance.
- Support user autonomy and informed decisions.

### Module 8 — Impact Analytics & Administration

Develop privacy-conscious tools for maintaining quality and understanding whether the platform is useful.

Planned capabilities:

- Content and source review workflows.
- Opportunity verification records.
- Language and content quality review.
- Anonymous or appropriately consented usage insights.
- Accessibility and usability feedback.
- Pilot evaluation and product improvement.

Analytics should prioritize meaningful outcomes and user privacy rather than collecting unnecessary personal information.

## 4. Development Phases

Development is organized into nine phases. These phases describe intended work and may evolve as research, testing, and resources change.

### Phase 0 — Product Discovery and Validation

**Goal:** Confirm that the platform addresses real user needs.

Planned work:

- Define priority user groups.
- Research barriers to career exploration.
- Validate assumptions about access, language, and digital literacy.
- Map initial user journeys.
- Identify trustworthy information sources.
- Establish practical measures of usefulness.

**Exit evidence:** Documented user needs, validated assumptions, and an agreed initial product scope.

**Status:** Planning and early product definition.

### Phase 1 — Technical Foundation

**Goal:** Establish a maintainable, testable, and secure foundation.

Work includes:

- Modular frontend and backend architecture.
- API contracts and deterministic business rules.
- Automated tests and CI.
- Development documentation.
- Accessibility improvements.
- Security and dependency reviews.
- Error handling and operational readiness.

**Exit evidence:** Reliable engineering checks, documented decisions, and a foundation suitable for further development.

**Status:** Partially implemented in v0.9; additional work remains.

### Phase 2 — Discover My Direction

**Goal:** Deliver a useful first discovery experience.

Planned work:

- Improve onboarding and language selection.
- Let users choose why they are visiting.
- Offer different exploration modes.
- Expand scenario-based activities.
- Improve reflection and explanations.
- Strengthen keyboard and mobile accessibility.
- Review isiZulu content with fluent speakers.
- Test comprehension and usability.

**Exit evidence:** A complete, accessible discovery journey evaluated with representative users.

**Status:** Partially implemented through the Water Challenge.

### Phase 3 — Career Exploration

**Goal:** Connect discovery activities to trustworthy career information.

Planned work:

- Define a structured career profile model.
- Build initial South African career profiles.
- Research education and qualification routes.
- Add alternative pathways.
- Connect discovery reflections to career exploration.
- Display information sources and review dates.

**Exit evidence:** Users can explore documented career pathways without receiving unsupported career-fit claims.

**Status:** Planned.

### Phase 4 — Opportunity Navigation

**Goal:** Help users find and prepare for relevant, verified opportunities.

Planned work:

- Define opportunity data structures.
- Establish source verification procedures.
- Add eligibility and requirement explanations.
- Build application checklists.
- Handle expired or unverified information.
- Provide direct links to original providers.

**Exit evidence:** An opportunity workflow with traceable sources, verification dates, and clear limitations.

**Status:** Planned.

### Phase 5 — AI Guidance and Learning

**Goal:** Introduce carefully bounded AI assistance and useful learning experiences.

Planned work:

- Develop practical learning content.
- Evaluate appropriate AI use cases.
- Ground AI responses in approved information.
- Keep eligibility decisions deterministic where appropriate.
- Test unsupported claims and prompt injection.
- Make automated guidance explainable.
- Provide clear uncertainty and safety boundaries.
- Test English and isiZulu quality.

AI should support exploration, not replace user judgment or invent opportunities.

**Exit evidence:** Evaluated guidance and learning experiences with documented accuracy, safety, and limitations.

**Status:** Planned. No AI engine is currently integrated.

### Phase 6 — Personal Journey and Analytics

**Goal:** Help users maintain progress while respecting privacy.

Planned work:

- Optional accounts or local progress mechanisms.
- Saved goals and interests.
- Learning and application progress.
- Privacy controls and data minimization.
- Consent and deletion processes where applicable.
- Administrative quality monitoring.

**Exit evidence:** Tested progress features and documented privacy safeguards.

**Status:** Planned.

### Phase 7 — KwaZulu-Natal Pilot

**Goal:** Evaluate the platform with real users before broader release.

Planned work:

- Recruit appropriate pilot participants.
- Conduct independent isiZulu review.
- Test mobile usability and accessibility.
- Review safeguarding and privacy practices.
- Validate information quality.
- Collect feedback and measure practical usefulness.
- Address findings before expansion.

**Exit evidence:** Documented pilot findings, corrective actions, and a responsible release decision.

**Status:** Planned. No pilot outcome claims are made.

### Phase 8 — National Expansion

**Goal:** Explore sustainable expansion beyond the initial pilot.

Potential work:

- Broader provincial information coverage.
- Additional language support.
- More career and learning pathways.
- Partnerships with credible information providers.
- Improved performance and accessibility.
- Sustainable maintenance and governance.

Expansion will depend on demonstrated usefulness, reliable information, and available resources.

**Status:** Long-term ambition.

## 5. Immediate Engineering Priorities

The next development work should strengthen the existing prototype before adding large new features.

### Priority 1 — Accessibility and Keyboard Navigation

Review the Water Challenge for:

- Semantic HTML and accessible controls.
- Logical keyboard navigation.
- Visible focus indicators.
- Clear errors and status messages.
- Assistive technology compatibility.
- English and isiZulu usability.
- Automated tests for important interactions.

Preserve the approved visual design unless changes are necessary to resolve accessibility problems.

### Priority 2 — Bilingual Experience Quality

- Review all current English and isiZulu copy.
- Check consistency across screens and API responses.
- Establish a fluent-speaker review process.
- Test long text, small screens, and error messages.

### Priority 3 — Discovery Journey Improvements

- Clarify onboarding and user intent.
- Improve activity instructions.
- Strengthen reflections and next steps.
- Explore multiple modes of engagement.
- Test whether users understand the purpose of the activities.

### Priority 4 — Career Information Foundation

- Design a career profile schema.
- Define source and review metadata.
- Establish a content review process.
- Connect one discovery journey to a small set of sourced career profiles.

### Priority 5 — Opportunity Verification Foundation

- Define opportunity categories and eligibility fields.
- Create a source-verification workflow.
- Establish expiry and review rules.
- Keep synthetic examples separate from real opportunities.

## 6. Engineering Principles

Pathways SA development will prioritize:

1. **Accuracy over impressive claims.** Implemented features must be clearly distinguished from planned features.
2. **User agency.** The platform supports decisions without assigning fixed personal labels.
3. **Accessibility.** Mobile-first design, keyboard support, and understandable content matter from the beginning.
4. **Language quality.** English and isiZulu experiences require careful review.
5. **Source transparency.** Career and opportunity information must be traceable.
6. **Privacy by design.** Collect only data needed to deliver a useful experience.
7. **Responsible AI.** AI must be evaluated, grounded, and appropriately limited before public use.
8. **Maintainable engineering.** Prefer clear module boundaries, tests, documentation, and incremental delivery.
9. **Evidence-based progress.** Completion should be demonstrated through working functionality, reviews, and testing.
10. **Long-term sustainability.** Build features that can be maintained responsibly.

## 7. Architecture Direction

The current technology foundation includes:

- React and TypeScript for the frontend.
- Python and FastAPI for the backend.
- Deterministic domain logic.
- Automated testing with pytest, Vitest, and Playwright.
- GitHub Actions for continuous integration.

Potential future additions include:

- PostgreSQL and database migrations.
- Containerized deployment.
- Secure optional authentication.
- Structured content and opportunity management.
- Source-grounded AI services.
- Privacy-conscious analytics and administration.

Future technologies will be selected based on actual requirements, not added simply to increase complexity.

## 8. Responsible Release Requirements

Before the platform can be presented as ready for public reliance, relevant release requirements will include:

- Independent language review.
- Accessibility and usability evaluation.
- Source verification and content maintenance.
- Security and deployment assessment.
- Privacy and safeguarding review, including applicable POPIA requirements.
- Clear limitations and user-facing explanations.
- Pilot feedback and documented corrective actions.

Passing automated tests alone does not establish that a career guidance product is ready for public use.

## 9. Progress and Contributions

Development progress will be reflected through GitHub issues, pull requests, architecture decisions, tests, and documented milestones.

The roadmap is a living plan rather than a promise of fixed delivery dates. Features and priorities may change as the project is validated.

Pathways SA is intended to remain independent, with free core access as a product principle. Any future open-source licensing or contribution policy will be documented explicitly rather than assumed.

---

**Current milestone:** Strengthen v0.9 engineering quality and complete the first meaningful discovery journey.

**Long-term direction:** A trustworthy, accessible South African platform connecting self-discovery, career exploration, learning, and practical opportunities.
