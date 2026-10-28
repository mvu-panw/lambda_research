# Enabling single sign-on (SSO) - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/enabling-sso/

Skip to content

# Enabling single sign-on (SSO)#

This guide describes how to enable single sign-on (SSO), which allows users
to authenticate to Lambda Cloud through your organization's existing identity
provider (IdP). Enabling SSO offers several advantages:

- Users don't need to manage a separate set of credentials for Lambda Cloud.

- Your organization's users are automatically added to your account when they
 first log in.

- Your IdP remains the single source of truth for managing user access.

## Prerequisites#

To set up SSO for your Lambda Cloud account, you must have:

- A 1-Click Cluster (1CC).

- The Account Admin role in your
 Lambda Cloud account.

- Permission to set up application integrations for your identity provider.

- Permission to create and modify DNS TXT records for the domain name that
 you plan to enroll in SSO.

## Getting started#

### Choose an SSO alias#

Before you set up SSO, take a moment to identify the SSO alias you want to
associate with your Lambda Cloud account. This alias is used to route users to
the correct account or IdP when they sign in. Your alias must satisfy the
following naming requirements:

- It must be between 1 and 50 characters in length.

- It must contain only lowercase letters, numbers, hyphens, or underscores.

- It must begin and end with a letter or number.

Tip

Choose a straightforward, easy-to-remember value for your alias. For
example, if your account is shared across Example Co., example or
example-co are both strong choices.

### Request an invitation to set up SSO#

Ask your Lambda account manager for an invitation email to set up SSO for your
existing Lambda Cloud account. Include your preferred SSO alias and the email
domains that you want to associate with the connection.

## Setting up SSO#

### Configure SSO for your identity provider#

To configure SSO for your identity provider:

- 

Open the invitation email, and then click the link to begin enrolling your
 account in SSO. You're taken to the SSO setup wizard.

Note

The invitation link can only be used once. After you open the link,
you have six hours to complete the SSO configuration process. If your
link expires, contact your Lambda account manager and ask them to
generate a new link.

- 

On the Configure Your Connection page, click Single Sign-On.

- Select your identity provider from the list of supported providers, and
 then click Next. If you don't see your provider on the list, choose
 Custom SAML or Custom OIDC, depending on your provider's
 authentication protocol.

- 

Follow the instructions to configure SSO for your selected provider. If
 your provider uses SAML authentication, make sure the provider is set up
 to send the following attributes in its assertions:

- NameID formatting: Use the
 urn:oasis:names:tc:SAML:2.0:nameid-format:persistent format.

- Email attribute: Include the user's email address in either the
email attribute or the
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
attribute.

- 

After you've finished the setup process, click Done. You're taken back
 to the Configure Your Connection page.

### Verify ownership of your domain#

To complete SSO setup for your domain, you must verify that you own the domain:

- On the Configure Your Connection page, click
 Domain Verification.

- In the Add Domain tab, input your target domain and then click
 Add Domain.

- Follow the instructions for verifying your domain.

- After your domain name has been verified, click Done. You're taken back
 to the Configure Your Connection page.

- On the Configure Your Connection page, click Enable Connection.
 A modal appears.

- Click Proceed to finish enabling SSO for your domain.

After the connection is enabled, users can:

- Sign in through your IdP by visiting the Lambda Cloud console, clicking
 Continue with SSO, and entering your account's SSO alias.

- Sign in directly at https://cloud.lambda.ai/login/<alias>, replacing
 <alias> with your account's SSO alias.

When a user signs in to an account using SSO for the first time, they're
automatically added to the account associated with the SSO connection. If they
already belong to the account, their existing identity is automatically linked
to the account's SSO connection.

Important

If a user's email address is already associated with a different Lambda
Cloud account, contact your Lambda account manager before that user signs
in with SSO.

## Next steps#

- For details on managing account and workspace users, see
 Managing identities and groups.

- For an overview of how access control works on Lambda Cloud, see the
 Identity and access management (IAM) overview.

 Back to top
