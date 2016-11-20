# SlackBot

This is a first iteration at implementing the a simple Slack bot to interface with Jira and Confluence. It performs basic functions, such as allowing users to search and filter tickets, get information about a topic from confluence and ticket bugs - all within the Slack interface. 

# Setup
Set-up for the SlackBot is simple. You'll need the following to get started:
* Slack API Token
* Jira username and password
* Jira host server

Step 1: Navigate to SlackBot directory
Step 2: Launch setup script, including your api token and jira credentials as arguments

``` python
python setup.py [TOKEN] [JIRA USER] [JIRA PASS]
```

More to come...