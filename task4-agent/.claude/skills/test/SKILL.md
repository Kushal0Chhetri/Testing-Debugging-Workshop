---
name: test
description: Write comprehensive unit tests for component behavior in isolation
---

<task>
Write comprehensive unit tests for a program that validate behavior in isolation.

Unit tests are executable documentation—they tell the story of what your component does and why. Write tests that validate behavior, not implementation. Cover happy paths, edge cases, error conditions, and all critical business logic.

Follow this process:

1. **Review component specification:**
   - Read source code and documentation to understand functionality
   - Extract all public methods, edge cases, and error conditions to test
   - Ask the user any clarifying questions to resolve ambiguity, prioritize test cases, determine the relevance of edge cases, etc. in an adversarial interview format using the QA engineer persona
2. **Write happy path tests:**
   - Test each public method with typical inputs
   - Verify expected outputs match specification
   - Use realistic data from constellation context

3. **Write edge case tests:**
   - Test boundary conditions (empty, max, min, null)
   - Test unusual but valid inputs
   - Verify graceful handling

4. **Write error condition tests:**
   - Test all error paths
   - Verify error handling per specification
   - Confirm recovery behavior

5. **Write critical logic tests:**
   - Achieve 100% branch coverage of business logic
   - Test all decision paths
   - Verify against gap success criteria
</task>


<thinking>
Before writing tests, analyze:
1. What are ALL public methods that need testing?
2. What edge cases exist (boundary conditions, empty inputs, null values)?
3. What error conditions must be handled?
4. What is the critical business logic that requires 100% coverage?
5. How can tests serve as executable documentation?
</thinking>

<output-format>
Write unit tests using the pytest framework following the python3 and pytest standards and coding patterns:

**Test File Structure Pattern:**

1. **File Header Documentation:**
   - Component under test
   - Purpose statement
   - Specification reference
   - Coverage summary (happy/edge/error/critical)
   - Success criteria being validated

2. **Test Organization:**
   - Group related tests by scenario/feature
   - Use descriptive names that explain behavior
   - Follow AAA pattern (Arrange, Act, Assert)
   - Make tests independent and fast (<100ms each)

3. **Test Categories to Cover:**
   - Happy paths: typical usage with valid inputs
   - Edge cases: boundary conditions (empty, null, max, min)
   - Error conditions: all error paths and recovery

Verify against specification, not just "something happened"
</output-format>

<instructions>
CRITICAL: Write tests as executable documentation that tell the story of what your component does.

NEVER write tests that:
- Test implementation details instead of behavior
- Use vague assertions like "assert result" without checking a specific value
- Skip edge cases or error conditions
- Lack descriptive test names explaining the scenario being tested
- Fail to validate against the specification or acceptance criteria
- Use unrealistic or placeholder test data
- Say "test that it works" without specifying WHAT works and HOW
- Skip boundary conditions (empty strings, zero-length lists, negative numbers)
- Forget to test error paths and exception handling
- Depend on execution order of other tests (tests MUST be independent)
- Skip critical business logic (score calculation, answer matching)
- Use magic numbers without explanation
- Call input() or other blocking I/O without mocking via monkeypatch
- Write to the real filesystem without using tmp_path or a temp directory

ALWAYS:
- Write descriptive test names following test_<method>_<scenario> pattern
- Use AAA pattern (Arrange, Act, Assert) with clear separation
- Test behavior and outcomes, not internal implementation details
- Use monkeypatch to mock input() so tests never block on stdin
- Use capsys to capture and verify printed output
- Use tmp_path fixture for any file I/O to avoid polluting the workspace
- Test ALL edge cases: empty question lists, missing files, case variations
- Test ALL error conditions: nonexistent quizzes, invalid menu choices
- Achieve 100% branch coverage of critical business logic (run_quiz scoring, answer matching)
- Make tests fast (each test MUST complete in < 100ms)
- Make tests independent (no shared state, no order dependencies)
- Validate against acceptance criteria from the QA Engineer specification
- Import from sample_app.quiz using the correct module path

REPEAT: Tests are executable documentation. Every test name should read like a specification. Use realistic data. Test behavior, not implementation.
</instructions>