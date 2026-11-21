"""Deterministic opportunity eligibility rules; no AI-generated decisions."""
from dataclasses import dataclass
from enum import Enum


class EligibilityStatus(str, Enum):
    ELIGIBLE = "eligible"
    INELIGIBLE = "ineligible"
    NEEDS_VERIFICATION = "needs_verification"


@dataclass(frozen=True)
class Applicant:
    highest_nqf_level: int | None
    province: str | None


@dataclass(frozen=True)
class OpportunityRequirements:
    minimum_nqf_level: int | None
    allowed_provinces: frozenset[str] | None
    source_verified: bool


@dataclass(frozen=True)
class EligibilityResult:
    status: EligibilityStatus
    reason_codes: tuple[str, ...]


def assess(applicant: Applicant, requirements: OpportunityRequirements) -> EligibilityResult:
    """Fail closed on uncertain source data; never infer missing applicant details."""
    if not requirements.source_verified:
        return EligibilityResult(EligibilityStatus.NEEDS_VERIFICATION, ("SOURCE_UNVERIFIED",))

    unmet: list[str] = []
    unknown: list[str] = []
    if requirements.minimum_nqf_level is not None:
        if applicant.highest_nqf_level is None:
            unknown.append("NQF_LEVEL_UNKNOWN")
        elif applicant.highest_nqf_level < requirements.minimum_nqf_level:
            unmet.append("NQF_LEVEL_BELOW_MINIMUM")

    if requirements.allowed_provinces is not None:
        if not applicant.province:
            unknown.append("PROVINCE_UNKNOWN")
        elif applicant.province.upper() not in requirements.allowed_provinces:
            unmet.append("PROVINCE_NOT_ALLOWED")

    if unmet:
        return EligibilityResult(EligibilityStatus.INELIGIBLE, tuple(unmet + unknown))
    if unknown:
        return EligibilityResult(EligibilityStatus.NEEDS_VERIFICATION, tuple(unknown))
    return EligibilityResult(EligibilityStatus.ELIGIBLE, ())
