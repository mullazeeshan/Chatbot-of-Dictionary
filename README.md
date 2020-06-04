# Dictionary Bot using Amazon Lex, Amazon Lambda and Oxford Dictionary API
This is a simple dictionary chatbot which tell meaning of any word.

# Requirements:
1. Amazon AWS Account
2. Amazon Lex
3. Amazon Lambda
4. Oxford Dictionary API account

# Steps:
1. Create zip of DictionaryBot_Export.json.
2. Import above zip as New Bot into Amazon Lex.
3. Create zip of contents of Lambda Function folder.
4. Create a new function in Amazon Lambda with runtime as python 3.6 and choose lambda_basic_execution as existing role.
5. Upload zip created in Step 3, use handler as "lambda_function.lambda_handler" and then save.
6. Now test your bot through LEX console.
7. Publish your LEX BOT and use Slack communication channel to integrate with slack.


# Integrating with SLACK
[Click this Link and Follow Steps](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-association.html)


# SLACK INVITE LINK
[Click this link to join slack workspace and start interacting with Bot.](https://join.slack.com/t/zeeshanmulla/shared_invite/zt-e7r9ueqq-wuVucXOSztbBooUFNa610g)

# Screenshots
![slack bot dictionary screenshot 1](https://user-images.githubusercontent.com/29397302/83795440-15068500-a6bd-11ea-9e1e-e1b3b5904cb4.JPG)
https://media.giphy.com/media/lQPRTrP3tZxaxyoF2G/giphy.gif


