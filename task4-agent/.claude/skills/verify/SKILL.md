---
name: verify
description: Verify a program implementation against the following quality gates: test integrity, health
  check completeness, deployment readiness, and maintainability. Updates status to VERIFIED.
---

# Feature Verification — Four Quality Gates

You are the Quality Verifier. Your job is to verify the command-line-quiz implementation against four gates. No exceptions, no partial passes.

## Trigger

The user invokes `/verify` within a project directory.

## Step 1: Read the Spec

Read `README.md`. Extract all requirements and acceptance criteria — these are the contract. Use an adversarial interview to ask the user clarifying questions about the project requirements, acceptance criteria, and specifications using the feature architect persona. If any acceptance criterion is vague or untestable, ask the user to clarify or update the spec before proceeding.

### Adversarial Interview

Ask clarifying questions to resolve ambiguity. Ask **one question at a time**, wait for the answer, then ask the next. Continue for 2-5 questions until you have enough clarity.

Draw questions from these techniques:

**Five Whys** — Dig into the real need:
- "Why does the user need this?"
- "Why can't the existing system handle this?"
- "Why this approach over alternatives?"

**Edge Case Probing** — Stress the boundaries:
- "What happens when the input is empty / invalid / huge?"
- "What does the error experience look like?"
- "What if the user does the unexpected thing?"

**Assumption Challenging** — Push back:
- "Why not just reuse [existing feature]?"
- "What if we scoped this to half the functionality?"
- "Is this a must-have or a nice-to-have?"

**Required questions** (must always ask):
- "What does the definition of done look like?"
- "How will this be verified?"

**Interview Rules:**
- Only ask 1 question at a time. Wait for the answer before asking the next.
- Do not accept vague answers. Follow up with "Can you be more specific about...?"
- After each answer, briefly summarize what you have learned.
- When ambiguity is resolved, state: "I have enough to write the spec. Proceeding."


## Step 2: Run the Four Gates

Run each gate in order. Report pass/fail with specifics. If any gate fails, fix the issue and re-verify that gate before moving on.

---

### Gate 1: Test Integrity

Run the test suite with coverage:

```
pytest --cov -v
```

**Pass criteria:**
- All tests pass. Zero failures, zero errors.
- Code coverage is at least 70%. No critical functions left uncovered.
- Edge cases from acceptance criteria are covered (empty inputs, missing files, case-insensitive matching).
- Test names describe behavior clearly (e.g., test_run_quiz_correct_answer_increments_score).
- Each public function (Question.__init__, to_dict, from_dict, run_quiz, save_quiz, load_quiz, create_quiz, main) has at least one test.

**If this gate fails:**
- Identify which tests failed and examine the error output.
- Determine if the bug is in the test or the source code.
- Fix the code if the test correctly specifies expected behavior. Fix the test only if the test itself is wrong.
- Identify uncovered lines from the coverage report Missing column.
- Write additional tests targeting uncovered lines and edge cases.
- Re-run pytest --cov -v until all tests pass and coverage meets the 70% threshold.

---

### Gate 2: Health Check Completeness

Review the implementation code for defensive programming:

**Pass criteria:**
- Error handling exists for file I/O operations (load_quiz handles missing files gracefully).
- No silent failures: no bare `except:` blocks, no swallowed exceptions.
- Invalid inputs produce clear, user-facing error messages (not raw tracebacks).
- The application does not crash on empty input, unexpected menu choices, or missing quiz files.
- Functions validate their inputs where appropriate (e.g., quiz name is not empty).

**If this gate fails:**
- Add input validation for any function that accepts user input without checking it.
- Add try/except blocks with descriptive error messages around file I/O operations.
- Replace any bare `except:` with specific exception types.
- Add tests for the new error-handling paths.
- Re-run Gate 1 to confirm all tests still pass after changes.

---

### Gate 3: Deployment Readiness

Run a clean install and execution check:

```
python quiz.py
```

**Pass criteria:**
- The application starts without errors or import failures.
- No hardcoded file paths, secrets, or environment-specific values in the source code.
- All dependencies are listed in requirements.txt.
- The main menu displays correctly and responds to all valid choices (1, 2, 3).
- Invalid menu choices display a helpful error message and re-prompt.
- README.md contains accurate instructions for setup and execution.
- Each acceptance criterion from the spec can be traced to at least one passing test.

**If this gate fails:**
- Fix any import errors or missing dependencies.
- Externalize any hardcoded paths or configuration values.
- Update requirements.txt with any missing packages.
- If any acceptance criterion lacks a corresponding test, write one and re-run Gate 1.
- Update README.md with corrected setup and execution instructions.

---

### Gate 4: Maintainability in Context

Run the linter and review code quality:

```
flake8
```

**Pass criteria:**
- flake8 reports zero violations (or only minor whitespace warnings on existing code).
- Code follows PEP 8 style conventions (consistent indentation, naming, line length).
- Variable and function names are self-documenting and describe their purpose.
- Functions have docstrings or inline comments explaining their behavior.
- No unnecessary or unjustified dependencies beyond the standard library and pytest.
- Test code is clean: no duplicate test logic, fixtures used to reduce repetition.

**If this gate fails:**
- Fix all flake8 violations (auto-fix with autopep8 where possible).
- Add docstrings to any public function that lacks one.
- Refactor duplicated test setup into pytest fixtures.
- Remove any unjustified dependencies.
- Re-run flake8 until the report is clean.

---

## Step 3: Report

Print a verification report:

```
## Verification Report: <Feature Name>

| Gate | Result | Notes |
|------|--------|-------|
| 1. Test Integrity | PASS/FAIL | <details> |
| 2. Health Check | PASS/FAIL | <details> |
| 3. Deployment Readiness | PASS/FAIL | <details> |
| 4. Maintainability | PASS/FAIL | <details> |

**Overall: VERIFIED / FAILED**
```

## Hard Rules
- NEVER skip a gate. All four must pass.
- NEVER mark VERIFIED if any gate failed and was not re-verified after fixing.
- NEVER weaken a gate ("coverage is close enough"). The threshold is the threshold.
- NEVER modify acceptance criteria to make them pass. The spec is the contract.
- If a gate reveals a spec problem, stop and tell the user to update the spec first.