import pytest
from pathways.domain.eligibility import Applicant, OpportunityRequirements, EligibilityStatus, assess


@pytest.mark.parametrize("applicant,requirements,expected", [
    (Applicant(4, "KZN"), OpportunityRequirements(4, frozenset({"KZN"}), True), EligibilityStatus.ELIGIBLE),
    (Applicant(3, "KZN"), OpportunityRequirements(4, frozenset({"KZN"}), True), EligibilityStatus.INELIGIBLE),
    (Applicant(4, "WC"), OpportunityRequirements(4, frozenset({"KZN"}), True), EligibilityStatus.INELIGIBLE),
    (Applicant(None, "KZN"), OpportunityRequirements(4, frozenset({"KZN"}), True), EligibilityStatus.NEEDS_VERIFICATION),
    (Applicant(4, None), OpportunityRequirements(4, frozenset({"KZN"}), True), EligibilityStatus.NEEDS_VERIFICATION),
    (Applicant(4, "KZN"), OpportunityRequirements(4, frozenset({"KZN"}), False), EligibilityStatus.NEEDS_VERIFICATION),
])
def test_assessment(applicant, requirements, expected):
    assert assess(applicant, requirements).status == expected


def test_known_failure_takes_precedence_over_unknown():
    result = assess(Applicant(2, None), OpportunityRequirements(4, frozenset({"KZN"}), True))
    assert result.status == EligibilityStatus.INELIGIBLE
    assert "PROVINCE_UNKNOWN" in result.reason_codes
