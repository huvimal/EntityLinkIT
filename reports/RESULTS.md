# EntityLinkIT — measured local run

Fictional IT asset catalog; lexical entity linking with explicit abstention. No learned model or production asset discovery.

## Results

```json
{
  "cases": [
    {
      "query": "gateway-east",
      "expected": "gateway-east",
      "predicted": "ambiguous"
    },
    {
      "query": "gatway-east",
      "expected": "gateway-east",
      "predicted": "ambiguous"
    },
    {
      "query": "gateway",
      "expected": "ambiguous",
      "predicted": "ambiguous"
    },
    {
      "query": "satellite",
      "expected": "unknown",
      "predicted": "unknown"
    },
    {
      "query": "cache-primary",
      "expected": "cache-primary",
      "predicted": "cache-primary"
    },
    {
      "query": "billing-prod",
      "expected": "billing-prod",
      "predicted": "billing-prod"
    },
    {
      "query": "queue",
      "expected": "queue-dev",
      "predicted": "queue-dev"
    }
  ],
  "accuracy": 0.7142857142857143,
  "checks": [
    "Ambiguous aliases abstain",
    "Out-of-catalog input abstains"
  ],
  "scope": "Fictional IT asset catalog; lexical entity linking with explicit abstention. No learned model or production asset discovery."
}
```

Local experiment assertions passed. This does not establish production readiness or performance on real customer data. Source fingerprints and dependency versions are in results.json.
