# exchange-rate-api
An api that returns exchange rate for currencies

### Exchange Rate API Task
Create an API that can accept two currencies and return the exchange rate for the currencies.

### Representation
Currencies are represented as their standard format in three letters like USD, NGN.

### API Specification
The api should be designed as follows. The rate from currency1 to currency2, the example below shows an exchange from USD to NGN (dollar to naira) which will return a value 410.56.

##### Routes
`/exchange-rate/`

##### Body
```json
{
  "currency1": "USD",
  "currency2": "NGN"
}
```

##### Response
```json
{
  "rate": 410.56
}
```

##### Types
```yaml
currency1: str
currency2: str
rate: float
```

