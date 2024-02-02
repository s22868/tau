Feature: Change Page Test

  Scenario Outline: Change page with different browsers
    Given Start change page test with "<browser>"
    When User clicks on login button
    Then User should be redirected to the login page

  Examples:
    | browser  |
    | Chromium  |
    | Edge      |