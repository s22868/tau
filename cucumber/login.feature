Feature: Login Test

  Scenario Outline: Login with different browsers
    Given Start login test with "<browser>"
    When User logs in with valid credentials
    Then User should be redirected to the home page

  Examples:
    | browser  |
    | Chromium  |
    | Edge      |