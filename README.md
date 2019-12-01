To use, simply make a POST request to / with the body:

```
{
  "question" : "How many episodes does Seinfeld have?"
}
```

You will receive a response containing:
```
{
  "error": "",
  "query": "",
  "result": ""
}
```

The "error" field will return empty if there are no errors, "query" field contains the SPARQL query and "result" field contains the answer(s) to the question, which can be a single element or array.
