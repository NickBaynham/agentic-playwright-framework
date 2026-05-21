@feature_tag
Feature: <Feature Name>
  <Business goal or feature description in one or two lines.>

  Background:
    Given <shared precondition>

  @ui @smoke @automatable
  Scenario: <Scenario name>
    Given <starting condition>
    When <user action>
    Then <expected result>
    And <additional expected result>

  @ui @regression @automatable
  Scenario Outline: <Scenario outline name>
    Given <starting condition>
    When <user performs action with "<data_field>">
    Then <expected result for "<data_field>">

    Examples:
      | data_field |
      | value_a    |
      | value_b    |
