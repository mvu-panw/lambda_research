# Billing overview - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/billing/

Skip to content

# Billing#

This page explains how Lambda bills each of its public cloud resources.

## Billable resources#

Lambda Cloud charges for the following resources:

- On-Demand Cloud (ODC) instances

- 1-Click Clusters (1CCs)

- Filesystems

Charges include sales tax, which is based on the location provided in your
billing information.

### On-Demand Cloud (ODC) instances#

ODC prices instances by hourly usage and bills in one-minute increments.
Billing begins the moment you launch an instance and the instance passes
health checks, and ends the moment you terminate the instance. Instances are
billed for as long as they're running, regardless if they're actively being
used. You receive weekly invoices for the previous week's usage.

To view current ODC instance pricing, see the pricing table on the
On-Demand Cloud page.

### 1-Click Clusters (1CCs)#

1CCs are priced per GPU per hour and billed in weekly increments according to
the terms of your reservation. You receive a billing summary during the 1CC
reservation process and an invoice by email when your reservation is approved.
After receiving the invoice, you have ten days to pay for your reservation.

To view current 1CC pricing, see the pricing table on the
1-Click Clusters page.

### Filesystems#

Filesystems are billed per GiB used per month in one-hour increments. For
example, at a rate of $0.20 per GiB per month:

- If you use 1,000 GiB continuously for a full month (720 hours), you'll
 be billed $200.00.

- If you use 1,000 GiB continuously for a full day (24 hours), you'll be
 billed $6.67.

Important

The rate above is used for example purposes and might not reflect
current pricing. The actual price will be displayed when you create your
filesystem.

Billing continues as long as a filesystem exists, even if it's not mounted to an
instance. There is no minimum storage period, and you are not charged for
ingress or egress.

## Credits and refunds#

Lambda issues refunds in the form of service credits toward future Lambda
Cloud usage. These credits can't be redeemed for cash and can't be used toward
purchases of other Lambda products or services. The credits expire 12 months
after they've been issued, and are subject to the
Lambda Cloud Terms of Service.

## Next steps#

For guidance on managing billing for your account, see
Managing billing.

 Back to top
