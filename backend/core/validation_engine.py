from dataclasses import dataclass


@dataclass
class ValidationResult:

    approved: bool

    title: str

    message: str

    failed_rules: list

    passed_rules: list


def analyze_validation(
    checklist,
    decision
):

    passed = []
    failed = []

    for item in checklist.items:

        if item.completed:

            passed.append(item.name)

        else:

            failed.append(item.name)

    approved = decision.grade == "A++"

    if approved:

        message = (
            "Every critical rule required for your A++ model "
            "is currently satisfied."
        )

    else:

        message = (
            "One or more A++ rules are missing. "
            "Execution should wait."
        )

    return ValidationResult(

        approved=approved,

        title="Trade Validation",

        message=message,

        failed_rules=failed,

        passed_rules=passed

    )