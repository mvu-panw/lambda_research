# Firewalls - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/firewalls/

Skip to content

# Firewalls#

You can restrict incoming traffic to the instances in a workspace, including
1-Click Cluster management (head)
nodes, by creating firewall rules on the
Firewall page in
the Lambda Cloud console. You can create global rules that apply to all of
the instances in the workspace, or rulesets scoped to individual instances and
their regions.

By default, Lambda allows only incoming ICMP traffic or TCP traffic on port 22
(SSH).

Note

You can also use the Lambda Cloud API to manage your global firewall rules
and per-instance rulesets programmatically. For details, see
Firewalls
in the Lambda Cloud API browser.

## Managing your global firewall rules#

Warning

Each port you open increases the attack surface of your instances. Make
sure to vet any services you run on your instances, and be judicious about
exposing new ports. If possible, restrict your incoming traffic to known
sources.

### Creating a global firewall rule#

You can create up to 100 global firewall rules per workspace.

To create a new global firewall rule:

- Navigate to the Global rules tab on the
 Firewall settings page
 in the Lambda Cloud console.

- In the Rules section, click Edit rules to begin creating a rule.

- Click Add rule.

- 

From the Type dropdown, select a rule type:

- Custom TCP: Manually allow incoming TCP traffic.

- Custom UDP: Manually allow incoming UDP traffic.

- HTTPS: Automatically allow incoming traffic to TCP/443.

- HTTP: Automatically allow incoming traffic to TCP/80.

- SSH: Automatically allow incoming traffic to TCP/22.

- All TCP: Automatically allow all incoming TCP traffic.

- All UDP: Automatically allow all incoming UDP traffic.

- ICMP: Automatically allow all incoming ICMP traffic.

- 

In the Source field, enter an IP address or CIDR range to restrict
 incoming traffic:

- Click to auto-fill your current IP.

- Enter a single IP (for example, 203.0.113.1).

- Enter a CIDR block (for example, 203.0.113.0/24).

- Use 0.0.0.0/0 to allow traffic from any source (not recommended).

- 

If you chose Custom TCP or Custom UDP as your rule type, enter a port
 range in the Port range field. Enter a single port (for example, 8080)
 or a range (for example, 8080-8081).

- (Optional) Add a description for the rule in the Description field.

- (Optional) Click Add rule to add additional rules.

- Click Update firewall rules to apply your changes.

### Updating a global firewall rule#

To update a global firewall rule:

- Navigate to the Global rules tab on the
 Firewall settings page
 in the Lambda Cloud console.

- In the Rules section, click Edit rules.

- Find the rule you want to update and modify it as needed.

- Click Update firewall rules to apply your changes.

### Deleting a global firewall rule#

To delete a global firewall rule:

- Navigate to the Global rules tab on the
 Firewall settings page
 in the Lambda Cloud console.

- In the Rules section, click Edit rules.

- Click the x next to the
 rule you want to delete.

- Click Update firewall rules to apply your changes.

Warning

If you delete the rule that allows incoming traffic to port TCP/22, you
won't be able to access your instances using SSH.

### Viewing your global firewall rules#

You can view a list of your existing global firewall rules by visiting the
Global rules tab on the Firewall settings page
in the Lambda Cloud console. You can also retrieve your rules programmatically
using the Lambda Cloud API. For more information, see
List inbound firewall rules
in the Lambda Cloud API browser.

## Managing your per-instance firewall rulesets#

In addition to global firewall rules, you can create per-instance rulesets
scoped to individual regions. These rulesets have the following characteristics:

- You must attach rulesets during the instance launch process. You can't attach
 them after the instance has been launched.

- You can't remove rulesets from an instance after the instance has been
 launched.

- If you modify a ruleset, the updates automatically apply to any instance
 that uses that ruleset.

- You can create up to 128 per-instance firewall rulesets per workspace.

### Creating a firewall ruleset#

To create a new firewall ruleset:

- Navigate to the Rulesets tab on the
 Firewall settings page
 in the Lambda Cloud console.

- Click Create new ruleset.

- Enter a name for the ruleset. Select a region, then click Next.

- Click Add rule.

- 

From the Type dropdown, select a rule type:

- Custom TCP: Manually allow incoming TCP traffic.

- Custom UDP: Manually allow incoming UDP traffic.

- HTTPS: Automatically allow incoming traffic to TCP/443.

- HTTP: Automatically allow incoming traffic to TCP/80.

- SSH: Automatically allow incoming traffic to TCP/22.

- All TCP: Automatically allow all incoming TCP traffic.

- All UDP: Automatically allow all incoming UDP traffic.

- ICMP: Automatically allow all incoming ICMP traffic.

- 

In the Source field, enter an IP address or CIDR range to restrict
 incoming traffic:

- Click to auto-fill your current IP.

- Enter a single IP (for example, 203.0.113.1).

- Enter a CIDR block (for example, 203.0.113.0/24).

- Use 0.0.0.0/0 to allow traffic from any source (not recommended).

- 

If you chose Custom TCP or Custom UDP as your rule type, enter a port
 range in the Port range field. Enter a single port (for example, 8080)
 or a range (for example, 8080-8081).

- (Optional) Add a description for the rule in the Description field.

- (Optional) Click Add rule to add additional rules to the ruleset.

- Click Create new firewall ruleset to save the ruleset.

### Updating a firewall ruleset#

To update a firewall ruleset:

- Navigate to the Rulesets tab on the
 Firewall settings page
 in the Lambda Cloud console.

- Find the ruleset that you want to update.

- Click the ⋮ menu next to the ruleset, then click Manage.

- Modify the ruleset as needed.

- Click Update firewall rules to apply your changes.

### Deleting a firewall ruleset#

To delete a firewall ruleset:

- Navigate to the Rulesets tab on the
 Firewall settings page
 in the Lambda Cloud console.

- Find the ruleset that you want to delete.

- Click the ⋮ menu next to the ruleset, then click Delete.

- Click Delete to confirm you want to delete the ruleset.

### Viewing your firewall rulesets#

You can view a list of your existing firewall rulesets by visiting the
Rulesets tab on the
Firewall rulesets page
in the Lambda Cloud console. You can also retrieve your rules programmatically
using the Lambda Cloud API. For more information, see
List inbound firewall rules
in the Lambda Cloud API browser.

 Back to top
