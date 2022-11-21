*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallee  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username needs to be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  janne  janne1
    Output Should Contain  Password needs to be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  janne  janneeee
    Output Should Contain  Password needs at least 1 number and character

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
